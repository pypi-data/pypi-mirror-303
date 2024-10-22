from supabase import create_client, Client
from typing import Optional
from datetime import datetime, timezone
import time
import os

supabase_url = os.environ['supabase_url']
supabase_key = os.environ['supabase_service_key']
supabase: Client = create_client(supabase_url, supabase_key)


######## Used in: main.py

# Get all pd_categories from db
async def db_get_all_pd_categories() -> list[dict]:
  pd_categories_result = supabase.table("pd_categories").select("*").eq("active", True).execute()
  return pd_categories_result.data

# Check if pd category exists in Supabase (incl variants), returns None if no, otherwise returns row data as dict
async def db_get_pd_category(pd_category: str) -> Optional[dict]:
  pd_category_rows = supabase.table("pd_categories").select("*").filter("variants", "cs", f'"{pd_category}"').execute()
  if pd_category_rows.data:
    return pd_category_rows.data[0]
  else:
    return None

# Get subm ids of subms that have been processed for a pd category
async def db_get_processed_subms_ids(pd_category_dict: dict) -> list[str]:
  subms_processed_entries = supabase.table("subms_processed").select("subm_id").eq("pd_category_id", pd_category_dict['id']).execute()
  return [subm['subm_id'] for subm in subms_processed_entries.data]

# Insert new opns into opns table
async def db_insert_opns(opns_data: dict) -> dict:
  opns_result = supabase.table("opns").insert(opns_data).execute()
  return opns_result.data[0]

# Insert new subms_processed into subms_processed table
async def db_insert_subms_processed(subms_processed_data: dict) -> dict:
  subms_processed_result = supabase.table("subms_processed").insert(subms_processed_data).execute()
  return subms_processed_result.data[0]

# Update last_processed for pd_category
async def db_update_last_processed(pd_category_id: int) -> None:
  last_processed = datetime.fromtimestamp(time.time(), tz=timezone.utc).isoformat()
  supabase.table("pd_categories").update({"last_processed": last_processed}).eq("id", pd_category_id).execute()






######## Used in: furnish_pd_info.py

# Get pd by ASIN
async def db_get_pd_by_asin(asin: str) -> Optional[dict]:
  result = supabase.table("products") \
    .select("*") \
    .eq("asin", asin) \
    .execute()
  return result.data[0] if result.data else None

# Get product_brand by pd_id and pd_category_id
async def db_get_product_brand_by_pd_and_category(pd_id: int, pd_category_id: int) -> Optional[dict]:
  result = supabase.table("product_brands") \
    .select("*, brands!inner(*)") \
    .eq("product_id", pd_id) \
    .eq("brands.pd_category_id", pd_category_id) \
    .execute()
  return result.data[0] if result.data else None

# Get brand from product_brands table by pd_id
async def db_get_brand_by_pd_id(pd_id: int) -> Optional[dict]:
  result = supabase.table("product_brands") \
    .select("brands!inner(*)") \
    .eq("product_id", pd_id) \
    .execute()
  return result.data[0]['brands'] if result.data else None


# Add brand to brands table if not already exists, returns the brand row of the brand that was added or already exists
async def db_add_brand_if_new(brand_name: str, pd_category_id: int) -> dict:
 
  # Check if brand exists in brands table
  print(f"Checking if brand {brand_name} exists in brands table")
  brand_result = supabase.table("brands") \
    .select("id") \
    .filter("name_variants", "cs", f'"{brand_name}"') \
    .eq("pd_category_id", pd_category_id) \
    .execute()
 
  # If brand exists, return brand
  if brand_result.data:
    brand = brand_result.data[0]
    return brand
  # else, add brand to brands table and return brand
  else:
    brand_data = {
      'name_full': brand_name,
      'name_variants': [brand_name],
      'pd_category_id': pd_category_id,
      'amzn_url': f'https://www.amazon.com/s?k={brand_name}&language=en_US&linkCode=ll2&linkId=bc302cef206410423351216a444a7e86&tag=redditrecs-g-20&ref=as_li_ss_tl'
    }
    brand_result = supabase.table("brands").insert(brand_data).execute()
    brand = brand_result.data[0]
    return brand

