from updater.utils.url_cleaner import clean_url_in_text
from updater.reddit_blacklist import BLACKLIST
from asyncpraw.models import Submission
import asyncio



# Subm object -> Loaded Subm (dict), stats (dict)
async def prep_subm_for_llm(subm: Submission) -> tuple[dict, dict]:
  print(f"\nPrepping submission: {subm.permalink}")
  subm_data = await expand_subm_data_for_llm(subm)

  total_words = count_total_words(subm_data)
  total_comments = count_total_comments(subm_data['replies'])
  stats = {'total_subm': 1, 'total_comments': total_comments, 'total_words': total_words}

  return subm_data, stats


# Subm object -> Subm data (dict)
async def expand_subm_data_for_llm(subm: Submission) -> dict:
  subreddit = subm.subreddit
  subm_data = {
    'subreddit_name': subreddit.display_name,
    'subreddit_title': subreddit.title,
    'subreddit_description': subreddit.public_description,
    'submission_author': subm.author.name if subm.author else '[deleted]',
    'submission_title': subm.title,
    'submission_text': clean_url_in_text(subm.selftext),
    'replies': await expand_comments_for_llm(subm)
  }
  return subm_data

# Subm object -> Comments nested (list)
async def expand_comments_for_llm(subm):
  async def process_comment(comment):
    return {
      'author': comment.author.name if comment.author else '[deleted]',
      'text': clean_url_in_text(comment.body) if (comment.author and comment.author.name not in BLACKLIST) else '[removed - author blacklisted]',
      'replies': [await process_comment(reply) async for reply in comment.replies]
    }
  
  comments = subm.comments
  return [await process_comment(comment) for comment in comments]


# Helped to count total words in subm data
def count_total_words(subm_data):
  total_words = len(subm_data['submission_text'].split())
  
  def count_reply_words(reply):
    reply_words = len(reply['text'].split())
    for sub_reply in reply['replies']:
      reply_words += count_reply_words(sub_reply)
    return reply_words
  
  for reply in subm_data['replies']:
    total_words += count_reply_words(reply)
  
  return total_words

# Helper to count total comments in subm data
def count_total_comments(replies):
  total = len(replies)
  for reply in replies:
    total += count_total_comments(reply['replies'])
  return total



if __name__ == '__main__':
  async def main():
    import json
    from updater.utils.reddit_handler import get_subm_from_subm_id, load_all_subm_comments
    
    subm_id = '16kmd4b'
    subm = await get_subm_from_subm_id(subm_id)
    subm_loaded = await load_all_subm_comments(subm)
    subm_data = await expand_subm_data_for_llm(subm_loaded)
    print(json.dumps(subm_data, indent=2, ensure_ascii=False))
  asyncio.run(main())


# # Subm data (dict) -> Amazon urls (dict), other urls (dict)
# def collect_urls(data):
#   print(f"\nCollecting urls...")
#   amazon_urls = {}
#   other_urls = {}
    
#   def extract_urls(item):
#     if isinstance(item, str):
#       urls = re.findall(r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*[^)\]}])', item)
#       for url in urls:
#         final_url = get_final_url(url)
#         if is_amazon_url(final_url):
#           asin = extract_asin_from_url(final_url)
#           if asin:
#             amazon_urls[url] = {'final_url': final_url, 'asin': asin} # add to amazon urls, with url as key
#         else:
#           other_urls[url] = final_url
#     elif isinstance(item, dict):
#       for value in item.values():
#         extract_urls(value)
#     elif isinstance(item, list):
#       for element in item:
#         extract_urls(element)

#   extract_urls(data)
#   print(f"--> Collected {len(amazon_urls)} amazon urls and {len(other_urls)} other urls")
#   return amazon_urls, other_urls

# # Amazon urls (dict) -> Amzn items (list), Asin-Title dict (dict)
# def process_amazon_urls(amazon_urls):
#   asins = list(set(info['asin'] for info in amazon_urls.values()))
#   amzn_items = get_items_data_from_asins(asins)
#   print(f"--> Received {len(amzn_items)} items data")
#   amzn_items_dict = {item.asin: item.item_info.title.display_value for item in amzn_items}
#   return amzn_items, amzn_items_dict

# # Other urls (dict) -> Other urls (dict) with titles as values
# def process_other_urls(other_urls):
#   print(f"Processing other urls...")
#   for url, final_url in other_urls.items():
#     title = get_website_title(final_url)
#     if title:
#       other_urls[url] = title
#   return other_urls

# # Subm data (dict) -> Subm data (dict) with urls annotated
# def annotate_urls(data, items_dict, amazon_urls, other_urls):
#   def replace_urls(text):
#     for url, info in amazon_urls.items():
#       if info['asin'] in items_dict:
#         pd_title = items_dict[info['asin']]
#         text = text.replace(url, f"{url.split('?')[0]}: ({pd_title})")
#     for url, title in other_urls.items():
#       text = text.replace(url, f"{url.split('?')[0]}: ({title})")
#     return text

#   if isinstance(data, dict):
#     return {k: annotate_urls(v, items_dict, amazon_urls, other_urls) for k, v in data.items()}
#   elif isinstance(data, list):
#     return [annotate_urls(item, items_dict, amazon_urls, other_urls) for item in data]
#   elif isinstance(data, str):
#     return replace_urls(data)
#   else:
#     return data

# # URL (str) -> Final URL (str)
# def get_final_url(url):
#   headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#   }    
#   try:
#     response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
#     response.raise_for_status() 
#     final_url = response.url
#     print(f"--> Final url: {final_url}")
#   except requests.exceptions.RequestException as e:
#     print(f'Error getting final url: {e}')
#     final_url = url
#   return final_url


# # URL (str) -> Website title (str)  
# def get_website_title(url):
#   headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#   }
#   try:
#     print(f"Getting website title for {url}...")
#     response = requests.get(url, headers=headers, timeout=1)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.content, 'html.parser')

#     if soup.title:
#       title = soup.title.string
#     else:
#       title = 'No title found'
#     print(f"--> Website title: {title}")
#     return title
  
#   except requests.exceptions.RequestException as e:
#     print(f'Error getting website title: {e}')
#     return None