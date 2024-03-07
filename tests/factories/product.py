import random

from product.product import Product
from faker import Faker  # Assuming you have faker installed


class ProductFactory:
    """
    Factory class for creating product objects with fuzzy data for testing purposes.
    """
    def __init__(self):
        self.faker = Faker()
        self.created_products = []

    def create_product(self):
        """
        Creates a Product object with fuzzy product data using faker library.
        """
        product_name = self.faker.unique.word().upper()
        individual_price = self.faker.pyfloat(positive=True, max_value=100, min_value=1, right_digits=2)

        # Ensure bulk price offers a discount compared to individual price
        bulk_price = {
            2: random.uniform(individual_price * 1.2, individual_price * 1.9),
            3: random.uniform(individual_price * 2.3, individual_price * 2.7)
        }

        product = Product(product_name, individual_price, bulk_price)
        self.created_products.append(product)
        return product
