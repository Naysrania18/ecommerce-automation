import pytest

def test_ecommerce_flow():
    steps = ["login", "browse", "add_to_cart", "checkout"]
    assert len(steps) == 4
    print("✅ Complete shopping flow: " + " → ".join(steps))

def test_math():
    assert 1 + 1 == 2
    assert 5 * 5 == 25
    print("✅ Math calculations correct")

class TestShopping:
    def test_add_to_cart(self):
        items_in_cart = 3
        assert items_in_cart > 0
        print(f"✅ {items_in_cart} items in cart")
    
    def test_checkout(self):
        total_amount = 2999
        assert total_amount > 0
        print(f"✅ Checkout amount: ₹{total_amount}")