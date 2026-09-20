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
(venv) PS C:\Users\Alsaudia\Downloads\AppTrack Job Application Tracker API> curl.exe -X GET http://127.0.0.1:8000/applications
[{"company":"Tabby","role":"Python Developer","source":"referral","status":"offer","remote":true,"expected_salary":5000,"applied_on":"2026-01-09","first_response_on":"2026-01-12","notes":null,"id":1,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Unifonic","role":"Backend Engineer","source":"linkedin","status":"interview","remote":true,"expected_salary":5200,"applied_on":"2026-01-15","first_response_on":"2026-01-20","notes":null,"id":2,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Lean Technologies","role":"Software Engineer","source":"company_site","status":"interview","remote":true,"expected_salary":5100,"applied_on":"2026-01-20","first_response_on":"2026-01-25","notes":null,"id":3,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Sary","role":"Python Developer","source":"recruiter","status":"screening","remote":false,"expected_salary":4200,"applied_on":"2026-02-01","first_response_on":"2026-02-05","notes":null,"id":4,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Tamara","role":"Backend Developer","source":"linkedin","status":"offer","remote":true,"expected_salary":4800,"applied_on":"2026-02-05","first_response_on":"2026-02-08","notes":null,"id":5,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Foodics","role":"Software Engineer","source":"referral","status":"interview","remote":true,"expected_salary":4600,"applied_on":"2026-02-10","first_response_on":"2026-02-18","notes":null,"id":6,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Jahez","role":"Python Engineer","source":"company_site","status":"interview","remote":false,"expected_salary":4000,"applied_on":"2026-02-12","first_response_on":"2026-02-26","notes":null,"id":7,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Floward","role":"Backend Developer","source":"linkedin","status":"screening","remote":true,"expected_salary":4300,"applied_on":"2026-02-15","first_response_on":"2026-02-20","notes":null,"id":8,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Nana","role":"Software Developer","source":"recruiter","status":"screening","remote":false,"expected_salary":3800,"applied_on":"2026-02-18","first_response_on":"2026-02-22","notes":null,"id":9,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"TruKKer","role":"Python Developer","source":"linkedin","status":"applied","remote":true,"expected_salary":4500,"applied_on":"2026-03-02","first_response_on":null,"notes":null,"id":10,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Fetchr","role":"Backend Engineer","source":"company_site","status":"applied","remote":false,"expected_salary":3900,"applied_on":"2026-03-05","first_response_on":null,"notes":null,"id":11,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Swvl","role":"Software Engineer","source":"linkedin","status":"applied","remote":true,"expected_salary":4700,"applied_on":"2026-03-10","first_response_on":null,"notes":null,"id":12,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Trella","role":"Python Developer","source":"referral","status":"applied","remote":true,"expected_salary":4400,"applied_on":"2026-03-12","first_response_on":null,"notes":null,"id":13,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Paymob","role":"Backend Engineer","source":"recruiter","status":"applied","remote":true,"expected_salary":4600,"applied_on":"2026-03-15","first_response_on":null,"notes":null,"id":14,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"MaxAB","role":"Software Developer","source":"linkedin","status":"applied","remote":false,"expected_salary":3700,"applied_on":"2026-03-18","first_response_on":null,"notes":null,"id":15,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Bosta","role":"Python Engineer","source":"company_site","status":"rejected","remote":true,"expected_salary":4100,"applied_on":"2026-01-10","first_response_on":"2026-01-14","notes":null,"id":16,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Yassir","role":"Backend Developer","source":"linkedin","status":"rejected","remote":true,"expected_salary":4300,"applied_on":"2026-01-18","first_response_on":"2026-01-22","notes":null,"id":17,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Vazeer","role":"Software Engineer","source":"referral","status":"rejected","remote":false,"expected_salary":3600,"applied_on":"2026-01-22","first_response_on":"2026-01-28","notes":null,"id":18,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Breadfast","role":"Python Developer","source":"recruiter","status":"rejected","remote":true,"expected_salary":4200,"applied_on":"2026-01-28","first_response_on":"2026-02-02","notes":null,"id":19,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Kashat","role":"Backend Engineer","source":"linkedin","status":"rejected","remote":false,"expected_salary":3500,"applied_on":"2026-02-02","first_response_on":"2026-02-08","notes":null,"id":20,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Rabbit","role":"Software Developer","source":"company_site","status":"rejected","remote":true,"expected_salary":4000,"applied_on":"2026-02-08","first_response_on":"2026-02-14","notes":null,"id":21,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"MNT-Halan","role":"Python Engineer","source":"linkedin","status":"rejected","remote":false,"expected_salary":3900,"applied_on":"2026-02-14","first_response_on":"2026-02-20","notes":null,"id":22,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Homzmart","role":"Backend Developer","source":"referral","status":"withdrawn","remote":true,"expected_salary":4500,"applied_on":"2026-01-25","first_response_on":"2026-01-30","notes":null,"id":23,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"},{"company":"Capiter","role":"Software Engineer","source":"linkedin","status":"withdrawn","remote":false,"expected_salary":3700,"applied_on":"2026-02-20","first_response_on":"2026-02-25","notes":null,"id":24,"created_at":"2026-09-20T11:34:34","updated_at":"2026-09-20T11:34:34"}]

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