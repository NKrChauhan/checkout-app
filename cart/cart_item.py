from product.product import Product


class CartItem:
    """
    Represents an item in the shopping cart, including product and quantity.
    """

    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    def cart_item_price(self):
        """
        :return: cart item price based on discounted bulk quantities if applicable
        """
        discounted_bulk_quantities = list(self.product.bulk_price.keys())
        quantities_of_item = self.quantity
        cart_item_price = 0.0
        if discounted_bulk_quantities:
            # Taking priority to higher value of quantity for eg:  4 for 18 over 2 for 9
            discounted_bulk_quantities.sort(reverse=True)
            for discounted_bulk_quantity in discounted_bulk_quantities:
                number_of_bulk_quantity_lot = quantities_of_item // discounted_bulk_quantity
                quantities_of_item -= (number_of_bulk_quantity_lot * discounted_bulk_quantity)
                cart_item_price = self.product.bulk_price[discounted_bulk_quantity] * number_of_bulk_quantity_lot
        cart_item_price += self.product.individual_price * quantities_of_item
        return cart_item_price
