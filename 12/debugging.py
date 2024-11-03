from cart_processor import process_cart_items

def main() -> None:
    shopping_carts = {
        "Alice": [12.99, 23.50, 5.75, 8.99],
        "Bob": [5.00, 15.00, 3.25, 12.50],
        "Charlie": [25.00, 35.00, 10.00]
    }  

    for customer, prices in shopping_carts.items():
        process_cart_items(customer_name=customer, prices=prices)


if __name__ == "__main__":
    main()
