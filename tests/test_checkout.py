import unittest
from cart.cart import Cart
from checkout.checkout import Checkout
from tests.factories.product import ProductFactory


class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        product_factory = ProductFactory()
        product_a = product_factory.create_product()
        product_b = product_factory.create_product()
        # Add some items to the cart
        self.cart.add_item(product_a)
        self.cart.add_item(product_b)

    def test_do_checkout(self):
        checkout = Checkout(self.cart)
        result = checkout.do_checkout()

        # Assert that cart_data is returned
        self.assertIn("cart_data", result)
        self.assertIsInstance(result["cart_data"], list)

        # Assert that total_payable_amount (including tax) is returned
        self.assertIn("total_payable_amount (including tax)", result)
        self.assertIsInstance(result["total_payable_amount (including tax)"], float)

    def test_calculate_total_payable(self):
        checkout = Checkout(self.cart)
        total_payable_amount = checkout.get_total_payable_amount()

        # Assert that total_payable_amount is a float
        self.assertIsInstance(total_payable_amount, float)

    def test_tax_payable(self):
        checkout = Checkout(self.cart)
        total_cart_value = 30.0  # Total price of items in the cart
        tax_payable = checkout.tax_payable(total_cart_value)

        # Assert that tax_payable is calculated correctly based on the region
        self.assertIsInstance(tax_payable, float)
        self.assertEqual(tax_payable, 0)
