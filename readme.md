
# 🧑‍💻 Developer Guide — Mechanical Store App

This guide will help you set up, run, and develop the Mechanical Store backend locally using Docker, FastAPI, and PostgreSQL.

## ⚙️ Local Development Setup

### ✅ Prerequisites

- Docker & Docker Compose installed
- Git
- Python 3.10+ (if not using Docker for local testing)
- Optional: `httpie` or `curl` for API testing

## 🗂️ Project Structure

```
mechanic_store/
├── app/
│   ├── api/v1/               # API routes
│   ├── core/                 # App config, JWT, security
│   ├── models/               # DB models
│   ├── schemas/              # Request/response validation
│   ├── services/             # Business logic (auth, booking)
│   └── database.py           # Database session
├── Dockerfile
├── docker-compose.yml
├── .env                      # Local environment variables
├── .gitignore
├── README.md                 # General user-facing guide
├── README.dev.md             # This developer guide
└── requirements.txt
```

## 🔐 Environment Setup

Create `.env` in the root directory:

```bash
cp .env.example .env
```

### Example `.env` file:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=your_db_name
DATABASE_URL=your_db_URl
SECRET_KEY=user_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=user_time
```

## 🐳 Docker Workflow

### 🔧 Build & Start Project

```bash
docker-compose up --build
```

### 💡 Restart with updated code

```bash
docker-compose down
docker-compose up --build
```

## 🌐 URLs

| Service         | URL                            |
|-----------------|---------------------------------|
| Swagger Docs    | `http://localhost:8000/docs`   |
| ReDoc           | `http://localhost:8000/redoc`  |
| DB Host (Docker)| `db` (from within the app)     |
| DB Host (local) | `localhost:5432`               |

## 🧪 Testing APIs (Manual)

### 1. Register Admin/User

```bash
POST /api/v1/auth/register
```

```json
{
  "name": "Admin",
  "email": "admin@example.com",
  "password": "admin123",
  "role": "admin"
}
```

### 2. Login

```bash
POST /api/v1/auth/login
```

```json
{
  "email": "admin@example.com",
  "password": "admin123"
}
```

Returns a JWT `access_token`.

### 3. Authenticated Request

```bash
GET /api/v1/users/
Authorization: Bearer <access_token>
```

## 🧰 Useful Docker Commands

```bash
# Check logs
docker-compose logs

# Stop services
docker-compose down

# Rebuild only backend
docker-compose build backend
```

## 📥 Connect to DB via psql or PgAdmin

**Credentials from `.env`:**

- Host: `localhost`
- Port: `5432`
- User: `postgres`
- Password: `postgres`
- DB: `mechanic_db`

## 🧪 Unit Testing (optional)

To run tests (if added):

```bash
docker exec -it mechanic_backend pytest
```

Or add a `tests/` directory and include:

```bash
pytest tests/
```

## 🗓️ Next Steps for Devs

- [ ] Add Alembic for migrations
- [ ] Write unit/integration tests
- [ ] Seed DB with sample vehicles/services
- [ ] Add logging and exception middleware
- [ ] Hook into frontend or mobile app
