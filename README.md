# ORM in Django

This project demonstrates the use of **Object-Relational Mapping (ORM)** in Django — exploring database models, queries, and relationships — created as part of a university seminar on *Advanced Data and Information Management Technologies*.

## 📖 Overview
The project is a practical implementation of Django ORM concepts, based on hands-on coding practice and inspired by the Django full course by **Mosh Hamedani**.  
It serves as both an academic exercise and a personal learning project to deepen understanding of how Django handles data persistence and database abstraction.

## 🛠️ Technologies Used
- **Python 3.9+**
- **Django** (latest version used in the course)
- **SQLite3** (default Django database) — managed and visualized using **DataGrip**
- HTML/CSS (for basic template rendering)

## ✨ Features
- Creating and managing Django models
- Defining fields and model relationships:
  - One-to-One
  - One-to-Many
  - Many-to-Many
- Performing CRUD operations via ORM
- QuerySets and filtering data
- Using Django Admin to manage records
- Applying migrations for schema changes
- Managing database schema and data using DataGrip

## 🚀 How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/rafifma/orm-django.git
   cd orm-django
2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Run migrations**
    ```bash
    python manage.py migrate
5. **Start development server**
    ```bash
    python manage.py runserver
6. **Access App**
    Open your browser and go to: http://localhost:8000

## 🎯 Purpose
This repository was built for:

Demonstrating Django ORM in an academic seminar

Practicing advanced data and information management concepts

Building a foundation for more complex Django applications

Note: This is a learning project and may not represent production-level code.