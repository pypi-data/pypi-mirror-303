import os
import re
import time
import requests
import random

from dotenv import load_dotenv
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.condition import Condition
from paapi5_python_sdk.models.get_items_request import GetItemsRequest
from paapi5_python_sdk.models.get_items_resource import GetItemsResource
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
from paapi5_python_sdk.models.item import Item
from paapi5_python_sdk.models.get_variations_request import GetVariationsRequest
from paapi5_python_sdk.models.get_variations_resource import GetVariationsResource
from paapi5_python_sdk.models.get_variations_response import GetVariationsResponse
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException

from typing import Optional
import asyncio
from asyncio import Semaphore
from functools import partial


load_dotenv()

# Define API credentials
access_key = os.environ['amazon_access_key']
secret_key = os.environ['amazon_secret']
partner_tag = 'redditrecs-g-20'

# PAAPI host and region to which you want to send request
# Details: https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region
host = "webservices.amazon.com"
region = "us-east-1"

# API declaration
default_api = DefaultApi(access_key=access_key,
                         secret_key=secret_key,
                         host=host,
                         region=region)

# Define resources needed
items_resource = [
  GetItemsResource.ITEMINFO_TITLE, 
  GetItemsResource.ITEMINFO_BYLINEINFO,
  GetItemsResource.ITEMINFO_TECHNICALINFO,
  GetItemsResource.ITEMINFO_PRODUCTINFO,
  GetItemsResource.ITEMINFO_CONTENTINFO,
  GetItemsResource.ITEMINFO_FEATURES,
  GetItemsResource.OFFERS_LISTINGS_PRICE,
  GetItemsResource.IMAGES_PRIMARY_LARGE,
  GetItemsResource.PARENTASIN
]

get_variations_resources = [
  GetVariationsResource.ITEMINFO_BYLINEINFO,
  GetVariationsResource.ITEMINFO_TITLE,
  GetVariationsResource.ITEMINFO_PRODUCTINFO,
  GetVariationsResource.OFFERS_LISTINGS_PRICE,
  GetVariationsResource.IMAGES_PRIMARY_LARGE,
  GetVariationsResource.PARENTASIN,
  GetVariationsResource.VARIATIONSUMMARY_VARIATIONDIMENSION
]

languages_of_preference = ["en_US"]

# Global semaphore to limit concurrent requests
request_semaphore = Semaphore(1)  # Allows 1 request per api_delay seconds
api_delay = 0.55



# URL (str) -> Is Amazon link (boolean)
def is_amazon_url(url):
  amazon_regex = re.compile(
      r'http[s]?://(?:www\.)?(amazon\.(?:com|co\.[a-z]+|de|fr|ca|jp|cn|in|br|mx|au|sg|ae|tr|nl|es|it)|amzn\.to|a\.co)/'
  )
  return bool(amazon_regex.search(url))



async def retry_with_exponential_backoff(func, max_retries=3, base_delay=1):
  for attempt in range(max_retries):
    try:
      return await func()
    except ApiException as exception:
      if exception.status == 429 and attempt < max_retries - 1:
        delay = (2 ** attempt * base_delay) + (random.random() * 0.1)
        print(f"Rate limited. Retrying in {delay:.2f} seconds...")
        await asyncio.sleep(delay)
      else:
        raise



async def get_items_data_from_asins(asins: list[str]) -> Optional[list[Item]]:
  try:
    get_items_request = GetItemsRequest(
      partner_tag=partner_tag,
      partner_type=PartnerType.ASSOCIATES,
      marketplace="www.amazon.com",
      condition=Condition.NEW,
      item_ids=asins,
      resources=items_resource,
    )
  except ValueError as exception:
    print("Error in forming GetItemsRequest: ", exception)
    return

  print(f"Amazon PAAPI: Sending request for {asins}")
  try:
    async with request_semaphore:
      get_items_func = partial(default_api.get_items, get_items_request)
      response = await retry_with_exponential_backoff(
        lambda: asyncio.get_event_loop().run_in_executor(None, get_items_func)
      )
      await asyncio.sleep(api_delay)
    return response.items_result.items
  except ApiException as exception:
    print("Error calling PA-API 5.0!")
    print("Status code:", exception.status)
    print("Errors :", exception.body)
    print("Request ID:", exception.headers["x-amzn-RequestId"])
  except (TypeError, ValueError, Exception) as exception:
    print(f"{type(exception).__name__} :", exception)




