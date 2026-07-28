import datetime

class Item:
    """
    Represents a product item in the system, including its price, quantity, and related product.
    """
    price: int = 0
    amount: int = 0
    product: "Product"

class Seller:
    """
    Represents a seller in the system, including account details, rating, wallet, and offered products.
    """
    id: int = 0
    name: str = ""
    rate: float = 0.0
    orders_list: str = ""
    wallet: int = 0
    number_of_sells: int = 0
    income: float = 0.0
    cost: int = 0
    profit: int = 0
    seller_id: int = 0
    company_name: str = ""
    products: list[Item]

class Transaction:
    """
    Represents a financial transaction such as a deposit or withdrawal with its amount and date.
    """
    amount: int = 0
    date: datetime.datetime = None
    transaction_type: str = ""

    def __init__(self, amount: int, date: datetime.datetime = None):
        """
        Initializes a transaction object.
        """
        self.amount = amount
        self.date = date

class Wallet:
    """
    Represents a wallet used to manage deposits, withdrawals, and transaction history.
    """
    wallet_id: int = 0
    transactions: list[Transaction]
    
    def deposit(self, amount: int) -> None:
        """
        Adds money to the wallet.
        """
        if not isinstance(amount, int):
            print("amount should be integer")
        elif amount < 0:
            print("amount should be a positive integer")
        else:
            transaction = Transaction(amount, datetime.datetime.now())
            self.transactions.append(transaction)

    def withdraw(self, amount: int) -> None:
        """
        Withdraws money from the wallet if the balance is sufficient.
        """
        if not isinstance(amount, int):
            print("amount should be integer")
        elif amount < 0:
            print("amount should be a positive integer")
        balance = 0
        for t in self.transactions:
            if t.transaction_type == "deposit":
                balance += t.amount
            elif t.transaction_type == "withdraw":
                balance -= t.amount
        if amount > balance:
            print("عدم موجودی")
        transaction = Transaction(amount, datetime.datetime.now())
        self.transactions.append(transaction)

class Coupon:
    """
    Represents a discount coupon that can be assigned to specific customers and products.
    """
    code: str = ""
    expire_date: int = 0
    amount: int = 0
    usage_limit: int = 0
    used_count: int = 0
    allowed_customers: list["Customer"]
    products: "Product"

class CartItem:
    """
    Represents an item inside a shopping cart, including product, seller, price, and quantity.
    """
    poduct: "Product"
    seller: Seller
    price: int = 0
    amount: int = 0
    coupon: Coupon
    wallet: Wallet

    def __init__(self, product: "Product", amount: int):
        """
        Initializes a cart item.
        """
        self.product = product
        self.amount = amount

    def __eq__(self, other):
        """
        Compares two cart items based on their product.
        """
        if not isinstance(other, CartItem):
            return False
        return (self.product == other.product)

class ShoppingCart:
    """
    Represents a customer's shopping cart and manages cart operations.
    """
    cart_items: list[CartItem]
    broken_products: list[CartItem]

    def add_item(self, cart_item: CartItem) -> None:
        """
        Adds an item to the cart or increases its quantity if it already exists.
        """
        item = CartItem(product=Product)
        if item not in self.cart_items:
            self.cart_items.append(item)
        elif cart_item in self.cart_items:
            i = self.cart_items.index(cart_item)
            self.cart_items[i].amount += 1

    def remove_item(self, cart_item: CartItem) -> None:
        """
        Removes an item from the cart.
        """
        item = CartItem(product=Product)
        if item not in self.cart_items:
            print("the product doesnt exist")
        elif cart_item in self.cart_items:
            self.cart_items.remove(item)
            return

    def increase_item(self, cart_item: CartItem) -> None:
        """
        Increases the quantity of an item in the cart by one.
        """
        item = CartItem(product=Product)
        if item not in self.cart_items:
            print("the product doesnt exist")
        elif cart_item in self.cart_items:
            i = self.cart_items.index(cart_item)
            self.cart_items[i].amount += 1

    def decrease_item(self, cart_item: CartItem) -> None:
        """
        Decreases the quantity of an item in the cart and removes it if the quantity becomes one.
        """
        item = CartItem(product=Product)
        if item not in self.cart_items:
            print("the product doesnt exist")
            return
        i = self.cart_items.index(cart_item)
        if self.cart_items[i].amount == 1:
            self.cart_items.remove(i)
        elif cart_item in self.cart_items:
            self.cart_items[i].amount -= 1

class SellerPanel:
    """
    Represents the seller panel used to manage incoming orders.
    """
    order_list: list[ShoppingCart]

class Comment:
    """
    Represents a customer comment and rating for a product.
    """
    comment: str = ""
    date: int = 0
    product_rating: int = 0
    customer: "Customer"

