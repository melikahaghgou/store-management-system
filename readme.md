# Store Management System

This project is about Store Management System by python.It is created to help with running a store by a way of writing code called Object-Oriented Programming.The main idea of this project is to make it easier for people to manage their stores.

The system has parts like sellers and customers and products. It also has shopping carts, wallets, transactions, comments and coupons. Each part does something.The Store part is like the center that connects all the parts with eachother.

This project shows how all these parts work together to make a system for managing a store. All the code has comments written in English to make it easy to read.

The project also has a diagram named `seller.pdf` that shows how all the parts fit together.It helps people understand how the system is designed and how it works.


## Class Overview

This project is made up of classes. Each class does a job for the store system. The main idea is to keep the code neat and have each part of the project do one thing.

### Seller

The Seller class stores information about the seller. It has things like the sellers id, name, rate, wallet, number of sells, income, cost, profit, seller id company name and products. These things help manage the sellers profile, sales, money and products.

### Store

The Store class is the class of the project. It connects the sellers, customers, products, coupons and orders that are waiting. It has things like store id, store name, rate, operator, level, delivery time, sellers, customers, products, products that are waiting sellers that are waiting products that were rejected sellers that were rejected and coupons. Some of its jobs are to add or remove sellers and customers confirm sellers and products make ids and calculate seller scores.

### Product

The Product class stores information about the product. It has things like score id, name, discount code, comments and offers. This class also has jobs to add and remove comments.

### Customer

The Customer class stores information about the customer. Keeps track of their wishlist cart orders and wallet. It has things like customer id, first name, last name, email, phone number, password, registration date wishlist orders history orders, customer rating, cart items and wallet. It also has jobs to add and remove items from the wishlist and make a purchase.

### Item

The Item class is a product in the sellers inventory. It has things like price, amount and product. These things show how much the item costs how many are available and which product it is.

### Wallet

The Wallet class is used to manage money. It has things like wallet id and transactions. The deposit job adds money to the wallet. The withdraw job removes money from it.

### OperatorPanel

The OperatorPanel class is used to manage and check the store. It keeps track of profit, sells, shoppings, confirmation, stores and discount code. This class is useful to check the status of the store system.

### Coupon

The Coupon class is used for discount codes. It has things like code expire date, amount, usage limit, count allowed customers and products. These things define the discount value, expiration date, usage limit and which customers or products can use the coupon.

### CartItem

The CartItem class is used for items in the shopping cart. It has things like Product, seller, price, amount, coupon and wallet. This class helps keep track of each product added to the cart and its related information.

### Transaction

The Transaction class stores payment information. It has things like amount, date and transaction type to record the details of each operation.

### FavoriteList

The FavoriteList class is used to store products for customers. It has things like date and product which show when the item was added and which product was saved.

### Comment

The Comment class is used for customer feedback on products. It helps store the rating and opinion of users about a product.

### ShoppingCart

The ShoppingCart class manages products that a customer wants to buy. It is responsible for handling cart items, prices and purchase operations.

### SellerPanel

The SellerPanel class is used for seller offers and product-related actions. It helps sellers manage their product offers inside the system.

### WaitingOrders

The WaitingOrders class is used for orders that are not processed yet. It helps keep track of pending purchases before they are finalized. The Product. The Seller class work together, with the WaitingOrders class to make sure everything runs smoothly. The Store class is also connected to the WaitingOrders class to keep track of all the orders. The Customer class and the Product class are connected to the WaitingOrders class to make sure the customer gets the product.