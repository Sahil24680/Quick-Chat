# 💬 Quick Chat

**Quick Chat** is a Django-based real-time chat application that allows users to communicate instantly. With a focus on simplicity and performance, Quick Chat provides a seamless messaging experience.

---

## 🚀 Features

- 🧑‍🤝‍🧑 User registration and authentication
- 💬 Real-time messaging between users
- 🕵️‍♂️ Search functionality to find friends by name or username
- 🔒 Privacy controls for user information
- 📁 Profile customization with personal information

---

## 🛠 Tech Stack

| Tool / Tech | Purpose                          |
|-------------|----------------------------------|
| Python      | Core programming language        |
| Django      | Web framework for backend        |
| HTML/CSS    | Frontend structure and styling   |
| JavaScript  | Frontend interactivity           |
| SQLite      | Database for storing user data   |

---

## 📁 Folder Structure

```
Quick-Chat/
├── chat/                   # Handles chat functionalities
│   ├── migrations/         # Database migrations for chat app
│   ├── templates/          # HTML templates for chat
│   ├── static/             # Static files (CSS, JS) for chat
│   ├── admin.py            # Admin configurations for chat
│   ├── apps.py             # App configuration for chat
│   ├── models.py           # Database models for chat
│   ├── tests.py            # Test cases for chat
│   ├── urls.py             # URL routing for chat
│   └── views.py            # View functions for chat
├── media/                  # Uploaded media files
├── Quick-Chat/             # Project configuration directory
│   ├── __init__.py         # Package initialization
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL routing
│   └── wsgi.py             # WSGI configuration
├── db.sqlite3              # SQLite database file
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```
git clone https://github.com/Sahil24680/Quick-Chat.git
cd Quick-Chat
```

### 2. Set Up the Virtual Environment

```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py migrate
```

### 5. Run the Development Server

```
python manage.py runserver
```

### 6. Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

---


