# Store Management System

This project is about Store Management System by python.It is created to help with running a store by a way of writing code called Object-Oriented Programming.The main idea of this project is to make it easier for people to manage their stores.

The system has parts like sellers and customers and products. It also has shopping carts, wallets, transactions, comments and coupons. Each part does something.The Store part is like the center that connects all the parts with eachother.

This project shows how all these parts work together to make a system for managing a store. All the code has comments written in English to make it easy to read.

The project also has a diagram named `seller.pdf` that shows how all the parts fit together.It helps people understand how the system is designed and how it works.
 
# Installation

To get this project up and running on your computer you need to do a few things. First you have to get a copy of the project. You can do this by copying the project from the internet to your system.

```Bash

git clone https://github.com/melikahaghgou/store-management-system.git

```

Next you have to go into the project folder.

```Bash

cd store-management-system

```

Now you have to make sure that Python is installed on your system. You can check this by seeing what version of Python you have.

```bash

python --version

```

After you have checked that Python is installed you can run the Python file, for the store management system.

```bash

python seller.py

```

# Usage
## Class Overview

This section explains the classes of the project. For each class, the properties are described, and their related methods are placed directly under the property they modify or interact with.

---

### Item
Represents a product item in the system, combining the product details with its price and quantity.  
#### properties :
* **`price`**: The price of the item.
* **`amount`**: The quantity of this item available in stock.
* **`product`**: The actual `Product` details that this item is based on.

---

### Seller
Represents a seller account in the marketplace.
#### properties :
* **`id` / `seller_id`**: Unique identifiers for the seller.
* **`name`**: The personal name of the seller.
* **`company_name`**: The name of the seller's company.
* **`rate`**: The rating score of the seller based on customer feedback.
* **`orders_list`**: A record of orders related to this seller.
* **`wallet`**: The money amount or wallet reference for the seller's earnings.
* **`number_of_sells`**: The total number of items sold by the seller.
* **`income`**: The total revenue earned from sales.
* **`cost`**: The expenses or commission costs for the seller.
* **`profit`**: The net profit calculated from income and costs.
* **`products`**: A list of `Item` objects that this seller offers in the store.

---

### Transaction
Represents a single financial transaction.
#### properties :
* **`amount`**: The money amount involved in the transaction.
* **`date`**: The date and time when the transaction happened.
* **`transaction_type`**: The type of transaction (such as a deposit or a withdrawal).

---

### Wallet
Manages financial balances and transactions.
#### properties :
* **`wallet_id`**: The unique identifier of the wallet.
* **`transactions`**: A list of all `Transaction` records associated with this wallet.
#### methods :
  * **`deposit(amount)`**: Adds money to the wallet. It verifies that the amount is valid and appends a new deposit transaction to the `transactions` list.

  * **`withdraw(amount)`**: Deducts money from the wallet. It checks if there is enough balance by reading the history in the `transactions` list, and then appends a new withdrawal transaction.

---

### Coupon
Represents a discount coupon that can be applied to orders.
#### properties :
* **`code`**: The unique text code of the coupon.
* **`expire_date`**: The expiration date of the coupon.
* **`amount`**: The discount value or percentage.
* **`usage_limit`**: The maximum number of times this coupon can be used.
* **`used_count`**: The number of times the coupon has actually been used.
* **`allowed_customers`**: A list of `Customer` accounts who are permitted to use this coupon.
* **`products`**: The specific `Product` or products that this coupon can be applied to.

---

### CartItem
Represents a single product inside a shopping cart.
#### properties :
* **`product`**: The `Product` that the customer wants to buy.
* **`seller`**: The `Seller` who provides this product.
* **`price`**: The price of the product at the time it was added.
* **`amount`**: The quantity of the product added to the cart.
* **`coupon`**: A `Coupon` applied to this specific cart item.
* **`wallet`**: The `Wallet` used to check or process the payment for this item.

---

### ShoppingCart
Manages the items selected by a customer for purchase.
#### properties :
* **`broken_products`**: A list of cart items that have issues or are no longer available.
* **`cart_items`**: A list of `CartItem` objects currently in the cart.
#### methods :
  * **`add_item(cart_item)`**: Adds a new item to the cart. If the item is already in the list, it increases its quantity.
  * **`remove_item(cart_item)`**: Removes a specific item completely from the cart.
  * **`increase_item(cart_item)`**: Increases the quantity of an existing item in the cart by one.
  * **`decrease_item(cart_item)`**: Decreases the quantity of an item in the cart. If the quantity reaches one, it removes the item.

