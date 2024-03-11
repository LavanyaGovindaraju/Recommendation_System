def get_item_price(data, item):
    item_prices = dict(zip(data['StockCode'], data['TotalPrice']))
    return item_prices.get(item, 0.0)  # Return 0.0 if item price is not found