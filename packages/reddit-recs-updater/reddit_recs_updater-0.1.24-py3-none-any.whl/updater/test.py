from updater.utils.reddit_handler import search_reddit

def print_hello():
  print('Hello, world!')
  
async def test_search_reddit():
  print('Testing search_reddit...')
  search_term = 'python'
  max_results = 10
  time_range = 'all'
  reddit_search_sort = 'relevance'
  results = await search_reddit(search_term, max_results, time_range, reddit_search_sort)
  print(results)