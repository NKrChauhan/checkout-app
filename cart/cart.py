from cart.cart_item import CartItem
from product.product import Product


class Cart:
    """
    Manages the shopping cart, including adding items, removing items, and getting the total price.
    """
    def __init__(self):
        self.items = []

    def get_cart_items_data(self):
        cart_items_data = []
        for cart_item in self.items:
            cart_item_data = {
                "product_name": cart_item.product.name,
                "product_quantity": cart_item.quantity,
                "price_for_product": cart_item.cart_item_price
            }
            cart_items_data.append(cart_item_data)
        return cart_items_data

    def add_item(self, product: Product, quantity: int = 1):
        """
        Adds an item (product) to the cart, optionally specifying quantity.
        """
        existing_item = next((item for item in self.items if item.product.name == product.name), None)
        if existing_item:
            existing_item.quantity += quantity
        else:
            self.items.append(CartItem(product, quantity))

    def remove_item(self, product: Product, quantity: int = 1):
        """
        Removes an item (product) from the cart, optionally specifying quantity.
        """
        for item in self.items:
            if item.product.name == product.name:
                if item.quantity > quantity:
                    item.quantity -= quantity
                else:
                    self.items.remove(item)
                return

    def get_total_price(self) -> float:
        """
        Calculates the total price of all items in the cart, considering both individual and bulk pricing.
        """
        total = 0
        for item in self.items:
            total += item.cart_item_price()
        return total
