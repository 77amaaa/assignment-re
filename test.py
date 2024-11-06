# test_ebookstore.py

from solution import Customer, EBook, ShoppingCart, Order, Invoice

def test_ebookstore():
    # Creating a customer
    print("\n--- Customer Information ---")
    customer = Customer("Alice", "alice@example.com", True)
    customer.set_id(1)  # Setting a unique ID for the customer
    print(f"Customer ID: {customer.get_id()}")
    print(f"Name: {customer.get_name()}")
    print(f"Contact Info: {customer.get_contact_info()}")
    print(f"Loyalty Member: {'Yes' if customer.is_loyalty_member() else 'No'}")

    # Creating eBooks with varying stock statuses
    print("\n--- Available eBooks ---")
    ebook1 = EBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 10.99, in_stock=True)
    ebook2 = EBook("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 8.99, in_stock=False)  # Out of stock
    print(ebook1)
    print(ebook2)

    # Adding items to shopping cart
    print("\n--- Adding Items to Shopping Cart ---")
    cart = ShoppingCart()
    cart.add_item(ebook1)  # Should succeed
    cart.add_item(ebook2)  # Should print a message about out of stock
    print(f"Total Items in Cart: {cart.get_total_items()}")
    print(f"Items in Cart: {[item.get_title() for item in cart.get_items()]}")
    print(f"Total Cost in Cart: ${cart.calculate_total():.2f}")

    # Creating an order
    print("\n--- Order Details ---")
    order = Order(customer, cart)
    order.set_order_id(101)  # Setting a unique order ID
    print(f"Order ID: {order.get_order_id()}")
    print(f"Customer for Order: {order.get_customer().get_name()}")
    print(f"Total Cost for Order: ${order.get_total_cost():.2f}")

    # Generating invoice
    print("\n--- Invoice Summary ---")
    invoice = Invoice(order)
    invoice.set_invoice_id(1001)  # Setting a unique invoice ID
    print(f"Invoice ID: {invoice.get_invoice_id()}")
    print(f"Customer Name on Invoice: {invoice.get_order().get_customer().get_name()}")
    print(f"Total Cost on Invoice: ${invoice.get_order().get_total_cost():.2f}")
    print("Invoice Items:")
    for item in invoice.get_order().get_cart().get_items():
        print(f"  - {item.get_title()} by {item.get_author()} - ${item.get_price()}")
    print(invoice)

if __name__ == "__main__":
    test_ebookstore()
