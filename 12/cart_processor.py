def calculate_total(prices: list[float]) -> float:
    return sum(prices)


def process_cart_items(customer_name: str, prices: list[float]) -> float:
    total_price = calculate_total(prices)
    print(f"Total price for {customer_name}: ${total_price:.2f}")
    return total_price

