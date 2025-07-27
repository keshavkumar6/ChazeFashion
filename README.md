

# ChazeFashion Product Catalog

A Django web application for managing and browsing a product catalog, including features like user authentication, product listing, cart, wishlist, and user profiles.

## Features

- User registration, login, and profile management
- Product listing and detail pages
- Shopping cart and wishlist functionality
- Admin interface for managing products
- Media support for product images and user avatars

## Project Structure

- ChazeFashion – Main Django project folder
- `catalog/` – Django app for product catalog features
- `theme/` – Custom theme and static assets
- `media/` – Uploaded product images and avatars
- `templates/` – HTML templates for the app

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repo-url>
   cd ChazeFashion
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`

## Custom Management Commands

- Seed products:  
  ```
  python manage.py seed_products
  ```

## License

MIT License

---

Let me know if you want to save or customize this README further!

Similar code found with 1 license type

keshavkumar6: hoe to copy htis as a whole

GitHub Copilot: To copy the entire README content as a whole:

1. Hover your mouse over the code block (the README content).
2. Click the "Copy" button (usually appears in the top-right corner of the code block).
3. If there is no copy button, select all the text inside the code block with your mouse, right-click, and choose "Copy" or press Ctrl+C (Cmd+C on Mac).

You can then paste it wherever you need. Let me know if you need the content again!