# Add product_brand to product_brands table
async def db_add_product_brand(product_id: Optional[int], brand_id: int) -> dict:
  product_brand_data = {
    'product_id': product_id,
    'brand_id': brand_id
  }
  product_brand_result = supabase.table("product_brands").insert(product_brand_data).execute()
  return product_brand_result.data[0]


# Add pd to products table with pd_info from furnish_pd_info.py
async def db_add_pd(pd_data: dict):
  pd_result = supabase.table("products").insert(pd_data).execute()
  pd = pd_result.data[0]
  return pd

# Get parent_asin from parent_asins table
async def db_get_parent_asin(parent_asin: str):
  result = supabase.table("parent_asins").select("*").eq("parent_asin", parent_asin).execute()
  return result.data

# Get product by parent_asin
async def db_get_product_by_parent_asin(parent_asin: str):
  result = supabase.table("products").select("*").eq("parent_asin", parent_asin).execute()
  return result.data





######## Used in: google_handler.py

async def db_get_api_tracker_data(key_name: str, date: str) -> Optional[dict]:
  tracker_data = supabase.table("api_call_tracker").select("*").eq("key_name", key_name).eq("date", date).execute()
  return tracker_data.data[0] if tracker_data.data else None

async def db_get_latest_tracker_row() -> Optional[dict]:
  tracker_data = supabase.table("api_call_tracker").select("*").order("created_at", desc=True).limit(1).execute()
  return tracker_data.data[0] if tracker_data.data else None

async def db_update_api_tracker_data(key_name: str, call_count: int, date: str):
  result = supabase.table("api_call_tracker").update({"call_count": call_count}).eq("key_name", key_name).eq("date", date).execute()
  if result.data:
    print(f"{key_name} call count updated to {call_count}")
  else:
    print(f"Failed to update {key_name} call count to {call_count}")

async def db_add_api_tracker_data(key_name: str, call_count: int, date: str):
  data = {"key_name": key_name, "call_count": call_count, "date": date}
  result = supabase.table("api_call_tracker").insert(data).execute()
  if result.data:
    print(f"Successfully added API call tracker for {key_name}")
  else:
    print(f"Failed to add API call tracker for {key_name}")

async def db_upsert_api_tracker_data(data_to_upsert: list[dict]):
  result = supabase.table("api_call_tracker").upsert(data_to_upsert).execute()
  if result.data:
    print(f"Successfully upserted API call tracker data:\n{result.data}")
  else:
    print(f"Failed to upsert API call tracker data:\n{result.data}")



######## Used in: process_parent_asin.py

# Add product_parent to product_parents table
async def db_add_product_parent(product_parent_data: dict) -> dict:
  product_parent_result = supabase.table("product_parents").insert(product_parent_data).execute()
  return product_parent_result.data[0]

# Get products by list ofASINs
async def db_get_pds_by_asins(asins: list[str]) -> list[dict]:
  products_result = supabase.table("products").select("*").in_("asin", asins).execute()
  return products_result.data

# Set product_parent_id for products
async def db_set_product_parent_id(product_parent_id: int, products_ids: list[int]):
  result = supabase.table("products").update({"product_parent_id": product_parent_id}).in_("id", products_ids).execute()
  return result.data
  
# Add parent_asin to parent_asins table
async def db_add_parent_asin(parent_asin: str):
  data = {"parent_asin": parent_asin}
  result = supabase.table("parent_asins").insert(data).execute()
  if result.data:
    print(f"Successfully added parent asin: {parent_asin}")
  else:
    print(f"Failed to add parent asin: {parent_asin}")


if __name__ == "__main__":
  import asyncio
  pd_id = 1086
  pd_category_id = 31
  asin = "B0B15Q3HCQ"
  print(asyncio.run(db_get_product_brand_by_pd_and_category(pd_id, pd_category_id)))