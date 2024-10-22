def get_amzn_pd_info(amzn_item):
  pd_info = {
    'asin': amzn_item.asin if amzn_item.asin else None,
    'brand': amzn_item.item_info.by_line_info.brand.display_value if amzn_item.item_info and amzn_item.item_info.by_line_info and amzn_item.item_info.by_line_info.brand else None,
    'title': amzn_item.item_info.title.display_value if amzn_item.item_info and amzn_item.item_info.title else None,
    'url': amzn_item.detail_page_url if amzn_item.detail_page_url else None,
    'price': amzn_item.offers.listings[0].price.amount if amzn_item.offers and amzn_item.offers.listings and amzn_item.offers.listings[0] and amzn_item.offers.listings[0].price else None,
    'img_url': amzn_item.images.primary.large.url if amzn_item.images and amzn_item.images.primary and amzn_item.images.primary.large else None
  }

  return pd_info