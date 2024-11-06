class Customer:
    """Represents a customer with information and loyalty membership status."""
    
    def __init__(self, name, contact_info, loyalty_member=False):
        self._name = name
        self._contact_info = contact_info
        self._loyalty_member = loyalty_member
        self._id = None  # Placeholder for a unique customer ID

    # Getters
    def get_name(self):
        return self._name
    
    def get_contact_info(self):
        return self._contact_info
    
    def is_loyalty_member(self):
        return self._loyalty_member
    
    def get_id(self):
        return self._id

    # Setters
    def set_name(self, name):
        self._name = name
    
    def set_contact_info(self, contact_info):
        self._contact_info = contact_info
    
    def set_loyalty_member(self, loyalty_member):
        self._loyalty_member = loyalty_member
    
    def set_id(self, id):
        self._id = id

    def __str__(self):
        return f"Customer(Name: {self._name}, Contact: {self._contact_info}, Loyalty Member: {self._loyalty_member})"


class EBook:
    """Represents an eBook with title, author, year, genre, price, and stock status."""
    
    def __init__(self, title, author, publication_year, genre, price, in_stock=True):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._genre = genre
        self._price = price
        self._in_stock = in_stock  # New attribute to indicate stock status

    # Getters
    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_publication_year(self):
        return self._publication_year
    
    def get_genre(self):
        return self._genre
    
    def get_price(self):
        return self._price
    
    def is_in_stock(self):
        return self._in_stock  # Check stock status

    # Setters
    def set_title(self, title):
        self._title = title
    
    def set_author(self, author):
        self._author = author
    
    def set_publication_year(self, publication_year):
        self._publication_year = publication_year
    
    def set_genre(self, genre):
        self._genre = genre
    
    def set_price(self, price):
        self._price = price

    def set_stock_status(self, in_stock):
        self._in_stock = in_stock  # Update stock status

    def __str__(self):
        return f"{self._title} by {self._author} ({self._publication_year}) - ${self._price}. " \
               f"{'In Stock' if self._in_stock else 'Out of Stock'}"


class ShoppingCart:
    """Manages items in the shopping cart."""
    
    def __init__(self):
        self._items = []

    # Getters
    def get_items(self):
        return self._items

    def get_total_items(self):
        return len(self._items)

    def calculate_total(self):
        return sum(item.get_price() for item in self._items)

    # Add and remove items
    def add_item(self, ebook):
        if ebook.is_in_stock():  # Only add if the eBook is in stock
            self._items.append(ebook)
        else:
            print(f"Cannot add '{ebook.get_title()}' to cart. It is currently out of stock.")

    def remove_item(self, ebook):
        if ebook in self._items:
            self._items.remove(ebook)

    def clear_cart(self):
        self._items.clear()

    def __str__(self):
        return f"Shopping Cart with {len(self._items)} items. Total: ${self.calculate_total()}"


class Order:
    """Represents an order by a customer with a total cost."""
    
    def __init__(self, customer, cart):
        self._customer = customer
        self._cart = cart
        self._order_id = None  # Placeholder for a unique order ID

    # Getters
    def get_customer(self):
        return self._customer
    
    def get_cart(self):
        return self._cart

    def get_order_id(self):
        return self._order_id
    
    def get_total_cost(self):
        return self._cart.calculate_total()

    # Setters
    def set_customer(self, customer):
        self._customer = customer
    
    def set_cart(self, cart):
        self._cart = cart
    
    def set_order_id(self, order_id):
        self._order_id = order_id

    def __str__(self):
        return f"Order for {self._customer.get_name()}, Total Cost: ${self.get_total_cost()}"


class Invoice:
    """Generates a formatted invoice based on an order."""  
    
    def __init__(self, order):
        self._order = order
        self._invoice_id = None  # Placeholder for a unique invoice ID

    # Getters
    def get_order(self):
        return self._order
    
    def get_invoice_id(self):
        return self._invoice_id

    # Setters
    def set_order(self, order):
        self._order = order
    
    def set_invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    def __str__(self):
        items_summary = "\n".join(str(item) for item in self._order.get_cart().get_items())
        return f"Invoice for {self._order.get_customer().get_name()}:\n" \
               f"{items_summary}\nTotal Cost: ${self._order.get_total_cost()}"
