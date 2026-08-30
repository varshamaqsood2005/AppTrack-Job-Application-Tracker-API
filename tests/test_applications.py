def test_create_application(client):
    payload = {
        "company": "Tabby",
        "role": "Python Developer",
        "source": "referral",
        "status": "applied",
        "remote": True,
        "expected_salary": 5000,
        "applied_on": "2026-01-09"
    }
    response = client.post("/applications", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["company"] == "Tabby"

def test_get_application_by_id(client):
    payload = {
        "company": "Lean Technologies",
        "role": "Backend Engineer",
        "source": "linkedin",
        "status": "interview",
        "remote": True,
        "expected_salary": 5100,
        "applied_on": "2026-01-15"
    }
    create_res = client.post("/applications", json=payload)
    app_id = create_res.json()["id"]

    response = client.get(f"/applications/{app_id}")
    assert response.status_code == 200
    assert response.json()["role"] == "Backend Engineer"

def test_get_nonexistent_application(client):
    response = client.get("/applications/99999")
    assert response.status_code == 404

def test_patch_application_leaves_other_fields_unchanged(client):
    payload = {
        "company": "Unifonic",
        "role": "Senior Engineer",
        "source": "linkedin",
        "status": "applied",
        "notes": "Initial contact",
        "applied_on": "2026-01-18"
    }
    create_res = client.post("/applications", json=payload)
    app_id = create_res.json()["id"]

    # PATCH only the status
    patch_res = client.patch(f"/applications/{app_id}", json={"status": "interview"})
    assert patch_res.status_code == 200
    updated_data = patch_res.json()
    
    assert updated_data["status"] == "interview"
    assert updated_data["notes"] == "Initial contact"  # Ensure notes were not changed/cleared

def test_delete_application(client):
    payload = {
        "company": "Foodics",
        "role": "Python Engineer",
        "source": "linkedin",
        "applied_on": "2026-02-05"
    }
    create_res = client.post("/applications", json=payload)
    app_id = create_res.json()["id"]

    # Delete application
    del_res = client.delete(f"/applications/{app_id}")
    assert del_res.status_code == 204

    # Subsequent GET returns 404
    get_res = client.get(f"/applications/{app_id}")
    assert get_res.status_code == 404

def test_create_missing_required_field(client):
    payload = {
        "company": "Sary"
        # missing role, source, applied_on
    }
    response = client.post("/applications", json=payload)
    assert response.status_code == 422

def test_analytics_endpoints(client):
    # Seed a test application with offer status
    client.post("/applications", json={
        "company": "Test Co",
        "role": "Engineer",
        "source": "linkedin",
        "status": "offer",
        "applied_on": "2026-01-01"
    })

    res_counts = client.get("/applications/stats/status-counts")
    assert res_counts.status_code == 200
    assert "offer" in res_counts.json()

    res_rate = client.get("/applications/stats/conversion-rate")
    assert res_rate.status_code == 200
    assert "conversion_rate" in res_rate.json()