from updater.utils.amzn_handler import extract_asin_from_url
from updater.utils.google_handler import fetch_google_results
from updater.pipeline.furnish_pd_info import match_pd_info_from_google
import asyncio
import json

async def main():
  google_results = await fetch_google_results("ASUS ZenScreen Go MB16AP", "amazon.com", None, 10)
  pd_info_str_extracted = "ASUS ZenScreen Go MB16AP"
  
  matched_result = await match_pd_info_from_google(google_results, pd_info_str_extracted)
  print(json.dumps(matched_result, indent=2))

if __name__ == "__main__":
  asyncio.run(main())