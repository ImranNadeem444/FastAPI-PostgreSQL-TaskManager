# TaskFlow API 🚀

A professional FastAPI backend project with JWT authentication, PostgreSQL integration, SQLAlchemy ORM, Alembic migrations, and secure multi-user task management.

---

# Features

✅ User Signup & Login  
✅ JWT Authentication  
✅ Password Hashing  
✅ PostgreSQL Database  
✅ SQLAlchemy ORM  
✅ Alembic Migrations  
✅ Protected Routes  
✅ Multi-User Authorization  
✅ Full CRUD Operations  
✅ Environment Variables (.env)  
✅ Swagger API Documentation  

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Pydantic
- Uvicorn

---

# Project Structure

```bash
TaskFlow-API/
│
├── alembic/
│
├── app/
│   ├── auth/
│   ├── crud/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
├── README.md
└── venv/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/taskflow-api.git
```

---

## Move Into Project Folder

```bash
cd taskflow-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create PostgreSQL database:

```sql
CREATE DATABASE taskflow_db;
```

---

# Environment Variables

Create `.env` file in project root:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost/taskflow_db

SECRET_KEY=your_super_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_HOURS=24
```

---

# Run Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | /signup | Register new user |
| POST | /login | User login |

---

## Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create task |
| GET | /tasks/{id} | Get single task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

---

# Security Features

- JWT Authentication
- Password Hashing
- Protected Routes
- User-Based Authorization
- Ownership-Based Access Control

---

# Skills Demonstrated

- Backend Development
- REST API Development
- FastAPI Framework
- PostgreSQL Integration
- SQLAlchemy ORM
- Authentication & Authorization
- Database Relationships
- Environment Variable Management
- API Documentation
- Secure Multi-User Architecture

---

# Future Improvements

- Docker Deployment
- CI/CD Integration
- Redis Caching
- Async FastAPI
- AI-Based Task Suggestions
- Frontend Integration

---

# Author

**Imran Nadeem**  
Computer Science Student | Backend Developer | AI Enthusiast

---