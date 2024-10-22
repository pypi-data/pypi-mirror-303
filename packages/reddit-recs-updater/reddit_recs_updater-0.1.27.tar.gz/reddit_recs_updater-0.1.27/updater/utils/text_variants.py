from inflect import engine

p = engine()

def generate_singular_plural_variants(category: str) -> list[str]:
  words = category.split()
  
  if len(words) > 1:
    # Handle multi-word phrases
    last_word = words[-1]
    singular_last = p.singular_noun(last_word) or last_word
    plural_last = p.plural(singular_last)
    
    singular = ' '.join(words[:-1] + [singular_last])
    plural = ' '.join(words[:-1] + [plural_last])
  else:
    # Handle single words
    singular = p.singular_noun(category) or category
    plural = p.plural(singular)
  
  return list(set([singular, plural, category]))

if __name__ == "__main__":
  print(generate_singular_plural_variants("cry baby"))
  # output: ['cry babies', 'cry baby']