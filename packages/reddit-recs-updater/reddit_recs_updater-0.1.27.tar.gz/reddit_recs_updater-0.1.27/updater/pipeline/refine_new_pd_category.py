from updater.utils.google_handler import fetch_google_results
from updater.utils.ai_handler import get_openai_response
import asyncio
from typing import Optional
from pathlib import Path

async def refine_new_pd_category(pd_category: str) -> Optional[str]:
  print(f"Refining pd_category: {pd_category}...")
  search_query = f"Best {pd_category}"
  search_site = "reddit.com"
  search_range_days = 365
  max_results = 10
  
  # Search google with pd_category
  search_results = await fetch_google_results(search_query, search_site, search_range_days, max_results)
  search_results_str = "\n\n".join([f"{result['title']}\n{result['snippet']}" for result in search_results])
  
  # configure prompt
  sys_prompt = "You are a helpful shopping assistant. Respond in JSON format as instructed."
  current_dir = Path(__file__).parent
  user_prompt_path = current_dir.parent / "llm_prompts" / "refine_pd_category_user.txt"
  with open(user_prompt_path, "r") as file:
    user_prompt = file.read()
  
  # Replace placeholders in the user prompt
  user_prompt = user_prompt.replace('{pd_category}', pd_category)
  user_prompt = user_prompt.replace('{search_results}', search_results_str)
  
  # Get response from openai
  model = "gpt-4o-2024-08-06"
  response_format = { "type": "json_object" }
  caller = "refine_new_pd_category"
  response = await get_openai_response(sys_prompt, user_prompt, model, response_format, caller)

  # Return refined pd_category if search results are not mostly relevant, else default to pd_category
  if response:
    if response['search_results_mostly_relevant'] == False:
      refined_pd_category = response['product_category'].capitalize()
      print(f"-> Search results are not mostly relevant. Refining pd_category to {refined_pd_category}")
      return refined_pd_category
    else:
      print(f"-> Search results are mostly relevant. No new pd_category to return")
      return None
  else:
    print("-> No response from LLM. No new pd_category to return")
    return None

if __name__ == "__main__":
  pd_category = "15 inch TVs"
  print(asyncio.run(refine_new_pd_category(pd_category)))

  