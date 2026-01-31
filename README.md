# Django Basic E-commerce Site

A simple e-commerce web application built with Django. This project demonstrates the core features of an online store, including product listing, shopping cart, user authentication, and order management.

## Features

- User registration and authentication
- Product catalog with categories
- Shopping cart functionality
- Order placement and order history
- Admin dashboard for product and order management

## Installation

1. **Clone the repository:**
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the site:**
    - Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

- Browse products and add them to your cart.
- Register or log in to place orders.
- Manage products and orders via the Django admin panel.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.

