from cart.cart import Cart
from checkout.checkout import Checkout
from product.product import Product


def test_case_setup(run_test_cases):
    """
        Decorator that sets up product objects and bulk price offers for test cases.
        """
    products = {
        "A": Product("A", 50, {3: 130}),
        "B": Product("B", 30, {2: 45}),
        "C": Product("C", 20),
        "D": Product("D", 15),
    }

    def get_result_for_test_case(*args, **kwargs):
        return run_test_cases(products=products, *args, **kwargs)

    return get_result_for_test_case


@test_case_setup
def run_test_cases(cart_items_string: str, products: dict):
    cart = Cart()
    for cart_item in cart_items_string:
        cart.add_item(products.get(cart_item))

    checkout = Checkout(cart)
    return checkout.get_total_payable_amount()


# Edit the test cases here
if __name__ == '__main__':
    test_cases = [
        ("", 0),
        ("A", 50),
        ("AB", 80),
        ("CDBA", 115),
        ("AA", 100),
        ("AAA", 130),
        ("AAAA", 180),
        ("AAAAA", 230),
        ("AAAAAA", 260),
        ("AAAB", 160),
        ("AAABB", 175),
        ("AAABBD", 190),
        ("DABABA", 190)
    ]
    for test_case in test_cases:
        print(f"Running.. test case '{test_case[0]}'")
        assert run_test_cases(cart_items_string=test_case[0]) == test_case[1]
        print("...OK\n")

    while True:
        user_test_case = input("Enter cart items: ")
        print(run_test_cases(cart_items_string=user_test_case))
