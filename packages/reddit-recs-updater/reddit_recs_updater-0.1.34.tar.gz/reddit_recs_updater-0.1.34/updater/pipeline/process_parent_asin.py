from updater.utils.amzn_handler import get_amzn_variations
from updater.utils.db_handler import db_get_pds_by_asins, db_add_product_parent, db_add_pd, db_set_product_parent_id, db_add_product_brand, db_add_parent_asin
from updater.utils.ai_handler import get_openai_response_instr
from pydantic import BaseModel, Field
from pathlib import Path
import asyncio


class Category(BaseModel):
  product_titles: list[str] = Field(description="product titles of the items belonging to the category")
  product_asins: list[str] = Field(description="asins of the items belonging to the category")
  category_description: str = Field(description="category description highlighting 1-2 key distinguishing features or the differentiating model name, and optionally 1-2 minor differences within the category")

class Categories(BaseModel):
  categories: list[Category]


# Get variations products, add them to db, return variation products
async def process_parent_asin(parent_asin: str, brand_id: int) -> list[dict]:
  # Get variations from amazon
  amzn_variations_result = await get_amzn_variations(parent_asin)
  print(f"No. of variations: {len(amzn_variations_result.items)}")
  
  variation_products = []
  
  if amzn_variations_result and amzn_variations_result.variation_summary.variation_count > 1:
    # Use llm to group and form parents
    categories = await group_variations(amzn_variations_result)
    
    # Create product_parents
    for category in categories:
      product_parent = await db_add_product_parent({'category_description': category.category_description})
      product_parent_id = product_parent['id']
            
      # Update product_parent_id for existing child products from db if any
      products_to_update = await db_get_pds_by_asins(category.product_asins)
      asins_to_update = [product['asin'] for product in products_to_update]
      print(f"asins_to_update: {asins_to_update}")
      
      if products_to_update:
        products_to_update_ids = [product['id'] for product in products_to_update]
        products_updated = await db_set_product_parent_id(product_parent_id, products_to_update_ids)
        variation_products.extend(products_updated)
        print(f"Updated {len(products_updated)} products - product_parent_id set to {product_parent_id}")
        
      # Add non-existing child (products & product_brands) to db
      asins_to_add = [asin for asin in category.product_asins if asin not in asins_to_update]
      print(f"asins_to_add: {asins_to_add}")
      
      items_to_add = [item for item in amzn_variations_result.items if item.asin in asins_to_add]
      for item in items_to_add:
        pd_data = {
          'asin': item.asin if item.asin else None,
          'product_parent_id': product_parent_id,
          'parent_asin': parent_asin,
          'title': item.item_info.title.display_value if item.item_info and item.item_info.title else None,
          'amzn_url': item.detail_page_url if item.detail_page_url else None,
          'amzn_price': item.offers.listings[0].price.amount if item.offers and item.offers.listings and item.offers.listings[0] and item.offers.listings[0].price else None,
          'img_url': item.images.primary.large.url if item.images and item.images.primary and item.images.primary.large else None
        }
        pd = await db_add_pd(pd_data)
        await db_add_product_brand(pd['id'], brand_id)
        
        variation_products.append(pd)
    
      print(f"Added {len(items_to_add)} products with parent_product_id {product_parent_id}")
        
  # Add parent_asin to parent_asins table
  await db_add_parent_asin(parent_asin)
  
  return variation_products
    

async def group_variations(amzn_variations_result: dict) -> Categories:
  current_dir = Path(__file__).parent
  
  sys_prompt_path = current_dir.parent / "llm_prompts" / "group_variations_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()

  items_str = ""
  for item in amzn_variations_result.items:
    variation_attr = []
    for attr in item.variation_attributes:
      variation_attr.append(attr.value)
    items_str += f"- {variation_attr}: {item.item_info.title.display_value if item.item_info and item.item_info.title else 'No title'} (${item.offers.listings[0].price.amount if item.offers and item.offers.listings and item.offers.listings[0] and item.offers.listings[0].price else 'NA'}) (ASIN: {item.asin})\n"
    
  user_prompt = f"Categorize the following items based on their critical features and specs:\n{items_str}"
  
  model = "gpt-4o-mini"
  
  max_retries = 5
  retry_count = 0

  while retry_count < max_retries:
    print(f"Group vars attempt no. {retry_count + 1}/{max_retries}")
    
    # vary temp with more retries
    temp = 0 + (retry_count * 0.2)
    response = await get_openai_response_instr(sys_prompt, user_prompt, model, temp, Categories)

    asins_from_response = set(asin for category in response.categories for asin in category.product_asins)
    original_asins = set(item.asin for item in amzn_variations_result.items)
    
    if original_asins == asins_from_response:
      return response.categories
    else:
      print(f"Retry {retry_count + 1}: Mismatch in original and response ASINs")
      print(f"Missing asins: {original_asins - asins_from_response}")
      print(f"Extra asins: {asins_from_response - original_asins}")
      retry_count += 1
      # Add a delay that increases with each retry
      delay = (retry_count + 1) * 5  # 5 seconds for first retry, 10 for second, 15 for third
      print(f"Waiting for {delay} seconds before next retry...")
      await asyncio.sleep(delay)

  print(f"Error: Failed to get a matching response after {max_retries} retries")
  return None

if __name__ == "__main__":
  import asyncio
  asyncio.run(process_parent_asin("B0DC69QWGC"))
