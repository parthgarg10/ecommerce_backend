# Django E-Commerce Backend

## Quick Setup (Step-by-step for beginners)

### Step 1 — Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### Step 2 — Install all packages
```bash
pip install -r requirements.txt
```

### Step 3 — Create your .env file
```bash
copy .env.example .env      # Windows
cp .env.example .env        # Mac/Linux
```
Then open `.env` and fill in your values.

### Step 4 — Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5 — Create an admin account
```bash
python manage.py createsuperuser
```

### Step 6 — Start the server
```bash
python manage.py runserver
```
Your backend is now running at: http://127.0.0.1:8000

---

## API Endpoints

### Auth
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/users/register/ | Register new user |
| POST | /api/users/login/ | Login → get JWT token |
| POST | /api/users/token/refresh/ | Refresh JWT token |
| GET/PUT | /api/users/profile/ | View/update profile |

### Products
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/products/ | List all products |
| GET | /api/products/?search=shirt | Search products |
| GET | /api/products/?category=1 | Filter by category |
| GET | /api/products/{slug}/ | Get single product |
| GET | /api/products/categories/ | List all categories |

### Cart
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/cart/ | View your cart |
| POST | /api/cart/add/ | Add item to cart |
| PATCH | /api/cart/update/{id}/ | Update quantity |
| DELETE | /api/cart/remove/{id}/ | Remove item |
| DELETE | /api/cart/clear/ | Clear entire cart |

### Orders
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/orders/ | Your order history |
| POST | /api/orders/create/ | Place new order |
| GET | /api/orders/{id}/ | Order details |

### Payments (Razorpay)
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/payments/create/ | Create payment |
| POST | /api/payments/verify/ | Verify payment |

---

## How to use JWT in frontend
After login, you get an `access` token. Send it with every request:
```javascript
headers: {
  'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}
```

## Django Admin
Visit http://127.0.0.1:8000/admin to manage products, orders, users visually.