---

### SellerPanel
Represents the control panel for a seller to track orders.
* **`order_list`**: A list of `ShoppingCart` objects representing orders sent to the seller.

---

### Comment
Represents feedback left by a customer.
#### properties :
* **`comment`**: The text content of the feedback.
* **`date`**: The date when the comment was written.
* **`product_rating`**: The numerical rating score given to the product.
* **`customer`**: The `Customer` who wrote the comment.

---

### Product
Represents a general product profile in the system.
#### properties :
* **`id`**: The unique identifier of the product.
* **`name`**: The name of the product.
* **`score`**: The average rating of the product.
* **`discount_code`**: A discount code linked to this product.
* **`offers`**: A list of `SellerPanel` options showing which sellers offer this product.
* **`comments`**: A list of `Comment` objects written by customers for this product.
#### methods :
  * **`add_comment(comment)`**: Adds a new comment to the comments list.
  * **`remove_comment(comment)`**: Searches for and removes a specific comment from the comments list.

---

### FavoriteList
Represents an item in a customer's wishlist.
#### properties :
* **`date`**: The date the product was favorited.
* **`product`**: The `Product` saved by the customer.

---

### Customer
Represents a customer account with shopping details.
#### properties :
* **`customer_id`**: The unique identifier of the customer.
* **`first_name` / `last_name`**: The customer's personal name.
* **`email`**: The registered email address.
* **`phone_number`**: The customer's contact number.
* **`password`**: The password for account authentication.
* **`registration_date`**: The date the customer registered.
* **`orders_history`**: A list of past orders (`ShoppingCart` objects) completed by the customer.
* **`orders`**: The current active `ShoppingCart` of the customer.
* **`customer_rating`**: The user rating of the customer.
* **`cart_items`**: A list of `CartItem` objects currently prepared for purchase.
* **`wallet`**: The customer's `Wallet` used to pay for purchases.
  
* **`wishlist`**: A list of `FavoriteList` items saved by the customer.
#### methods :
  * **`add_to_wishlist(wishlist)`**: Adds a product to the customer's wishlist if it is not already there.
  * **`remove_from_wishlist(wishlist)`**: Removes a product from the customer's wishlist.
  * **`purchase()`**: Finalizes the current cart items and turns them into a waiting order for processing.
---

### WaitingOrders
Represents an order that has been submitted but is waiting for processing.
#### properties :
* **`cart`**: The `ShoppingCart` containing the purchased items.
* **`customer`**: The `Customer` who placed the order.

---

### Store
Represents the main administrative store system.
#### properties :
* **`store_id`**: Unique identifier for the store.
* **`store_name`**: The name of the store.
* **`rate`**: The overall rating of the store.
* **`operater`**: The operator managing the store settings.
* **`level`**: The level or tier of the store.
* **`delivery_time`**: The default delivery time setting.
* **`sellers_commission`**: The percentage fee taken from seller sales.
* **`waiting_products`**: Products waiting for review before appearing in the store.
* **`rejected_products`**: Products that were not approved.
* **`waiting_sellers`**: Sellers waiting for approval to join the store.
  
* **`rejected_sellers`**: Sellers that were rejected.
* **`coupons`**: A list of all valid coupons in the store.
* **`waiting_orders`**: A list of orders waiting for operator approval.
* **`products`**: A list of all approved products available in the store.
#### methods :
  * **`confirm_seller(seller)`**: Confirms and approves a pending seller from the waiting list.
  *  **`confirm_product(product)`**: Approves a product request and makes the product available in the store.
  * **`add_seller(seller)`**: Registers a new seller in the system.
  * **`remove_seller(seller)`**: Removes a seller from the active list.
  * **`add_customer(customer)`**: Registers a new customer in the store.
  * **`remove_customer(customer)`**: Removes a customer from the active list.
  * **`generate_customer_id()`**: Generates a unique customer ID during registration.
  
---

### OperaterPanel
Represents the control panel for the store operator.
#### properties :
* **`profit`**: The total system profits earned from commissions.
* **`sells`**: The total number of sales tracked across the platform.
* **`shoppings`**: The total purchases monitored in the system.
* **`confirmation`**: A list of sellers waiting for the operator's review.
* **`stores`**: A list of store entities under the operator's control.
* **`discount_code`**: A list of active store coupons managed by the operator.