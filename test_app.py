from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_echo():
    response = client.get(
        '/echo',
        params={"param": "test"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": "test"}


def test_echo2():
    response = client.get(
        '/echo',
        params={"param": "test2"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": "test"}


def test_scrape():
    response = client.get(
        '/scrape/prices',
        params={"product": "iphone"},
    )
    assert response.status_code == 200
