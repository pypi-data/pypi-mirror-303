import asyncio
import aiohttp
from datetime import datetime, date
from dotenv import load_dotenv
from updater.utils.db_handler import db_upsert_api_tracker_data, db_get_latest_tracker_row
import os
from typing import List, Dict, Optional


load_dotenv()

MAX_CALLS_PER_KEY = 80
NUMBER_OF_API_KEYS = 14
MAX_CALLS_PER_CACHE_UPDATE = 20

google_search_engine_id = os.environ['google_searchengine_id']
google_api_keys = [os.environ[f'google_api_key_{i}'] for i in range(1, NUMBER_OF_API_KEYS + 1)]

cache = {}
cache_call_count = 0
cache_lock = asyncio.Lock()

async def get_cached_api_key() -> str:
  global cache
  global cache_call_count
  
  async with cache_lock:  
    # If reached max calls per cache update, update db and reset cache
    if cache_call_count >= MAX_CALLS_PER_CACHE_UPDATE:
      await upsert_api_tracker_db()
      cache_call_count = 0
  
    # If cache is empty, initialize it with data from db
    if not cache:
      await initialize_cache()
    
    # Get latest key from cache
    latest_key_id = max(cache.keys())
    today = date.today()
    
    # If latest key is from today, handle same day key
    if cache[latest_key_id]['date'] == today:
      key_to_return = await handle_same_day_key(latest_key_id)
    else:
      # If latest key is not from today, create new key
      new_key_id = latest_key_id + 1
      new_key_num = 1
      key_to_return = await create_new_key(new_key_id, new_key_num)

    await update_cache()
    
    return key_to_return

async def initialize_cache() -> str:
  global cache
  latest_tracker_row = await db_get_latest_tracker_row()
  print(f"Latest tracker row: {latest_tracker_row}")
  key_id = latest_tracker_row['id']
  cache[key_id] = {
    'key_num': int(latest_tracker_row['key_name'].split('_')[-1]),
    'key_name': latest_tracker_row['key_name'],
    'call_count': latest_tracker_row['call_count'],
    'date': datetime.fromisoformat(latest_tracker_row['date']).date()
  }
  print(f"Initialized cache with key: {cache[key_id]}")

async def handle_same_day_key(key_id: int) -> str:
  global cache
  if cache[key_id]['call_count'] >= MAX_CALLS_PER_KEY:
    new_key_id = key_id + 1
    new_key_num = cache[key_id]['key_num'] + 1
    return await create_new_key(new_key_id, new_key_num)
  print(f"Using same day key: {cache[key_id]['key_name']}")
  return cache[key_id]['key_name']

async def create_new_key(new_key_id: int, new_key_num: int) -> str:
  global cache
  if new_key_num > NUMBER_OF_API_KEYS:
    raise Exception("Max number of Google API keys reached")
  
  cache[new_key_id] = {
    'key_num': new_key_num,
    'key_name': f'google_api_key_{new_key_num}',
    'call_count': 0,
    'date': date.today()
  }
  print(f"Created new key: {cache[new_key_id]['key_name']}")
  return cache[new_key_id]['key_name']
  

async def update_cache():
  global cache
  global cache_call_count

  latest_key_id = max(cache.keys())
  cache[latest_key_id]['call_count'] += 1
  cache_call_count += 1
  print(f"Updated cache after call: {cache[latest_key_id]['key_name']}, call count: {cache[latest_key_id]['call_count']}")


async def fetch_google_results(search_query: str, search_site: str, search_range_days: Optional[int], max_results: int) -> List[Dict[str, str]]:
  if search_range_days:
    date_restriction = f'd{search_range_days}'
  else:
    date_restriction = ""
  
  results_fetched = 0
  start_index = 1
  all_items = []

  async with aiohttp.ClientSession() as session:
    while results_fetched < max_results:
      try:
        api_key_name = await get_cached_api_key()
        api_key = os.environ[api_key_name]
        
        # Construct API call URL with parameters
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
      except Exception as e:
        print(f"Error fetching results: {e}")
        break

  return all_items[:max_results]


async def upsert_api_tracker_db():
  global cache
  # Update api tracker db with latest cache data, then reset cache
  data_to_upsert = [
    {
      'id': key,
      'key_name': value['key_name'],
      'call_count': value['call_count'],
      'date': value['date'].isoformat()
    }
    for key, value in cache.items()
  ]
  await db_upsert_api_tracker_data(data_to_upsert)
  cache = {}


# For testing purposes
if __name__ == "__main__":
  search_queries = ["razer naga", "razer viper", "razer deathadder", "razer krait", "razer iskur"]
  search_site = "amazon.com"
  search_range_days = None
  max_results = 10

  for search_query in search_queries:
    results = asyncio.run(fetch_google_results(search_query, search_site, search_range_days, max_results))
    for result in results:
      print(result['title'])
    print("\n")
    
  asyncio.run(upsert_api_tracker_db())
  