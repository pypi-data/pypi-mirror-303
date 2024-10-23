from fastapi.testclient import TestClient
from api.main import app
from lingustruct.license_manager import validate_api_key

client = TestClient(app)

HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": "your-license-key"
}

def test_generate_master():
    """Test the /lingu_struct/generate_master endpoint with mock data."""
    validate_api_key("your-license-key", test_mode=True)  # テストモードでのバリデーション
    payload = {"project_id": "test_project", "version": "1.0"}
    response = client.post("/lingu_struct/generate_master", json=payload, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error Response: {response.json()}")

    assert response.status_code == 200

def test_get_module():
    """Test the /lingu_struct/modules/{module_id} endpoint with mock data."""
    validate_api_key("your-license-key", test_mode=True)  # テストモードでのバリデーション
    response = client.get("/lingu_struct/modules/1", headers=HEADERS)

    if response.status_code != 200:
        print(f"Error Response: {response.json()}")

    assert response.status_code == 200

def test_rate_limit():
    """Test the rate limit with multiple requests."""
    validate_api_key("your-license-key", test_mode=True)  # テストモードでのバリデーション
    for _ in range(10):
        response = client.get("/lingu_struct/modules/1", headers=HEADERS)

    assert response.status_code in (200, 429), f"Unexpected status: {response.status_code}"
