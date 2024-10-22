import os
import asyncpraw

from asyncprawcore.exceptions import AsyncPrawcoreException
from asyncpraw.models import Submission, Comment

reddit = None

async def get_reddit():
  global reddit
  if reddit is None:
    reddit = await configure_reddit()
  return reddit

async def configure_reddit():
  reddit_id = os.environ['reddit_id']
  reddit_secret = os.environ['reddit_secret']
  return asyncpraw.Reddit(
    client_id=reddit_id,
    client_secret=reddit_secret,
    user_agent='python:RedditReccs:v1.0 (by /u/heyyyjoo)'
  )

# Search term (str) -> Subm objects (list)
async def search_reddit(search_term, max_results, time_range, reddit_search_sort):
  reddit = await get_reddit()
  subreddit_to_search = "all"
  print(f"\nSearching Reddit for '{search_term}', time range: '{time_range}', max results: '{max_results}'...")
  try:
    subreddit = await reddit.subreddit(subreddit_to_search)
    search_results = subreddit.search(
      search_term, 
      limit=max_results, 
      time_filter=time_range,
      sort=reddit_search_sort
    )
    search_results_list = []
    async for submission in search_results:
      try:
        await submission.load()
        search_results_list.append(submission)
      except Exception as e:
        print(f"Error loading submission: {str(e)}")
    print(f"--> Returning {len(search_results_list)} results")
    return search_results_list
  except Exception as e:
    print(f"Error in search_reddit: {str(e)}")
    return []
  
  

# Subm id (str) -> Subm object
async def get_subm_from_subm_id(subm_id: str) -> Submission:
  reddit = await get_reddit()
  try:
    subm = await reddit.submission(id=subm_id)
    return subm
  except AsyncPrawcoreException as e:
    print(f"Error getting subm for {subm_id}: {str(e)}")
    return None


# Subm object -> Subm object with all comments loaded
async def load_all_subm_comments(subm: Submission) -> Submission:
  try: 
    await subm.subreddit.load()
    await subm.comments.replace_more(limit=None)
    return subm
  except AsyncPrawcoreException as e:
    print(f"Error loading all comments for subm {subm.id}: {str(e)}")
    return subm



async def get_comment_from_comment_id(comment_id: str) -> Comment:
  reddit = await get_reddit()
  try:
    comment = await reddit.comment(id=comment_id)
    return comment
  except AsyncPrawcoreException as e:
    print(f"Error getting comment for {comment_id}: {str(e)}")
    return None



