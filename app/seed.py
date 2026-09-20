from datetime import datetime
import json
import sys
from pathlib import Path
from sqlalchemy import select
from app.db import SessionLocal
from app.models import Application

def seed_data(filepath: str):
    file_path = Path(filepath)

    # Check if the path exists AND is a regular file (rejects directories)
    if not file_path.is_file():
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error: Malformed JSON file.", file=sys.stderr)
        sys.exit(1)

    db = SessionLocal()
    inserted = 0
    skipped = 0

    try:
        for item in data:
            # Check duplicate by (company, role) to enforce idempotency
            stmt = select(Application).where(
                Application.company == item["company"],
                Application.role == item["role"]
            )
            if db.scalar(stmt):
                skipped += 1
                continue

            applied_on = datetime.strptime(item["applied_on"], "%Y-%m-%d").date()
            first_response = (
                datetime.strptime(item["first_response_on"], "%Y-%m-%d").date()
                if item.get("first_response_on")
                else None
            )

            app_obj = Application(
                company=item["company"],
                role=item["role"],
                source=item["source"],
                status=item["status"],
                remote=item["remote"],
                expected_salary=item.get("expected_salary"),
                applied_on=applied_on,
                first_response_on=first_response,
            )
            db.add(app_obj)
            inserted += 1

        db.commit()
        print(f"seeded {inserted} applications ({skipped} skipped).")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m app.seed <path_to_json>", file=sys.stderr)
        sys.exit(1)
    seed_data(sys.argv[1])