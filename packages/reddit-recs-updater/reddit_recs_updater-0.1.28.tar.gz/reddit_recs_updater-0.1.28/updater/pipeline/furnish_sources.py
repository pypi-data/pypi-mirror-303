import re
from datetime import datetime, timezone

# Furnish sources for opns
def furnish_sources(checked_opns_w_pd_info: list[dict], subm_loaded) -> list[dict]:
  for opn in checked_opns_w_pd_info:
    opn['sources'] = get_sources(opn, subm_loaded)
    if opn['sources']:
      opn['latest_source_date'] = max([source['date'] for source in opn['sources'].values()])
    else:
      opn['latest_source_date'] = None
  
  return checked_opns_w_pd_info


def get_sources(opn, subm_loaded):
  verbatims = set()

  subreddit = subm_loaded.subreddit.display_name
  
  # Extract verbatims from opinion_summary
  for sentiment in ['positive', 'neutral', 'negative']:
    sentiment_verbatims = opn['opinion_summary']['verbatim'].get(sentiment)
    if sentiment_verbatims:
      verbatims.update(sentiment_verbatims)
  
  # Clean verbatims
  cleaned_verbatims = {clean_text(verbatim) for verbatim in verbatims}
  
  sources = {}
  
  # Check submission text
  if subm_loaded.author and subm_loaded.author.name == opn['username']:
    cleaned_selftext = clean_text(subm_loaded.selftext)
    if any(cleaned_verbatim in cleaned_selftext for cleaned_verbatim in cleaned_verbatims):
      sources[subm_loaded.id] = {
        'type': 'submission',
        'text': subm_loaded.selftext,
        'permalink': f"https://www.reddit.com{subm_loaded.permalink}",
        'subreddit': subreddit,
        'subm_title': subm_loaded.title,
        'date': datetime.fromtimestamp(subm_loaded.created_utc, tz=timezone.utc).isoformat(),
        'subm_permalink': f"https://www.reddit.com{subm_loaded.permalink}"
      }
  
  # Check comments
  for comment in subm_loaded.comments.list():
    if comment.author and comment.author.name == opn['username']:
      cleaned_comment_body = clean_text(comment.body)
      if any(cleaned_verbatim in cleaned_comment_body for cleaned_verbatim in cleaned_verbatims):
        sources[comment.id] = {
          'type': 'comment',
          'text': comment.body,
          'permalink': f"https://www.reddit.com{comment.permalink}",
          'subreddit': subreddit,
          'subm_title': subm_loaded.title,
          'date': datetime.fromtimestamp(comment.created_utc, tz=timezone.utc).isoformat(),
          'subm_permalink': f"https://www.reddit.com{subm_loaded.permalink}"
        }
  
  return sources


def clean_text(text):
  
  # Remove markdown links entirely
  text = re.sub(r'\[([^\]]+)\](?:\((?:https?://[^\s)]+|/[^\s)]+)\))', r'\1', text)
  
  # Remove all non-alphanumeric characters and convert to lowercase
  text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
  return text

if __name__ == "__main__":
  text_to_clean = "[Get this one](https://www.reddit.com/r/MechanicalKeyboards/comments/1831q00/comment/k3q111o/?utm_source=share&utm_medium=web3x&utm_name=Web3X&utm_term=1&utm_content=share_button) -Mechanical -under $50 -good warranty -small form factor -Red LEDS -not too loud -good key size"
  print(clean_text(text_to_clean))