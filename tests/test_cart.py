import unittest

from cart.cart import Cart
from tests.factories.product import ProductFactory


class CartTest(unittest.TestCase):

    def setUp(self):
        self.product_factory = ProductFactory()
        self.cart = Cart()

    def test_add_item(self):
        """Tests adding a single item to the cart."""
        # setup params
        product = self.product_factory.create_product()

        # actions
        self.cart.add_item(product)

        # assertions
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].product, product)
        self.assertEqual(self.cart.items[0].quantity, 1)

    def test_add_multiple_items(self):
        """Tests adding multiple items of the same type."""
        product = self.product_factory.create_product()

        self.cart.add_item(product)
        self.cart.add_item(product)
        self.cart.add_item(product)

        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].product, product)
        self.assertEqual(self.cart.items[0].quantity, 3)

    def test_add_different_items(self):
        """Tests adding items of different types."""
        product_a = self.product_factory.create_product()
        product_b = self.product_factory.create_product()

        self.cart.add_item(product_a)
        self.cart.add_item(product_b)

        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.items[0].product, product_a)
        self.assertEqual(self.cart.items[0].quantity, 1)
        self.assertEqual(self.cart.items[1].product, product_b)
        self.assertEqual(self.cart.items[1].quantity, 1)

    def test_remove_item_existing(self):
        """Tests removing an existing item from the cart."""
        product = self.product_factory.create_product()
        self.cart.add_item(product, quantity=2)

        self.cart.remove_item(product)

        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].quantity, 1)

    def test_remove_item_partial(self):
        """Tests removing a partial quantity of an existing item."""
        product = self.product_factory.create_product()
        self.cart.add_item(product, quantity=2)

        self.cart.remove_item(product)

        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].quantity, 1)

    def test_remove_item_all(self):
        """Tests removing all of an existing item."""
        product = self.product_factory.create_product()
        self.cart.add_item(product, quantity=2)

        self.cart.remove_item(product, quantity=2)

        self.assertEqual(len(self.cart.items), 0)

    def test_get_cart_items_data_empty(self):
        """Tests get_cart_items_data for an empty cart."""
        data = self.cart.get_cart_items_data()
        self.assertEqual(data, [])