# Extracts item ID (ASIN) given an Amazon URL, even if shortened
def extract_asin_from_url(url):
    
  # If URL is shortened, get full URL
    if url.startswith("https://a.co"):
      try:
        response = requests.get(url, timeout=10)
        url = response.url
        print(f"Full URL: {url}")
      except requests.RequestException as e:
        print(f"Error following shortened URL: {e}")
        return None

    patterns = [
      r'/dp/([A-Z0-9]{10})', r'/gp/product/([A-Z0-9]{10})',
      r'/gp/aw/d/([A-Z0-9]{10})', r'/gp/offer-listing/([A-Z0-9]{10})',
      r'/product-reviews/([A-Z0-9]{10})'
    ]

    for pattern in patterns:
      match = re.search(pattern, url)
      if match:
        return match.group(1)
    # If no patterns matched
    return None




async def search_pd_amzn(search_term: str, max_results: int) -> Optional[list]:
  search_index = "All"  # Category for search

  try: # Forming request
    search_items_request = SearchItemsRequest(
      partner_tag=partner_tag,
      partner_type=PartnerType.ASSOCIATES,
      keywords=search_term,
      search_index=search_index,
      item_count=max_results,
      resources=items_resource,
    )
  except ValueError as exception:
    print("Error in forming SearchItemsRequest: ", exception)
    return None

  try: # Sending request
    async with request_semaphore:
      # Use partial to create a callable that doesn't require arguments
      search_items_func = partial(default_api.search_items, search_items_request)
      # Run the API call in a thread pool
      response = await retry_with_exponential_backoff(
        lambda: asyncio.get_event_loop().run_in_executor(None, search_items_func)
      )
      # Wait without blocking the event loop
      await asyncio.sleep(api_delay)

    if response and response.search_result and response.search_result.items:
      return response.search_result.items
    else:
      print("Amzn pd search: No results")
      return None

  except ApiException as exception:
    print("Error calling PA-API 5.0!")
    print("Status code:", exception.status)
    print("Errors :", exception.body)
    print("Request ID:", exception.headers["x-amzn-RequestId"])
  except TypeError as exception:
    print("TypeError :", exception)
  except ValueError as exception:
    print("ValueError :", exception)
  except Exception as exception:
    print("Exception :", exception)
  
  return None


async def get_amzn_variations(asin: str):
  try:
    get_variations_request = GetVariationsRequest(
      partner_tag=partner_tag,
      partner_type=PartnerType.ASSOCIATES,
      marketplace="www.amazon.com",
      languages_of_preference=languages_of_preference,
      asin=asin,
      resources=get_variations_resources,
    )
  except ValueError as exception:
    print("Error in forming GetVariationsRequest: ", exception)
    return
  
  try:
    async with request_semaphore:
      get_variations_func = partial(default_api.get_variations, get_variations_request)
      response = await retry_with_exponential_backoff(
        lambda: asyncio.get_event_loop().run_in_executor(None, get_variations_func)
      )
      await asyncio.sleep(api_delay)
    
    return response.variations_result
  
  except ApiException as exception:
    print("Error calling PA-API 5.0!")
    print("Status code:", exception.status)
    print("Errors :", exception.body)
    print("Request ID:", exception.headers["x-amzn-RequestId"])
  except (TypeError, ValueError, Exception) as exception:
    print(f"{type(exception).__name__} :", exception)
  except Exception as exception:
    print("Exception :", exception)
  



if __name__ == "__main__":
  asin = "B0936FGLQS"
  parent_asin = asyncio.run(get_items_data_from_asins([asin]))[0].parent_asin
  print(parent_asin)
  # variations_result = asyncio.run(get_amzn_variations(parent_asin))
  # print(variations_result)
  