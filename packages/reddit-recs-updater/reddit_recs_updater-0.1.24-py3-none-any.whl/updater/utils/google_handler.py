import asyncio
import aiohttp
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from updater.utils.db_handler import db_get_api_tracker_data, db_update_api_tracker_data, db_add_api_tracker_data
import os
from typing import List, Dict, Optional
import json

load_dotenv()

google_search_engine_id = os.environ['google_searchengine_id']
google_api_key_1 = os.environ['google_api_key_1']
google_api_key_2 = os.environ['google_api_key_2']
google_api_key_3 = os.environ['google_api_key_3']
google_api_key_4 = os.environ['google_api_key_4']
google_api_key_5 = os.environ['google_api_key_5']
google_api_key_6 = os.environ['google_api_key_6']
google_api_key_7 = os.environ['google_api_key_7']
google_api_key_8 = os.environ['google_api_key_8']
google_api_key_9 = os.environ['google_api_key_9']
google_api_key_10 = os.environ['google_api_key_10']
google_api_key_11 = os.environ['google_api_key_11']
google_api_key_12 = os.environ['google_api_key_12']
google_api_key_13 = os.environ['google_api_key_13']
google_api_key_14 = os.environ['google_api_key_14']

async def fetch_google_results(search_query: str, search_site: str, search_range_days: Optional[int], max_results: int) -> List[Dict[str, str]]:
  # each call returns 10 results
  if search_range_days:
    date_restriction = f'd{search_range_days}'
  else:
    date_restriction = ""
  
  results_fetched = 0
  start_index = 1
  all_items = []

  async with aiohttp.ClientSession() as session:
    while results_fetched < max_results:
      api_key_name = get_available_api_key_name()
      update_api_key_usage(api_key_name)
      api_key = os.environ[api_key_name]
      
      # Construct api call url with parameters
      url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&cx={google_search_engine_id}&key={api_key}&dateRestrict={date_restriction}&siteSearch={search_site}&siteSearchFilter=i&start={start_index}"

      async with session.get(url) as response:
        data = await response.json()

      items = data.get('items', [])
      all_items.extend(items)

      results_fetched += len(items)
      start_index += len(items)

      # Break if no more results are returned
      if not items:
        break

  return all_items[:max_results]


def get_available_api_key_name() -> str:
  today = datetime.now(timezone.utc).date().isoformat()
  
  for key_num in range(1, 15):
    key_name = f'google_api_key_{key_num}'
    tracker_data = db_get_api_tracker_data(key_name, today)
    
    if not tracker_data:
      db_add_api_tracker_data(key_name, 0, today)
      return key_name
    elif tracker_data['call_count'] < 100:
      return key_name
  
  raise Exception("All API keys have reached their daily limit")

def update_api_key_usage(key_name: str):
  today = datetime.now(timezone.utc).date().isoformat()
  
  tracker_data = db_get_api_tracker_data(key_name, today)
  if tracker_data:
    call_count = tracker_data['call_count']
    db_update_api_tracker_data(key_name, call_count + 1, today)
  else:
    db_add_api_tracker_data(key_name, 1, today)



# For testing purposes
if __name__ == "__main__":
  search_query = "razer naga"
  search_site = "amazon.com"
  search_range_days = None
  max_results = 10

  results = asyncio.run(fetch_google_results(search_query, search_site, search_range_days, max_results))

  print(json.dumps(results, indent=2))
  
  