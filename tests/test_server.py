from fastapi.testclient import TestClient
from researchx.server import app

client = TestClient(app)

def test_server_dashboard_root():
    res = client.get("/")
    assert res.status_code == 200
    assert "ResearchX" in res.text

def test_server_healthz():
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_server_readyz():
    res = client.get("/readyz")
    assert res.status_code == 200
    assert res.json()["analyst_agents_active"] == 3

def test_server_generate_report_api():
    payload = {
        "topic_id": "RES-API-01",
        "query": "Autonomous Agent Market Ingestion",
        "sector": "TECHNOLOGY",
        "depth": "INSTITUTIONAL_DEEP_DIVE",
        "time_horizon": "2026 - 2030"
    }
    res = client.post("/api/v1/research/generate-report", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["overall_confidence_score"] >= 0.90
    assert len(data["verifiable_citations"]) >= 3
