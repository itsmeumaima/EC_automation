# PostSync – E-Commerce Platform

**PostSync** is a modern e-commerce web application built with **Django**, **Tailwind CSS**, and **SQLite**.  
It provides a seamless shopping experience for users and an efficient management panel for admins.  
A standout feature is its **automation system** using **Make (Integromat)** and **Cloudinary Webhooks** to automatically post new products on **Instagram** and **Facebook** whenever an admin uploads a new item to the website.

---

##  Features

###  User Features
- Browse and search products
- Add items to the cart
- Manage cart (update quantity, remove items)
- Checkout with order summary
- User authentication (sign up, login, logout)

###  Admin Features
- Add, update, and delete products
- View and manage orders
- Manage user data
- Product images hosted using **Cloudinary**

###  Automation Feature (Make + Cloudinary Webhooks)
Whenever an admin uploads a new product:
1. The image and product data are uploaded to **Cloudinary**.
2. **Cloudinary Webhook** triggers a **Make (Integromat)** automation scenario.
3. Make fetches the product details (title, price, image URL) from the Django backend.
4. It automatically posts the new product to:
   -  **Instagram Page**
   -  **Facebook Page**
5. The automation ensures social media pages stay up-to-date without manual posting.

---

##  Tech Stack

| Layer | Technology Used |
|-------|------------------|
| **Frontend** | Tailwind CSS, HTML5, JavaScript |
| **Backend** | Django (Python) |
| **Database** | SQLite |
| **Cloud Hosting** | Cloudinary (for media) |
| **Automation** | Make (Integromat) + Cloudinary Webhooks |

---



##  Setup Instructions

###  Clone the Repository
```bash
git clone <repo-name>
cd ECOMMERCE
```
###  Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # on Windows
source venv/bin/activate # on macOS/Linux
```

### Install Dependencies
```
pip install -r requirements.txt
```

### switch to the working directory
```
cd .\postsync\
```

### Run the Development Server
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/
