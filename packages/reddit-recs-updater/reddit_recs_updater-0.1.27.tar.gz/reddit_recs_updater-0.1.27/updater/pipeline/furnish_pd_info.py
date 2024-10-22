from updater.utils.amzn_handler import is_amazon_url, extract_asin_from_url, get_items_data_from_asins, search_pd_amzn
from updater.utils.ai_handler import get_openai_response
from updater.utils.google_handler import fetch_google_results, upsert_api_tracker_db
from updater.utils.db_handler import db_get_pd_by_asin, db_add_pd, db_add_brand_if_new, db_get_product_brand_by_pd_and_category, db_get_brand_by_pd_id, db_add_product_brand, db_get_parent_asin, db_get_product_by_parent_asin
from updater.pipeline.process_parent_asin import process_parent_asin
from typing import Optional
from paapi5_python_sdk.models.item import Item
from pathlib import Path
import inflect
import asyncio

# Initialize lock 
# Purpose is to prevent race conditions when checking and adding products, brands, and product_brands to db
process_opn_w_db_lock = asyncio.Lock()


# Takes checked opns list -> to each opn adds product_brand_id (int/None)
async def furnish_pd_info(checked_opns: list[dict], pd_category_name: str) -> list[dict]:
  opns_w_asin = []
  opns_wo_asin = []
  
  # Initialize product_brand_id and asin for each opn
  for opn in checked_opns:
    opn['product_brand_id'] = None
    opn['asin'] = None
  
  # Check filtered opns for asin and split into respective groups
  for opn in checked_opns:
    print(f'\nChecking for asin for: {opn["username"]}...')
    initial_url = opn['pd_url']
    if initial_url and is_amazon_url(initial_url):
      opn['asin'] = extract_asin_from_url(initial_url) # Extracts asin from URL even if shortened
      if opn['asin']:
        opns_w_asin.append(opn)
        print(f'-> ASIN found, no need to search: {initial_url}')
      else:
        opns_wo_asin.append(opn)
        print(f'-> ASIN NOT found: {initial_url}')
    else:
      print(f'-> Amzn url NOT found for: {opn["username"]}')
      opns_wo_asin.append(opn)

  # Create tasks for both groups of opns
  print(f'\nCreating tasks for {len(opns_w_asin)} opns with asin and {len(opns_wo_asin)} opns without asin...')
  tasks_w_asin = [asyncio.create_task(process_opn_w_asin(opn, opn['asin'])) for opn in opns_w_asin]
  tasks_wo_asin = [asyncio.create_task(process_opn_wo_asin(opn, pd_category_name)) for opn in opns_wo_asin]

  # Combine all tasks
  all_tasks = tasks_w_asin + tasks_wo_asin

  # Wait for all tasks to complete
  print(f'Processing {len(all_tasks)} total tasks...')
  processed_opns = await asyncio.gather(*all_tasks)
  
  # Update api tracker db for google call usage
  await upsert_api_tracker_db()

  # Filter only opns that have product_brand_id
  opns_w_product_brand_id = [opn for opn in processed_opns if opn['product_brand_id']]

  return opns_w_product_brand_id




# Process opn with asin (return opn with product_brand_id)
async def process_opn_w_asin(opn: dict, asin: str) -> dict:
  pd_category_id = opn['pd_category_id']
  
  # Lock to prevent race conditions when checking and adding brands and products
  async with process_opn_w_db_lock:
    # Check db for product with asin
    db_pd = await db_get_pd_by_asin(asin)
    
    # If in db...
    if db_pd:
      db_pd_id = db_pd['id']
      # Check if product_brand exists
      product_brand = await db_get_product_brand_by_pd_and_category(db_pd_id, pd_category_id)
      # If product_brand exists, set product_brand_id
      if product_brand:
        opn['product_brand_id'] = product_brand['id']
      # If product_brand does not exist, add brand using brand name and pd_category_id, then add product_brand to db
      else:
        brand_template = await db_get_brand_by_pd_id(db_pd_id)
        brand_name = brand_template['name_full']
        new_brand = await db_add_brand_if_new(brand_name, pd_category_id)
        opn['product_brand_id'] = (await db_add_product_brand(db_pd_id, new_brand['id']))['id']
    
    # If not in db, add amzn item to db (call amzn api, add to db, then set product_id and brand_id)
    else:
      amzn_items = await get_items_data_from_asins([asin])
      if amzn_items:
        amzn_item = amzn_items[0]
        product_brand_id = await add_amzn_item_to_db(amzn_item, pd_category_id)
        opn['product_brand_id'] = product_brand_id
      else:
        print(f'-> No Amazon item found for asin: {asin}, assume product no longer available')
  
  return opn


