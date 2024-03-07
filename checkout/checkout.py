from cart.cart import Cart
from checkout.constants import REGION
from checkout.helpers.regional_tax_rule import RegionalTaxRuleHelper


class Checkout:
    """
    Manages the checkout process and calculating the total price.
    """

    def __init__(self, cart: Cart, region=REGION.INDIA):
        self.cart = cart
        self.region = region

        if not isinstance(self.region, str):
            raise ValueError("Region must be a string.")

    def do_checkout(self):
        try:
            cart_data = self.cart.get_cart_items_data()
            total_payable_amount = self.get_total_payable_amount()
            return {
                "cart_data": cart_data,
                "total_payable_amount (including tax)": total_payable_amount
            }
        except (ValueError, KeyError) as e:
            raise Exception(f"Checkout error: {e}")

    def get_total_payable_amount(self) -> float:
        """
        Calculates the total price of all items in the cart using the Cart object.
        """
        total_cart_value = self.cart.get_total_price()
        try:
            tax_payable_on_cart_items = self.tax_payable(total_cart_value) * total_cart_value
            return total_cart_value + tax_payable_on_cart_items
        except Exception as e:
            raise Exception(f"Failed to calculate total payable amount.{e}")

    def tax_payable(self, total_cart_value):
        """
        Calculates the tax based on the region.
        """
        regional_tax_rule_percent = RegionalTaxRuleHelper.get_tax_rule_percent_for_region(self.region)
        return total_cart_value * regional_tax_rule_percent
