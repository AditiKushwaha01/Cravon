# 🍽️ Cravon

**Cravon** is a luxury-focused food delivery web application built using Django.
It aims to deliver a **premium, curated dining experience** rather than a typical discount-driven food app.

---

## 🚀 Features

* 🧾 **Curated Restaurant Listings**
  Only premium and high-quality restaurants are showcased.

* 🍔 **Dynamic Menu System**
  Browse dishes with pricing, descriptions, and categories.

* 🛒 **Cart & Order Management**
  Add items to cart and place orders seamlessly.

* 👤 **User Authentication**
  Secure login and signup functionality.

* ⚡ **Admin Dashboard**
  Manage restaurants, menus, and orders via Django admin.

* 💎 **Luxury UI Concept**
  Minimal, clean, and premium design approach.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS (Bootstrap/Tailwind optional)
* **Database:** SQLite (default, can be upgraded to PostgreSQL)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
cravon_project/
│
├── delivery/        # Main app (views, models, urls)
├── templates/       # HTML templates
├── static/          # CSS, JS, images
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/cravon.git
cd cravon
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```
python manage.py migrate
```

### 5️⃣ Start server

```
python manage.py runserver
```

👉 Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Access

Create superuser:

```
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin/
```

---

## 💡 Future Enhancements

* AI-based food recommendations
* Real-time order tracking
* Payment gateway integration
* Mobile app version
* Advanced filtering & search

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is for educational purposes.
You can modify and use it as needed open for collaboration also.

---

## ✨ Author

**Aditi Kushwaha**
GitHub: https://github.com/AditiKushwaha01

---

> *Cravon – Curated Cravings. Premium Experience.*