# Add new product to db based on amzn item data, return product_brand_id
async def add_amzn_item_to_db(amzn_item: Item, pd_category_id: int) -> int:
  
  # Add brand if not in db
  brand_name = amzn_item.item_info.by_line_info.brand.display_value if amzn_item.item_info and amzn_item.item_info.by_line_info and amzn_item.item_info.by_line_info.brand else None
  brand = await db_add_brand_if_new(brand_name, pd_category_id)
  brand_id = brand['id']
  
  # Add product (incl parent product if applicable) to db
  product_parent_id = None
  parent_asin = amzn_item.parent_asin
  
  # If parent asin, and parent asin not in db, and there is another product with the same parent asin, then get variations products and add them to db...
  if parent_asin and not await db_get_parent_asin(parent_asin) and await db_get_product_by_parent_asin(parent_asin):
    variation_products = await process_parent_asin(parent_asin, brand_id)
    pd = next((product for product in variation_products if product['asin'] == amzn_item.asin), None)
  # ...else add product as normal
  else:
    pd_data = {
      'asin': amzn_item.asin if amzn_item.asin else None,
      'product_parent_id': product_parent_id,
      'parent_asin': parent_asin,
      'title': amzn_item.item_info.title.display_value if amzn_item.item_info and amzn_item.item_info.title else None,
      'amzn_url': amzn_item.detail_page_url if amzn_item.detail_page_url else None,
      'amzn_price': amzn_item.offers.listings[0].price.amount if amzn_item.offers and amzn_item.offers.listings and amzn_item.offers.listings[0] and amzn_item.offers.listings[0].price else None,
      'img_url': amzn_item.images.primary.large.url if amzn_item.images and amzn_item.images.primary and amzn_item.images.primary.large else None
    }
    pd = await db_add_pd(pd_data)
  
  product_id = pd['id']
  
  product_brand = await db_add_product_brand(product_id, brand_id)
  product_brand_id = product_brand['id']
  
  return product_brand_id




async def process_opn_wo_asin(opn: dict, pd_category_name: str) -> dict:
  # If no brand identified but url exists, try to get brand from url (None if cannot find)
  if not opn['pd_brand'] and opn['pd_url']:
    opn['pd_brand'] = await get_pd_brand(opn['pd_url'])
  
  # Initialize pd_info
  pd_brand = opn['pd_brand']
  pd_model = opn['pd_model_or_name']
  pd_specs = opn['pd_key_specs']
  pd_info_components = [pd_brand, pd_model, pd_specs]

  # If enough info to search...
  if is_searchable(pd_info_components):
    
    # Construct search string
    pd_info_str_extracted = " ".join(filter(None, pd_info_components))
    # Add pd category name to search str if not already inside
    if contains_phrase_or_variants(pd_info_str_extracted, pd_category_name):
      search_str = pd_info_str_extracted
    else:
      search_str = f'{pd_info_str_extracted} {pd_category_name}'
    
    # Search Google site:amazon.com
    google_results = await fetch_google_results(search_str, "amazon.com", None, 10)
    if google_results:
      matched_item = await match_pd_info_from_google(google_results, pd_info_str_extracted)
      if matched_item and matched_item['asin']:
        opn = await process_opn_w_asin(opn, matched_item['asin'])

  # If product not identified, but pd_brand identified, add brand, then add product_brand to db leaving product_id as None
  if not opn['product_brand_id'] and pd_brand:
    # Lock to prevent race conditions when checking and adding brands and products
    async with process_opn_w_db_lock:
      brand = await db_add_brand_if_new(pd_brand, opn['pd_category_id'])
      product_brand = await db_add_product_brand(None, brand['id'])
      opn['product_brand_id'] = product_brand['id']
  
  # If both product and brand not identified, let product_brand_id be None

  return opn



# Helper function to check if there is enough info to search
def is_searchable(pd_info_components: list[str]) -> bool:
  valid_components = [c for c in pd_info_components if c]
  is_searchable = len(valid_components) >= 2
  return is_searchable


