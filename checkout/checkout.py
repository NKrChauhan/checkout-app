from cart.cart import Cart
from checkout.constants import REGION
from checkout.factories.regional_tax_rule_factory import RegionalTaxRuleFactory


class Checkout:
    """
    Manages the checkout process and calculating the total price.
    """

    def __init__(self, cart: Cart, region=REGION.INDIA):
        self.cart = cart
        self.region = region

    def do_checkout(self):
        cart_data = self.cart.get_cart_items_data()
        return {
            "cart_data": cart_data,
            "total_payable_amount (including tax)": self.calculate_total_payable()
        }

    def calculate_total_payable(self) -> float:
        """
        Calculates the total price of all items in the cart using the Cart object.
        """
        total_cart_value = self.cart.get_total_price()
        tax_payable_on_cart_items = self.tax_payable(total_cart_value)
        return total_cart_value + tax_payable_on_cart_items

    def tax_payable(self, total_cart_value):
        """
        Calculates the tax based on the region.
        """
        regional_tax_rule_percent = RegionalTaxRuleFactory.get_tax_rule_percent_for_region(self.region)
        return total_cart_value * regional_tax_rule_percent
