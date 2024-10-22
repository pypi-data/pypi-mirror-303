import json
from updater.utils.ai_handler import get_openai_response
from pathlib import Path
# CURRENTLY NOT USED
# FOR NOW WE SIMPLY EXTRACT ALL OPINION DATA DIRECTLY

async def extract_opn_breakdown(opinion_context, username, product_category, pd_info_str, use_cases):
  # Construct paths to prompt files
  current_dir = Path(__file__).parent
  sys_prompt_path = current_dir.parent / "llm_prompts" / "extract_opn_breakdown_sys.txt"
  user_prompt_path = current_dir.parent / "llm_prompts" / "extract_opn_breakdown_user.txt"

  # Load prompts
  with open(sys_prompt_path, 'r') as file:
    sys_prompt = file.read()
  with open(user_prompt_path, 'r') as file:
    user_prompt = file.read()

  # Replace placeholders in user prompt
  user_prompt = user_prompt.replace("{username}", username)
  user_prompt = user_prompt.replace("{product_category}", product_category)
  user_prompt = user_prompt.replace("{product_name}", pd_info_str)
  user_prompt = user_prompt.replace("{use_cases}", json.dumps(use_cases))
  user_prompt = user_prompt.replace("{opinion_context}", json.dumps(opinion_context, indent=2))
  
  # Define other openai parameters
  model = "gpt-4o-2024-08-06"
  response_format = { "type": "json_object" }
  
  # Call openai
  opn_breakdown = await get_openai_response(sys_prompt, user_prompt, model, response_format, 'extract_opn_breakdown')

  # Add username
  opn_breakdown['username'] = username

  return opn_breakdown