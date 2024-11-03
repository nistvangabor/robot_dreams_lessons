class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and quantities, e.g., {"apple": 2}

    def add_item(self, item_name: str, price: float, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
        else:
            self.items[item_name] = {"price": price, "quantity": quantity}
    
    def remove_item(self, item_name: str, quantity: int = 1):
        if item_name not in self.items:
            raise ValueError("Item not in cart.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if self.items[item_name]["quantity"] <= quantity:
            del self.items[item_name]
        else:
            self.items[item_name]["quantity"] -= quantity
    
    def total_cost(self):
        return sum(item["price"] * item["quantity"] for item in self.items.values())
    
    def apply_discount(self, discount_code: str):
        # This would call an external service to check discount validity
        # For testing purposes, we will mock this part
        valid_codes = {"SAVE10": 0.1, "SAVE20": 0.2}
        discount = valid_codes.get(discount_code, 0)
        return self.total_cost() * (1 - discount)

    def checkout(self, discount_code: str):
        # Apply the discount and return the final cost
        discounted_price = self.apply_discount(discount_code)
        return discounted_price    

    def __str__(self):
        return f"ShoppingCart with {len(self.items)} items, Total Cost: {self.total_cost():.2f}"
    

cart_1 = ShoppingCart()
cart_1.add_item("apple", 12, 3)