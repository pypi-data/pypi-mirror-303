import json
from updater.utils.ai_handler import get_openai_response
from pathlib import Path

# Product category (str) -> Dict of use cases (dict)
async def gen_use_cases(product_category: str) -> tuple[dict, list[str]]:
  print(f'Generating use cases for {product_category}...')

  model = 'gpt-4o-2024-08-06'
  response_format = { "type": "json_object" }
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "gen_use_cases_sys.txt"
  with open(sys_prompt_path, "r") as file:
    sys_prompt = file.read()
  user_prompt_path = current_dir.parent / "llm_prompts" / "gen_use_cases_user.txt"
  with open(user_prompt_path, "r") as file:
    user_prompt = file.read()
  user_prompt = user_prompt.replace('{product_category}', product_category)
  response = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'gen_use_cases')
  
  use_cases_dict = response['Usage scenarios']
  use_cases_names = list(use_cases_dict.keys())

  print(json.dumps(use_cases_dict, indent=2))
  print(f'--> Use cases generated: {use_cases_names}')
  
  return use_cases_dict, use_cases_names