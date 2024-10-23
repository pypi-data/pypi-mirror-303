import copy
import json
import asyncio
from collections import defaultdict
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from pathlib import Path

from updater.utils.ai_handler import get_openai_response_struct, get_openai_response

from updater.utils.reddit_handler import get_subm_from_subm_id, load_all_subm_comments
from updater.pipeline.prep_subm_for_llm import prep_subm_for_llm

# Given subm data, split into blocks, then return a list of opinions
async def identify_opns(prepped_for_llm_subm_data: dict, pd_category: str) -> list[dict]:
  blocks = split_replies(prepped_for_llm_subm_data)
  block_count = len(blocks)
  print(f'\nSubmission split into {block_count} block(s)')
  
  tasks = [asyncio.create_task(process_block(block, i, block_count, pd_category)) for i, block in enumerate(blocks)]
  results = await asyncio.gather(*tasks)
  # Unpack results from list of lists to a single list of dicts, filtering out None values
  flat_extracted_opns = [opn for extracted_opns in results if extracted_opns is not None for opn in extracted_opns]
  
  # SKIP DEDUPING FOR NOW UNTIL ITS FIXED
  # uniq_opns_list = await dedup_identified_opns(flat_extracted_opns) if flat_extracted_opns else []

  return flat_extracted_opns


# Given subm data, split along replies into blocks, return list of blocks
def split_replies(data: dict, max_chars: int=5000) -> list[dict]:
  base_data = {key: value for key, value in data.items() if key != 'replies'} # Create a base data dict without replies
  
  blocks = []
  current_block = copy.deepcopy(base_data) # Start a block with the base data
  current_block['replies'] = []
  current_size = len(json.dumps(current_block, indent=2, ensure_ascii=False))

  # For each first level reply...
  for reply in data['replies']:
    reply_size = len(json.dumps(reply, indent=2, ensure_ascii=False))

    if current_size + reply_size > max_chars and len(current_block['replies']) == 0: # Sepcial check - If adding first reply already exceeds max_chars on its own
      current_block['replies'].append(reply)
      blocks.append(current_block)

      # Start a new block
      current_block = copy.deepcopy(base_data)
      current_block['replies'] = []
      current_size = len(json.dumps(current_block, indent=2, ensure_ascii=False))
      continue
    
    elif current_size + reply_size > max_chars: # If adding current reply will exceed,
      blocks.append(current_block) # add current block to list of blocks, 
      current_block = copy.deepcopy(base_data) # then start a new current block with base data
      current_block['replies'] = []
      current_size = len(json.dumps(current_block, indent=2, ensure_ascii=False)) # reset current size to base size

    current_block['replies'].append(reply) # Add reply to current block
    current_size += reply_size # Update current size

  if current_block['replies']: # Add the last block if it has any replies
    blocks.append(current_block)

  return blocks

# Given a block, return a list of opinions
async def process_block(block: dict, index: int, block_count: int, pd_category: str) -> list[dict]:
  class Sentiment(str, Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"

  class Verbatim(BaseModel):
    positive: Optional[list[str]] = Field(description="Quotes suggesting Redditor's positive sentiment for the product, if applicable")
    neutral: Optional[list[str]] = Field(description="Quotes suggesting Redditor's neutral sentiment for the product, if applicable")
    negative: Optional[list[str]] = Field(description="Quotes suggesting Redditor's negative sentiment for the product, if applicable")

  class OpinionSummary(BaseModel):
    verbatim: Verbatim
    overall_sentiment: Sentiment = Field(description="The Redditor's overall sentiment for the product. Can be positive, neutral, or negative.")

  class Opinion(BaseModel):
    opinion_summary: OpinionSummary
    username: str = Field(description="Username of Redditor with the opinion")
    pd_brand: Optional[str] = Field(description=f"Brand of the {pd_category}")
    pd_model_or_name: Optional[str] = Field(description=f"Model or name of the {pd_category}")
    pd_key_specs: Optional[str] = Field(description="Key specs - technical specs only e.g. Polycarbonate, 41L, QLED etc). Exclude high level descriptions made by the Redditor about the product, such as lightweight, compact, portable, etc.")
    pd_url: Optional[str] = Field(description=f"Url of the {pd_category}. Exclude query parameters (everything after the ?)")

  class Opinions(BaseModel):
    opinions: Optional[list[Opinion]] = Field(description="If there are no valid opinions, let this field be None or null (as in not the str).")
  
  print(f'Identifying opn for block {index + 1} of {block_count}...')
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "identify_opn_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  model = 'gpt-4o-2024-08-06'
  block_json_str = json.dumps(block, indent=2, ensure_ascii=False)
  user_prompt = f'Extract opinions on "{pd_category}" from this Reddit thread from Redditors who have owned them.\n\nReddit thread:\n```\n{block_json_str}\n```'
  response_format = Opinions
  llm_response = await get_openai_response_struct(sys_prompt, user_prompt, model, response_format, 'identify_opns')
  llm_response_dict = llm_response.model_dump(mode='json') if llm_response else None
  opinions_list = llm_response_dict['opinions'] if llm_response_dict else []
  return opinions_list



# Processes the flat_extracted_opns and updates the opinions dictionary
async def dedup_identified_opns(flat_extracted_opns: list[dict]) -> list[dict]:
  opns_grouped_by_username_and_brand = defaultdict(list)
  for opn in flat_extracted_opns:
    username = opn.get('username')
    brand = opn.get('pd_brand')
    user_brand = (username, brand)
    opns_grouped_by_username_and_brand[user_brand].append(opn)

  # Define a function to merge group of opinions if needed
  async def merge_group(user_brand, opns):
    if len(opns) > 1:
      print(f'Merging {len(opns)} opinions for {user_brand}...')
      processed_opns = await check_and_merge_opns(opns)
      print(f'Merged {len(opns)} opinions for {user_brand} into {len(processed_opns)} opinions')
      return processed_opns
    return opns

  # Create tasks for processing each group
  merge_tasks = [
    asyncio.create_task(merge_group(user_brand, opns))
    for user_brand, opns in opns_grouped_by_username_and_brand.items()
  ]

  # Run all tasks concurrently
  merged_groups = await asyncio.gather(*merge_tasks)

  # Flatten the merged groups to a list of opinions
  uniq_opns_list = [opn for group in merged_groups for opn in group]
  
  return uniq_opns_list


# Given a list of opinions, check if they are talking about the same product, and merge them if they are
async def check_and_merge_opns(opns: list[dict]) -> list[dict]:
  # PLACEHOLDER FOR NOW
  merged_opns_list = opns
  return merged_opns_list




if __name__ == '__main__':
  async def main():
    subm_id = '1adcro8'
    subm = await get_subm_from_subm_id(subm_id)
    subm_loaded = await load_all_subm_comments(subm)
    subm_data_for_llm, subm_stats = await prep_subm_for_llm(subm_loaded)
    print(subm_data_for_llm)
    print('\n\n')
    blocks = split_replies(subm_data_for_llm)
    for block in blocks:
      print(block)
      print('*************')

  asyncio.run(main())



  
