import re
import logging
from urllib.parse import urlparse, urlunparse

def clean_url_in_text(text: str) -> str:

  def strip_query(url):
    try:
      parsed_url = urlparse(url)
      stripped_url = urlunparse(parsed_url._replace(query=''))
      return stripped_url
    except Exception as e:
      return url

  # Regex to find URLs
  url_pattern = re.compile(r'https?://[^\s]+')
  
  # Find all URLs in the text
  urls = url_pattern.findall(text)

  for url in urls:
    clean_url = strip_query(url)
    if not isinstance(clean_url, str):
      clean_url = str(clean_url, 'utf-8') if isinstance(clean_url, (bytes, bytearray, memoryview)) else str(clean_url)
    text = text.replace(url, clean_url)
  return text
