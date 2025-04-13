from tests.conftest import HEADERS


def test_invalid_x_token(client):
    """
    Test if it the endpoint is invalid without the token
    """
    response = client.get("/foos", params={"name": "Test Foo"})
    assert response.status_code == 422


def test_add_foo(client):
    """
    Tests if the foos are being added to the database
    """

    response = client.post("/foo", json={"name": "Test Foo"}, headers=HEADERS)
    data = response.json()

    # validates if the request was successfull
    assert response.status_code == 201

    print(data)

    # validates the saved record
    assert "name" in data


def test_get_foo(client):
    """
    Tests if the foos get request is successfull
    """

    response = client.get("/foos", headers=HEADERS)

    id = response.json()[-1]["id"]

    # validates if the request was successfull
    assert response.status_code == 200


def test_add_invalid_sneaker(client):
    """
    Tests if it validates the inavlid payload
    """

    invalid_payload = {}

    response = client.post("/foo", json=invalid_payload, headers=HEADERS)

    # validates if the request was invalid because of inappropriate data
    assert response.status_code == 422
