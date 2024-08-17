# E-Commerce API

## Description

This is an E-Commerce API built with Django and Django REST Framework. It provides endpoints to manage categories, products, carts, and purchases. The API supports CRUD operations and handles business logic such as calculating the total price of purchases and ensuring that product prices and stock quantities are non-negative.

## Models

### Category

Represents a category for products.

- `category`: The name of the category (unique).
- `created_at`: Timestamp for when the category was created.
- `updated_at`: Timestamp for when the category was last updated.

### Product

Represents a product in the inventory.

- `category`: Foreign key linking to the `Category` model.
- `product`: The name of the product (unique).
- `description`: Description of the product (unique).
- `price`: Price of the product.
- `stock`: Number of items in stock.
- `created_at`: Timestamp for when the product was created.
- `updated_at`: Timestamp for when the product was last updated.

### Cart

Represents a shopping cart for a user.

- `owner`: Foreign key linking to the `User` model.
- `products`: Many-to-many relationship with `Product`.
- `created_at`: Timestamp for when the cart was created.
- `updated_at`: Timestamp for when the cart was last updated.

### Buy

Represents a purchase made by a user.

- `user`: Foreign key linking to the `User` model.
- `products`: Many-to-many relationship with `Product`.
- `total_price`: Total price of all purchased products.
- `is_paid`: Boolean indicating if the purchase has been paid.
- `created_at`: Timestamp for when the purchase was created.
- `updated_at`: Timestamp for when the purchase was last updated.

## Serializers

### CategorySerializer

Serializes `Category` instances, including all fields.

### ProductSerializer

Serializes `Product` instances and replaces category IDs with category names.

### CartSerializer

Serializes `Cart` instances, including detailed information about products and the owner's username.

### BuySerializer

Serializes `Buy` instances, including detailed information about purchased products.

## ViewSets

### CategoryAPI

Provides CRUD operations for `Category` instances.

### ProductAPI

Provides CRUD operations for `Product` instances.

### CartAPI

Provides CRUD operations for `Cart` instances.

### BuyAPI

Provides CRUD operations for `Buy` instances.

## URLs

The following routes are available:

- `GET /categories/` - List all categories.
- `POST /categories/` - Create a new category.
- `GET /categories/{id}/` - Retrieve a specific category.
- `PUT /categories/{id}/` - Update a specific category.
- `DELETE /categories/{id}/` - Delete a specific category.

- `GET /products/` - List all products.
- `POST /products/` - Create a new product.
- `GET /products/{id}/` - Retrieve a specific product.
- `PUT /products/{id}/` - Update a specific product.
- `DELETE /products/{id}/` - Delete a specific product.

- `GET /carts/` - List all carts.
- `POST /carts/` - Create a new cart.
- `GET /carts/{id}/` - Retrieve a specific cart.
- `PUT /carts/{id}/` - Update a specific cart.
- `DELETE /carts/{id}/` - Delete a specific cart.

- `GET /buys/` - List all purchases.
- `POST /buys/` - Create a new purchase.
- `GET /buys/{id}/` - Retrieve a specific purchase.
- `PUT /buys/{id}/` - Update a specific purchase.
- `DELETE /buys/{id}/` - Delete a specific purchase.
