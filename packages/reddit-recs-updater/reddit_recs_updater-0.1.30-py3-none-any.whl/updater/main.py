import asyncio
import time
from datetime import datetime, timezone, timedelta
from asyncpraw.models import Submission

from updater.utils.reddit_handler import load_all_subm_comments, get_subm_from_subm_id
from updater.utils.db_handler import db_get_processed_subms_ids, db_insert_opns, db_insert_subms_processed, db_get_all_pd_categories, db_update_last_processed

from updater.pipeline.gen_search_terms import gen_search_terms
from updater.pipeline.search import search_reddit
from updater.pipeline.has_opns_from_scan import scan_if_has_opns
from updater.pipeline.prep_subm_for_llm import prep_subm_for_llm
from updater.pipeline.identify_opns import identify_opns
from updater.pipeline.perform_checks_on_opns import perform_checks_on_opns
from updater.pipeline.furnish_pd_info import furnish_pd_info
from updater.pipeline.furnish_sources import furnish_sources



# GET ALL PD CATEGORIES AND PROCESS
async def update_all_existing_pd_categories() -> None:
  
  # Get all pd_categories from db
  all_pd_categories = await db_get_all_pd_categories()
  
  # Process each pd_category
  for pd_category_dict in all_pd_categories:
    if pd_category_dict['name'] != "Portable monitor": # Exclude portable monitors for now
      last_processed = datetime.fromisoformat(pd_category_dict['last_processed'])
      if datetime.now(timezone.utc) - last_processed > timedelta(days=6):
        print(f"Pd_category {pd_category_dict['name']} last processed > 6 days ago, proceeding to update...")
        await update_existing_pd_category(pd_category_dict)


# PROCESSING FOR AN EXISTING PD CATEGORY
async def update_existing_pd_category(pd_category_dict: dict) -> None:
  print(f'Updating {pd_category_dict["name"]}...')
  unique_subms = []

  # Generate search terms, search Reddit to get subms
  search_terms = gen_search_terms(pd_category_dict['name'])
  search_max_results = 10
  unique_results_list = await search_reddit(search_terms, search_max_results)
  unique_subms_ids = [result['subm_id'] for result in unique_results_list]
  unique_subms = [await get_subm_from_subm_id(subm_id) for subm_id in unique_subms_ids]

  await process_subm_list(unique_subms, pd_category_dict)


  
# PROCESSING FOR A UNIQUE LIST OF SUBMISSIONS
async def process_subm_list(unique_subms: list[Submission], pd_category_dict: dict) -> None:
  print(f'Processing {len(unique_subms)} submissions...')

  # Get subms that have already been processed for this pd_category
  processed_subms_ids = await db_get_processed_subms_ids(pd_category_dict)
  
  # Process each submission in parallel
  process_subm_tasks = [asyncio.create_task(process_subm(subm, processed_subms_ids, pd_category_dict)) for subm in unique_subms]
  await asyncio.gather(*process_subm_tasks)

  # Update last_processed for pd_category
  await db_update_last_processed(pd_category_dict['id'])
  

# PROCESSING FOR A SUBMISSION
async def process_subm(subm: Submission, processed_subms_ids: list[str], pd_category_dict: dict) -> None:

  # If subm processed already, process existing subm (for now will skip)
  if subm.id in processed_subms_ids:
    print(f'Skipping subm: {subm.id} because it has already been processed')
    return # For now we will skip existing subms

  # Else, process new subm
  # Initialize variables
  comments_analyzed_ids = []
  opns_extracted = []
  checked_opns = []
  checked_opns_w_pd_info = []
  checked_opns_w_pd_and_sources = []
  ready_to_go_opns = []
  pd_category_name = pd_category_dict['name']
  
  # Load subm and prep for LLM
  subm_loaded = await load_all_subm_comments(subm)
  subm_data_for_llm, subm_stats = await prep_subm_for_llm(subm_loaded)

  # Scan subm to check if worth digging deeper
  has_opns_from_scan = await scan_if_has_opns(subm_data_for_llm, pd_category_name)
  if has_opns_from_scan:
    # Extract opinions from subm
    opns_extracted = await identify_opns(subm_data_for_llm, pd_category_name)
    # Add pd_category_id to each opn for ease later
    [opn.update({'pd_category_id': pd_category_dict['id']}) for opn in opns_extracted]
    if opns_extracted:
      # Check if extracted opinions are valid
      checked_opns = await perform_checks_on_opns(opns_extracted, subm_loaded, pd_category_name)
      # Filter opns based on validity
      checked_opns_passed = [opn for opn in checked_opns if opn['is_opn']]
      # Furnish product info and sources
      checked_opns_w_pd_info = await furnish_pd_info(checked_opns_passed, pd_category_name)
      checked_opns_w_pd_and_sources = furnish_sources(checked_opns_w_pd_info, subm_loaded)
      # Check if at the end of it there are opinions that are ready to go
      ready_to_go_opns = [opn for opn in checked_opns_w_pd_and_sources if opn['sources']]

  
  # Update db
  comments_analyzed_ids = [comment.id for comment in subm_loaded.comments.list()]

  # Insert subms_processed
  subms_processed_data = {
    "subm_id" : subm.id,
    "subm_title" : subm.title,
    "subm_permalink" : subm.permalink,
    "subm_subreddit" : subm.subreddit.display_name,
    "subm_stats" : subm_stats,
    "pd_category_id" : pd_category_dict['id'],
    "comments_analyzed_ids" : comments_analyzed_ids,
    "has_opns_from_scan" : has_opns_from_scan,
    "last_updated": datetime.fromtimestamp(time.time(), tz=timezone.utc).isoformat()
  }
  subms_processed_result = await db_insert_subms_processed(subms_processed_data)

  # Insert opns
  for opn in checked_opns_w_pd_and_sources:  
    opns_data = {
      "pd_category_id" : pd_category_dict['id'],
      "subm_processed_id" : subms_processed_result['id'],
      "opn_summary" : opn['opinion_summary'],
      "username" : opn['username'],
      "pd_brand_identified" : opn['pd_brand'],
      "pd_model_or_name_identified" : opn['pd_model_or_name'],
      "pd_key_specs_identified" : opn['pd_key_specs'],
      "pd_url_identified" : opn['pd_url'],
      "is_opn" : opn['is_opn'],
      "is_owner" : opn['is_owner'],
      "product_brand_id" : opn['product_brand_id'],
      "sources" : opn['sources'],
      "latest_source_date" : opn['latest_source_date']
    }
    await db_insert_opns(opns_data)

  print(f'*--> Parallel task completed: Retreived {len(ready_to_go_opns)} opns from {subm.url}')



if __name__ == "__main__":
  # pd_category_dict = {
  #   "name" : "Air purifier",
  #   "id" : 65
  # }
  # asyncio.run(update_existing_pd_category(pd_category_dict))
  asyncio.run(update_all_existing_pd_categories())
  