# Helper function to determine which amzn result matches provided pd info
async def match_pd_info(amzn_results: list[Item], pd_info_str_extracted: str) -> Optional[Item]:

  amzn_titles = [get_formatted_title(item) for item in amzn_results]
  amzn_titles_indexed = "\n".join(
    f"{i+1}. {title}" for i, title in enumerate(amzn_titles)
  )
  
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "is_amzn_item_match_pd_info_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  user_prompt = f"Product info string: {pd_info_str_extracted}\n\nAmazon product titles:\n{amzn_titles_indexed}"
  model = "gpt-4o-mini"
  response_format = { "type": "json_object" }

  print(f'\nChecking if any amzn result matches pd info...\n- Pd str extracted: {pd_info_str_extracted}\n')
  openai_response = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'match_pd_info')
  if openai_response and 'match_index' in openai_response:
    match_index = openai_response['match_index']
    if match_index is not None and 0 <= match_index < len(amzn_results):
      matched_item = amzn_results[match_index]
      print(f'-> Match found: {matched_item.item_info.title.display_value}')
      return matched_item
  
  print('-> No match found')
  return None

# Helper function to format amzn item title
def get_formatted_title(item: Item) -> str:
  title = "Unknown Title"
  brand = "Unknown Brand"

  if item.item_info and item.item_info.title:
    title = item.item_info.title.display_value

  if (item.item_info and 
      item.item_info.by_line_info and 
      item.item_info.by_line_info.brand):
    brand = item.item_info.by_line_info.brand.display_value

  return f"{title} (Brand: {brand})"



async def match_pd_info_from_google(google_results: list[dict], pd_info_str_extracted: str) -> Optional[dict]:
  filtered_results = []
  
  # Filter items to only include items with asin in url
  for result in google_results:
    asin = extract_asin_from_url(result.get('link', ''))
    if asin:
      result['asin'] = asin # Add asin to result
      filtered_results.append(result)
  
  if filtered_results:
    snippets = [result['snippet'] for result in filtered_results]
    snippets_indexed = "\n".join(
      f"{i+1}. {snippet}" for i, snippet in enumerate(snippets)
    )
    
    current_dir = Path(__file__).parent
    sys_prompt_path = current_dir.parent / "llm_prompts" / "is_google_amzn_item_match_pd_info_sys.txt"
    with open(sys_prompt_path, "r") as file:
      sys_prompt = file.read()
    user_prompt = f"Product info string: {pd_info_str_extracted}\n\nGoogle results:\n{snippets_indexed}"
    model = "gpt-4o-mini"
    response_format = { "type": "json_object" }
    openai_response = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'match_pd_info_from_google')
    if openai_response and 'match_index' in openai_response:
      match_index = openai_response['match_index']
      if match_index is not None and 0 <= match_index < len(filtered_results):
        matched_result = filtered_results[match_index]
        print(f'-> Match found: {matched_result["title"]}')
        return matched_result
  else:
    print('-> No match found')
    return None

  





async def get_pd_brand(url: str) -> Optional[str]:
  # Search Google using the URL
  search_results = await fetch_google_results(url, "", None, 3)

  # Prepare the search results for LLM input
  search_content = "\n\n".join([f"{i+1}. Title: {item['title']}\nSnippet: {item['snippet']}" for i, item in enumerate(search_results)])
  print(search_content)

  # Prepare prompts for LLM
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "get_pd_brand.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  user_prompt = f"Product URL: {url}\n\nTop search results for searching the product URL:\n{search_content}"

  # Use LLM to extract the brand
  response = await get_openai_response(sys_prompt, user_prompt, "gpt-4o-mini", { "type": "json_object" }, 'get_pd_brand')

  # Extract and return the brand
  brand = response.get("brand", None)
  return brand


def contains_phrase_or_variants(initial_text: str, phrase: str) -> bool:
  p = inflect.engine()
  words = phrase.lower().split()
  initial_text_lower = initial_text.lower()

  # Check if any word or its variant exists in the initial text
  for word in words:
    singular = p.singular_noun(word) or word
    plural = p.plural(word)
    
    if (singular in initial_text_lower or 
        plural in initial_text_lower):
      return True
    else:
      return False



