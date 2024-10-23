import json
from updater.utils.ai_handler import get_openai_response
from pathlib import Path

async def gen_use_cases_from_subreddit(submission, product_category, use_cases) -> list[str]:
  
  # Get subreddit info from submission
  subreddit = submission.subreddit
  subreddit_name = subreddit.display_name
  subreddit_description = subreddit.public_description

  # Ask LLM to generate use cases
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "gen_use_cases_subreddit_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  user_prompt = f"Product: {product_category}\nSubreddit name: {subreddit_name}\nSubreddit description: {subreddit_description}\nPossible use cases: {use_cases}"
  model = 'gpt-4o-2024-08-06'
  response_format = { "type": "json_object" }

  openai_response = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'gen_use_cases_from_subreddit')

  return openai_response['use_cases']