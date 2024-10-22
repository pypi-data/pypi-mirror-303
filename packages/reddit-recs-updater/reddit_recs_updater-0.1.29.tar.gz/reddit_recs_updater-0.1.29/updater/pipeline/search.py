import asyncio
import re
from updater.utils.google_handler import fetch_google_results

# List of search terms -> List of dicts of results data
async def search_reddit(search_terms: list[str], max_results: int) -> list[dict]:
  search_site = "reddit.com"
  search_range_days_list = [365, 120, 60]
  search_google_tasks = [
    asyncio.create_task(fetch_google_results(search_term, search_site, search_range_days, max_results))
    for search_term in search_terms
    for search_range_days in search_range_days_list
  ]
  search_google_task_results = await asyncio.gather(*search_google_tasks)
  
  unique_results = {}
  for result_set in search_google_task_results:
    for item in result_set:
      if 'link' in item:
        subm_id = extract_submission_id(item['link'])
        if subm_id:
          unique_results[subm_id] = {
            'title': item['title'],
            'snippet': item['snippet'],
            'link': item['link'],
            'subm_id': subm_id,
            'subreddit': extract_subreddit_name(item['link'])
          }

  return list(unique_results.values())


def extract_submission_id(url):
  # Regular expression to match Reddit submission URLs
  pattern = r'https?://(?:www\.)?reddit\.com/r/\w+/comments/(\w+)/'
  match = re.match(pattern, url)

  if match:
    return match.group(1)
  else:
    return None

def extract_subreddit_name(url):
  # Regular expression to match Reddit submission URLs
  pattern = r'https?://(?:www\.)?reddit\.com/r/(\w+)/'
  match = re.match(pattern, url)

  if match:
    return match.group(1)
  else:
    return None


if __name__ == "__main__":
  search_terms = [
    'best gaming mouse for fps'
  ]
  unique_results_dict = asyncio.run(search_reddit(search_terms, 10))
  print(unique_results_dict)