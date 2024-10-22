from updater.utils.google_handler import fetch_google_results
from updater.utils.ai_handler import get_openai_response
from pathlib import Path

async def get_pd_brand(url):
  # Search Google using the URL
  search_results = await fetch_google_results(url, "", None, 3)

  # Prepare the search results for LLM input
  search_content = "\n\n".join([f"{i+1}. Title: {item['title']}\nSnippet: {item['snippet']}" for i, item in enumerate(search_results)])
  print(search_content)

  # Prepare prompts for Groq
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "get_pd_brand.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  user_prompt = f"Product URL: {url}\n\nTop search results for searching the product URL:\n{search_content}"

  # Use Groq to extract the brand
  response = await get_openai_response(sys_prompt, user_prompt, "gpt-4o-mini", { "type": "json_object" }, 'get_pd_brand')

  # Extract and return the brand
  brand = response.get("brand", None) if response else None
  return brand