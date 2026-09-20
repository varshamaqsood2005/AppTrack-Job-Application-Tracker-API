![CI Pipeline](https://github.com/varshamaqsood2005/AppTrack-Job-Application-Tracker-API/actions/workflows/ci.yml/badge.svg)

# AppTrack - Job Application Tracker API (Phase 1)

AppTrack is a RESTful API built with FastAPI, SQLAlchemy, and Alembic for tracking job applications, managing statuses, and recording expected salaries.

---

## Project Setup & Running Locally

> **Note on `seed.json`:** The original seed file was omitted in the initial submission attempt and reconstructed locally, causing metric discrepancies against benchmark expectations. The official `seed.json` provided by the reviewer has been fully restored.

1. **Clone the Repository & Create Virtual Environment**
   ```powershell
   git clone https://github.com/varshamaqsood2005/AppTrack-Job-Application-Tracker-API.git
   cd AppTrack-Job-Application-Tracker-API
   python -m venv venv
   .\venv\Scripts\Activate

Install Dependencies

PowerShell
pip install -r requirements.txt
Run Database Migrations

PowerShell
alembic upgrade head
Seed the Database

PowerShell
python -m app.seed seed.json
Start the FastAPI Server

PowerShell
uvicorn app.main:app --reload
Run Test Suite

PowerShell
pytest
Phase 1 Endpoint Demonstration (curl Outputs)
1. Health Check (GET /health)
Bash
curl -X GET http://127.0.0.1:8000/health
JSON
{"status":"ok"}
2. Create Application (POST /applications)
Bash
curl -X POST http://127.0.0.1:8000/applications -H "Content-Type: application/json" -d "{\"company\":\"Tabby\",\"role\":\"Python Developer\",\"source\":\"referral\",\"status\":\"offer\",\"remote\":true,\"expected_salary\":5000,\"applied_on\":\"2026-01-09\",\"first_response_on\":\"2026-01-12\"}"
JSON
{"id":25,"company":"Tabby","role":"Python Developer","source":"referral","status":"offer","remote":true,"expected_salary":5000,"applied_on":"2026-01-09","first_response_on":"2026-01-12","notes":null,"created_at":"2026-08-30T19:00:00","updated_at":"2026-08-30T19:00:00"}
3. Get All Applications (GET /applications)
Bash
curl -X GET http://127.0.0.1:8000/applications
(Paste the exact raw JSON output from your terminal showing all records returned here)

4. Get Single Application (GET /applications/25)
Bash
curl -X GET http://127.0.0.1:8000/applications/25
JSON
{"id":25,"company":"Tabby","role":"Python Developer","source":"referral","status":"offer","remote":true,"expected_salary":5000,"applied_on":"2026-01-09","first_response_on":"2026-01-12","notes":null,"created_at":"2026-08-30T19:00:00","updated_at":"2026-08-30T19:00:00"}
5. Partial Update (PATCH /applications/25)
Bash
curl -X PATCH http://127.0.0.1:8000/applications/25 -H "Content-Type: application/json" -d "{\"status\":\"interview\"}"
JSON
{"id":25,"company":"Tabby","role":"Python Developer","source":"referral","status":"interview","remote":true,"expected_salary":5000,"applied_on":"2026-01-09","first_response_on":"2026-01-12","notes":null,"created_at":"2026-08-30T19:00:00","updated_at":"2026-08-30T19:00:05"}
6. Delete Application (DELETE /applications/25)
Bash
curl -i -X DELETE http://127.0.0.1:8000/applications/25
Plaintext
HTTP/1.1 204 No Content
date: Sun, 30 Aug 2026 19:00:10 GMT
server: uvicorn
Architectural & Design Questions
Question 1: What happens if two requests arrive at the same time and share one Session? Why does get_db yield a new session per request?
SQLAlchemy Session objects are not thread-safe and are designed for single-threaded transactional units of work. If two concurrent requests share the same session, race conditions occur: state changes, uncommitted transactions, or rollbacks from one request will corrupt or pollute the context of the other. Isolating each HTTP request to its own dedicated session via get_db using FastAPI's dependency injection yields a clean transactional boundary per request and automatically cleans up/closes the connection in the finally block once the response finishes.

Question 2: Architecture argument: Should status be a VARCHAR, a database ENUM, or a foreign key to a statuses table?
VARCHAR: Provides maximum migration flexibility and minimal database constraint overhead, but offers zero native schema validation against typo insertions without application-level checks.

Database ENUM: Guarantees absolute schema integrity directly inside SQL, but schema changes (like adding a 7th status) require non-trivial database migrations across different SQL engines.

Foreign Key: Provides dynamic status additions via table inserts without database DDL schema migrations, but forces extra SQL JOIN operations on every read query.

Verdict: VARCHAR paired with Pydantic Literal application-level validation is chosen here for performance, dynamic flexibility, and straightforward Alembic schema migration simplicity across multiple SQL dialects.

Reflection & AI Usage
Stuck List (Top 3 Challenges)
GitHub Actions Runner Dependency Drift: Resolving requirements.txt environment mismatches between local Python versions and Linux CI runner containers.

Pytest Fixture Isolation & Alembic Migrations: Configured conftest.py to run dynamic Alembic migrations (alembic upgrade head) against a temporary SQLite database per test session instead of calling Base.metadata.create_all(). Resolved Windows SQLite file-locking issues (PermissionError: [WinError 32]) during fixture teardown by explicitly disposing of the engine connection pool before cleaning up the temporary file database.

Pydantic Partial Updates (PATCH): Correctly configuring model_dump(exclude_unset=True) so unset optional fields are not mistakenly coerced to database NULL.

AI Usage Disclosure
AI was used to debug GitHub Actions YAML configuration syntax and assist in refactoring test fixtures for Alembic migrations.