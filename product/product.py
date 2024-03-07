class Product:
    def __init__(self, product_name, individual_price, bulk_price=None):
        self.name = product_name
        self.individual_price = individual_price
        # This is added to track the bulk price of an item
        self.bulk_price = bulk_price or {}