class Product:
    """
    Represents a product in the store, including comments, score, and offers.
    """
    score: int = 0
    id: str = ""
    name: str = ""
    discount_code: str = ""
    comments: list[Comment]
    offers: list[SellerPanel]

    def __eq__(self, other):
        """
        Compares two products based on their ID.
        """
        if not isinstance(other, CartItem):
            return False
        return (self.id == other.id)

    def __init__(self, id, name):
        """
        Initializes a product.
        """
        self.id = id
        self.name = name
        self.comments = []

    def add_comment(self, comment: Comment) -> None:
        """
        Adds a new comment to the product.
        """
        new_comment = Comment()
        self.comments.append(new_comment)

    def remove_comment(self, comment: Comment) -> None:
        """
        Removes a comment from the product.
        """
        comment = Comment(customer=Customer)
        if comment not in self.comments:
            print("the comment doesnt exist")
        else:
            self.comments.remove(comment)

class Coupon:
    """
    Represents a discount coupon with usage limits and eligible customers/products.
    """
    code: str = ""
    expire_date: int = 0
    amount: int = 0
    usage_limit: int = 0
    used_count: int = 0
    allowed_customers: list["Customer"]
    products: Product

class FavoriteList:
    """
    Represents a customer's wishlist item.
    """
    date: datetime.datetime = None
    product: Product

    def __init__(self, product: Product):
        """
        Initializes a favorite list item.
        """
        self.product = product

    def __eq__(self, other):
        """
        Compares two favorite items based on the product ID.
        """
        if not isinstance(other, FavoriteList):
            return False
        return self.product.id == other.product.id

class Customer:
    """
    Represents a customer with profile data, wishlist, orders, cart items, and wallet.
    """
    customer_id: str = ""
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    phone_number: str = ""
    password: str = ""
    registration_date: int = 0
    wishlist: list[FavoriteList]
    orders_history: list[ShoppingCart]
    orders: ShoppingCart
    customer_rateing: int = 0
    cart_items: list[CartItem]
    wallet: Wallet

    def add_to_wishlist(self, wishlist: FavoriteList) -> None:
        """
        Adds a product to the customer's wishlist.
        """
        if not isinstance(wishlist, (int, str, list)):
            print("error")
            return

        if item in self.wishlist:
            print("product already exists")
            return
        item = FavoriteList(product=Product)
        self.wishlist.append(item)

    def remove_from_wishlist(self, wishlist: FavoriteList) -> None:
        """
        Removes a product from the customer's wishlist.
        """
        if not isinstance(wishlist, (int, str, list)):
            print("error")
            return

        if item in self.wishlist:
            item = FavoriteList(product=Product)
            self.wishlist.remove(item)
            return
        else:
            print("product doesnt exists")

    def purchase(self) -> "WaitingOrders":
        """
        Finalizes the purchase and creates a waiting order.
        """
        pass

class WaitingOrders:
    """
    Represents orders that are waiting for processing or approval.
    """
    cart: ShoppingCart
    customer: Customer

class SellerPanel:
    """
    Represents the seller panel that holds a list of orders.
    """
    order_list: list[ShoppingCart]

class Comment:
    """
    Represents a product comment along with its rating and author.
    """
    comment: str = ""
    date: int = 0
    product_rating: int = 0
    customer: Customer

    def __init__(self, comment, product_rating, customer):
        """
        Initializes a comment object.
        """
        self.comment = comment
        self.date = datetime.datetime.now
        self.product_rating = product_rating
        self.customer = customer

    def __eq__(self, other):
        """
        Compares two comments by text, rating, and customer.
        """
        if not isinstance(other, Comment):
            return False
        return self.comment == other.comment / self.product_rating == self.product_rating / self.customer == other.customer

class Store:
    """
    Represents the main store system, managing customers, sellers, products, orders, and coupons.
    """
    sellers_commission: int = 0
    store_id: str = ""
    seller_id: str = ""
    store_name: str = ""
    rate: int = 0
    operater: str = ""
    level: int = 0
    delivery_time: int = 0
    customers: list[Customer]
    waiting_products: list[Product]
    waiting_sellers: list[Seller]
    rejected_products: list[Product]
    rejected_sellers: list[Seller]
    coupons: list[Coupon]
    waiting_orders: list[WaitingOrders]
    products: list[Product]
    sellers: list[Seller]

    def add_customer(self, customer: Customer) -> None:
        """
        Adds a customer to the store system.
        """
        pass

    def remove_customer(self, customer: Customer) -> None:
        """
        Removes a customer from the store system.
        """
        pass

    def add_seller(self, seller: Seller) -> None:
        """
        Adds a seller to the store system.
        """
        pass

    def remove_seller(self, seller: Seller) -> None:
        """
        Removes a seller from the store system.
        """
        pass

    def confirm_seller(self, seller: Seller) -> None:
        """
        Confirms a seller that is waiting for approval.
        """
        pass

    def confirm_customer(self, product: Product) -> None:
        """
        Confirms a product or customer-related approval request.
        """
        pass

    def generate_customer_id(self) -> str:
        """
        Generates a unique customer ID.
        """
        pass

class OperaterPanel:
    """
    Represents the operator panel used for monitoring profit, sales, and store confirmations.
    """
    profit: int = 0
    sells: int = 0
    shoppings: int = 0
    confirmation: list[Seller]
    stores: list[Store]
    discount_code: list[Coupon]
