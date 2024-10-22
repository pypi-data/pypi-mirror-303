import json
import asyncio
from updater.utils.ai_handler import get_openai_response
from asyncpraw.models import Submission
from updater.reddit_blacklist import BLACKLIST
from typing import Optional
from pathlib import Path


# Takes the opns_extracted list, to each opn adds keys 'is_opn' (True/False) and 'is_owner' (True/False/None)
async def perform_checks_on_opns(opns_extracted: list[dict], subm_loaded: Submission, pd_category: str) -> list[dict]:
  perform_checks_on_opn_tasks = [asyncio.create_task(perform_checks_on_opn(opn, subm_loaded, pd_category)) for opn in opns_extracted]
  processed_opns = await asyncio.gather(*perform_checks_on_opn_tasks)
  checked_opns = [opn for opn in processed_opns if opn is not None]

  return checked_opns


# Indivdual check on each opn
async def perform_checks_on_opn(opn: dict, subm_loaded: Submission, pd_category: str) -> dict:
  opn_context = get_opn_context(opn, subm_loaded)

  username = opn['username']
  pd_brand = opn['pd_brand']
  pd_name = opn['pd_model_or_name']
  pd_key_specs = opn['pd_key_specs']
  pd_info = f'{pd_brand} {pd_name}, {pd_key_specs}'
  
  print(f'\nChecking opn validity for: {username}...')
  opn['is_opn'] = await check_if_is_opn(username, opn_context, pd_category, pd_info)
  opn['is_owner'] = await check_if_is_owner(username, opn_context, pd_category, pd_info) if opn['is_opn'] else None
  
  return opn


async def check_if_is_opn(username, opn_context, pd_category, pd_info) -> bool:
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "is_opn_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  sys_prompt = sys_prompt.replace('{username}', username).replace('{pd_category}', pd_category).replace('{pd_info}', pd_info)
  model = 'gpt-4o-mini'
  response_format = { "type": "json_object" }
  user_prompt = json.dumps(opn_context, indent=2, ensure_ascii=False)
  response = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'check_if_is_opn')
  print(f'- Response: {response}')
  if response and response['1'] == 'True':
    return True
  elif response and response['1'] != 'True' and response['2'] == 'True' and response['3'] != 'True':
    return True
  else:
    return False


async def check_if_is_owner(username, opn_context, pd_category, pd_info):
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "is_owner_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  sys_prompt = sys_prompt.replace('{username}', username).replace('{pd_category}', pd_category).replace('{pd_info}', pd_info)
  model = 'gpt-4o-mini'
  response_format = { "type": "json_object" }
  user_prompt = json.dumps(opn_context, indent=2, ensure_ascii=False)
  response = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'check_if_is_owner')
  if response and response['answer'].startswith('1.'):
    return True
  else:
    return False



# ppn (dict), subm_loaded (praw.models.Submission) -> opn_context (dict) i.e. submission + reply tree associated with username from opn
def get_opn_context(opn, subm_loaded):
  username = opn['username']
  replies_tree = []
  for reply in subm_loaded.comments:
    (keep_replies_tree, replies) = recur_get_replies(False, reply, username)
    if keep_replies_tree:
      replies_tree.append(replies)
  opn_context = {
    'subreddit_name': subm_loaded.subreddit.display_name,
    'subreddit_title': subm_loaded.subreddit.title,
    'subreddit_description': subm_loaded.subreddit.public_description,
    'submission_title': subm_loaded.title,
    'submission_author': subm_loaded.author.name if subm_loaded.author else '[deleted]',
    'submission_text': subm_loaded.selftext,
    'replies': replies_tree
  }

  return opn_context


# Recursively get replies, only keep chains of replies associated with the username
# keep_this (bool), comment (praw.models.Comment), username (str) -> keep_this (bool), replies (dict)
def recur_get_replies(keep_this, comment, username):
  replies_current = []
  keep_this = False
  for reply in comment.replies:
    (keep_replies, replies) = recur_get_replies(False, reply, username)
    if keep_replies:
      replies_current.append(replies)
    if keep_this is False and keep_replies is True:
      keep_this = True

  data = {
    'author': comment.author.name if comment.author else '[deleted]',
    'text': comment.body if (comment.author and comment.author.name not in BLACKLIST) else '[removed - author blacklisted]',
    'replies': replies_current
  }

  if str(comment.author) == username or keep_this:
    keep_this = True

  return (keep_this, data)


if __name__ == "__main__":
  import asyncio
  username = 'u/The_Dude_123'
  opn_context = {
    'subreddit_name': 'buildapc',
    'subreddit_title': 'Build a PC',
    'subreddit_description': 'For all your PC building needs!',
    'submission_title': 'I need a new gaming monitor',
    'submission_author': 'u/The_Dude_123',
    'submission_text': 'I\'m looking for a monitor that\'s good for gaming. I\'ve heard good things about the ASUS ROG Swift PG27AQ. What do you think?',
    'replies': []
  }
  pd_category = 'gaming monitor'
  pd_info = 'ASUS ROG Swift PG27AQ'
  print(asyncio.run(check_if_is_owner(username, opn_context, pd_category, pd_info)))