import pytest
from application import create_app


class TestApplication:
    @pytest.fixture
    def client(self):
        app = create_app("config.MockConfig")
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Matheus",
            "last_name": "Schwertz",
            "cpf": "037.073.010-01",
            "email": "matheusschwertz@gmail.com",
            "birth_date": "1999-09-10",
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Matheus",
            "last_name": "Schwertz",
            "cpf": "037.073.010-35",
            "email": "matheusschwertz@gmail.com",
            "birth_date": "1999-09-10",
        }

    def test_get_users(self, client):
        response = client.get("/users")
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post("/user", json=valid_user)
        assert response.status_code == 200
        assert b"successfuly" in response.data

        response = client.post("/user", json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get("/user/%s" % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Matheus"
        assert response.json[0]["last_name"] == "Schwertz"
        assert response.json[0]["cpf"] == "037.073.010-01"
        assert response.json[0]["email"] == "matheusschwertz@gmail.com"

        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "1999-09-10T00:00:00Z"

        response = client.get("/user/%s" % invalid_user["cpf"])
        assert response.status_code == 400
        assert b"User does not exist in database!" in response.data

    def test_patch_user(self, client, valid_user):
        valid_user["first_name"] = "Matheuss"
        response = client.patch("/user", json=valid_user)
        assert response.status_code == 200
        assert b"updated" in response.data

        valid_user["cpf"] = "812.886.411-41"
        response = client.patch("/user", json=valid_user)
        assert response.status_code == 400
        assert b"does not exist in database" in response.data

    def test_delete_user(self, client, valid_user):
        response = client.delete("/user/%s" % valid_user["cpf"])
        assert response.status_code == 200
        assert b"deleted" in response.data

        response = client.delete("/user/%s" % valid_user["cpf"])
        assert response.status_code == 400
        assert b"does not exist" in response.data
