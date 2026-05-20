# Phase 3 Part B — Database Setup, Migration, and First Run Verification

## Step 1 — Create PostgreSQL Database and User

```bash
psql -U postgres
```

```sql
CREATE USER cyber_admin WITH PASSWORD 'change_this_password';
CREATE DATABASE cybershield_academy OWNER cyber_admin;
GRANT ALL PRIVILEGES ON DATABASE cybershield_academy TO cyber_admin;
\q
```

## Step 2 — Create `.env` File

Create a `.env` file in the project root with exactly:

```env
FLASK_ENV=development
SECRET_KEY=replace_with_a_secure_random_key
DATABASE_URL=postgresql+psycopg2://cyber_admin:change_this_password@localhost:5432/cybershield_academy
MAIL_SERVER=
MAIL_PORT=587
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_USE_TLS=True
SESSION_COOKIE_SECURE=False
```

## Step 3 — Initialize Flask-Migrate

```bash
flask db init
```

## Step 4 — Generate First Migration

```bash
flask db migrate -m "initial schema: all tables"
```

## Step 5 — Apply Migration

```bash
flask db upgrade
```

## Step 6 — Verify Tables in PostgreSQL

```bash
psql -U cyber_admin -d cybershield_academy -c "\dt"
```

Expected table names:
- admins
- users
- lessons
- quizzes
- quiz_questions
- quiz_results
- phishing_examples
- activities
- user_lessons

---

## Troubleshooting (Top 5 Common Errors)

### 1) `SQLALCHEMY_DATABASE_URI` not set
**Exact error message:**
```text
RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set.
```
**Why this happens:** DATABASE_URL is missing or not loaded from `.env`.
**Exact fix:** Set `DATABASE_URL` in `.env`, ensure `load_dotenv()` is in `config.py`, then restart the app.

### 2) psycopg2 connection refused
**Exact error message:**
```text
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Connection refused
```
**Why this happens:** PostgreSQL server is not running or the host/port is incorrect.
**Exact fix:** Start PostgreSQL service, verify port 5432, and confirm `DATABASE_URL` credentials/host are correct.

### 3) ModuleNotFoundError on blueprint imports
**Exact error message:**
```text
ModuleNotFoundError: No module named 'app.blueprints.auth'
```
**Why this happens:** Missing package files (`__init__.py`) or incorrect import path.
**Exact fix:** Ensure each blueprint folder has `__init__.py`, verify import paths, and run from project root.

### 4) Flask-Migrate migration conflict
**Exact error message:**
```text
ERROR [flask_migrate] Error: Can't locate revision identified by '<revision_id>'
```
**Why this happens:** Migration history is out of sync with database state.
**Exact fix:** Confirm migration files exist, run `flask db stamp head` (if schema already exists), then re-run `flask db migrate` and `flask db upgrade`.

### 5) SECRET_KEY not set warning
**Exact error message:**
```text
WARNING: Using insecure fallback SECRET_KEY.
```
**Why this happens:** `SECRET_KEY` is empty and fallback value is being used.
**Exact fix:** Set a strong random `SECRET_KEY` in `.env` and restart the app.
