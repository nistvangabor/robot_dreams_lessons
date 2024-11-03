import pytest
from shopping_cart import ShoppingCart  # Assuming the class is saved in shopping_cart.py
from unittest.mock import patch

# Fixtures for setting up different ShoppingCart instances
@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 3)  # 3 apples at $1 each
    cart.add_item("banana", 0.5, 5)  # 5 bananas at $0.5 each
    return cart

# 1. Basic Test Cases

def test_add_item(empty_cart):
    empty_cart.add_item("apple", 1.0, 2)
    assert empty_cart.items["apple"]["quantity"] == 2
    assert empty_cart.items["apple"]["price"] == 1.0

def test_remove_item(cart_with_items):
    cart_with_items.remove_item("apple", 1)
    assert cart_with_items.items["apple"]["quantity"] == 2  # Started with 3 apples
    cart_with_items.remove_item("apple", 2)
    assert "apple" not in cart_with_items.items  # All apples removed

def test_total_cost(cart_with_items):
    assert cart_with_items.total_cost() == 5.5  # 3 * $1 + 5 * $0.5 = 5.5

# 2. Edge Cases with Parameterization

@pytest.mark.parametrize("item_name, price, quantity, expected_exception", [
    ("orange", -1.0, 1, ValueError),  # Negative price
    ("orange", 1.0, 0, ValueError),   # Zero quantity
    ("orange", 1.0, -2, ValueError),  # Negative quantity
])
def test_add_item_invalid_inputs(empty_cart, item_name, price, quantity, expected_exception):
    with pytest.raises(expected_exception):
        empty_cart.add_item(item_name, price, quantity)

@pytest.mark.parametrize("item_name, quantity, expected_exception", [
    ("apple", -1, ValueError),        # Negative quantity
    ("orange", 1, ValueError),        # Item not in cart
])
def test_remove_item_invalid_inputs(cart_with_items, item_name, quantity, expected_exception):
    with pytest.raises(expected_exception):
        cart_with_items.remove_item(item_name, quantity)

# 3. Test Apply Discount with Mocking


@patch('shopping_cart.ShoppingCart.apply_discount', return_value=4.4)
def test_checkout(mock_apply_discount, cart_with_items):
    # Here we are checking if checkout correctly utilizes apply_discount
    final_price = cart_with_items.checkout("SAVE10")
    
    # Ensure the checkout uses the mocked apply_discount and returns the expected value
    assert final_price == 4.4
    mock_apply_discount.assert_called_once_with("SAVE10")


# 4. Testing __str__ Representation

def test_str_representation(cart_with_items):
    result = str(cart_with_items)
    assert "ShoppingCart with 2 items" in result
    assert "Total Cost: 5.50" in result  # Total should match cart's total cost

# 5. Additional Functional Tests

def test_apply_discount_valid_code(cart_with_items):
    assert cart_with_items.apply_discount("SAVE10") == 4.95  # 10% off $5.5

def test_apply_discount_invalid_code(cart_with_items):
    assert cart_with_items.apply_discount("INVALID") == cart_with_items.total_cost()  # No discount applied

