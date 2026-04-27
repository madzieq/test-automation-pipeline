import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestPosts:

    def test_get_post_returns_200(self):
        """
        Test that GET /posts/{id} returns HTTP 200 OK.
        Verifies that the endpoint is reachable and responds successfully.
        """
        r = requests.get(f"{BASE_URL}/posts/1")
        assert r.status_code == 200

    def test_get_post_has_required_fields(self):
        """
        Test that a single post contains all required fields.
        Verifies that the response body includes: id, title, body, userId.
        """
        r = requests.get(f"{BASE_URL}/posts/1")
        data = r.json()
        assert "id" in data
        assert "title" in data
        assert "body" in data
        assert "userId" in data

    def test_get_all_posts_returns_list(self):
        """
        Test that GET /posts returns a list of 100 posts.
        Verifies that the response is a non-empty list with the expected number of items.
        """
        r = requests.get(f"{BASE_URL}/posts")
        data = r.json()
        assert isinstance(data, list)
        assert len(data) == 100

    def test_create_post_returns_201(self):
        """
        Test that POST /posts successfully creates a new post.
        Sends a valid payload and verifies that:
        - HTTP 201 Created is returned
        - the response contains the same title as sent in the request
        """
        payload = {"title": "Test post", "body": "Test body", "userId": 1}
        r = requests.post(f"{BASE_URL}/posts", json=payload)
        assert r.status_code == 201
        assert r.json()["title"] == "Test post"

    def test_delete_post_returns_200(self):
        """
        Test that DELETE /posts/{id} successfully deletes a post.
        Verifies that the endpoint returns HTTP 200 OK upon deletion.
        """
        r = requests.delete(f"{BASE_URL}/posts/1")
        assert r.status_code == 200