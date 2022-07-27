from fastapi.testclient import TestClient

from application import app


client = TestClient(app)


def test_read_home():
    response = client.get("/weather/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_put_home():
    response = client.put("/weather/")
    assert response.status_code == 405
    assert response.json() == {
	"detail": "Method Not Allowed"
}


def test_post_empty():
    response = client.post("/weather/")
    assert response.status_code == 422
    
    
def test_read_weather_list():
    response = client.get("/weather/list/")
    assert response.status_code == 200
    
    
def test_read_weather_post():
    response = client.post("/weather/",
        json = {"city_id" : "3439525"})
    assert response.status_code == 200
    

def test_read_weather_typing_post():
    response = client.post("/weather/",
        json = {"city_id" : 3439525})
    assert response.status_code == 200


def test_read_weather_wrong_post():
    response = client.post("/weather/",
        json = {"city.id" : 3439525})
    assert response.status_code == 422