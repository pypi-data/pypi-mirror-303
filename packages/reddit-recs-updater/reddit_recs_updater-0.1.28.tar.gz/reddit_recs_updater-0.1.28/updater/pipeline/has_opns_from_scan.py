# Given a subm, check if it has opinions. If yes, return subm data. Else, return none.
import json
from updater.utils.ai_handler import get_openai_response_struct
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
import asyncio

async def scan_if_has_opns(subm_data: dict, pd_category_name: str) -> bool:
  print('- Checking if submission has opinions')
  
  class Inference(BaseModel):
    verbatim: Optional[str]
    product_brand: Optional[str]
    product_model_or_name: Optional[str]
    product_series: Optional[str]
    product_url: Optional[str]
    valid_rec_or_antirec: Optional[bool]
  
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "has_opn_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  max_tokens_reddit = 3000
  reddit_thread_str = json.dumps(subm_data, indent=2)[:max_tokens_reddit * 4]
  user_prompt = f"I am shopping for a {pd_category_name}. Help me analyze this Reddit thread and determine if it has any recommendations or anti-recommendations for any brand, model or series for a {pd_category_name}.\n\n'Reddit Thread:'\n{reddit_thread_str}"
  model = "gpt-4o-mini"
  response_format = Inference

  response = await get_openai_response_struct(sys_prompt, user_prompt, model, response_format, 'has_opns')

  if response:
    verbatim = response.verbatim
    has_opn_raw = response.valid_rec_or_antirec
    has_pd_raw = response.product_brand or response.product_model_or_name or response.product_series or response.product_url
    has_opn = True if (has_opn_raw and has_pd_raw) else False

    print(f'- 1 Opinion extracted: {verbatim}')
    print(f'- 1 Product extracted: {has_pd_raw}')
    print(f'- LLM inference of validity: {has_opn_raw}')
    print(f'--> Has opinion?: {has_opn}')
    return has_opn
  else:
    return False
  
if __name__ == "__main__":
  subm_data = {
    "title": "I need a new gaming monitor",
    "selftext": "I'm looking for a monitor that's good for gaming. I've heard good things about the ASUS ROG Swift PG27AQ. What do you think?",
    "author": "JohnDoe",
    "created_utc": 1672531200,
    "url": "https://www.reddit.com/r/buildapc/comments/1234567890abcdef"
  }
  pd_category_name = "gaming monitor"
  has_opn = asyncio.run(scan_if_has_opns(subm_data, pd_category_name))
  print(f'Has opinion?: {has_opn}')

  
  