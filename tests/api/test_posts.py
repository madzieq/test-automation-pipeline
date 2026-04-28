import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestPosts:

    # Parametrized: different post IDs are used to verify that the endpoint
    # works correctly across the full range of available posts (first, middle, last).
    # Hardcoding a single ID would only prove the endpoint works for one case.
    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_returns_200(self, post_id):
        """
        Test that GET /posts/{id} returns HTTP 200 OK for multiple valid post IDs.
        Verifies that the endpoint is reachable and responds successfully.
        """
        r = requests.get(f"{BASE_URL}/posts/{post_id}")
        assert r.status_code == 200

    # Not parametrized: we are testing the response structure, not the range of IDs.
    # The fields (id, title, body, userId) are the same for every post,
    # so a single representative post (ID=1) is sufficient.
    def test_get_post_has_required_fields(self):
        """
        Test that a single post contains all required fields.
        Verifies that the response body includes: id, title, body, userId.
        A specific post (ID=1) is used as a representative example.
        """
        r = requests.get(f"{BASE_URL}/posts/1")
        data = r.json()
        assert "id" in data
        assert "title" in data
        assert "body" in data
        assert "userId" in data

    # Not parametrized: we are verifying a fixed business rule —
    # the API always returns exactly 100 posts.
    # There are no variable inputs to test here.
    def test_get_all_posts_returns_list(self):
        """
        Test that GET /posts returns a list of 100 posts.
        Verifies that the response is a non-empty list with the expected number of items.
        """
        r = requests.get(f"{BASE_URL}/posts")
        data = r.json()
        assert isinstance(data, list)
        assert len(data) == 100

    # Parametrized: different payloads are used to verify that post creation
    # works correctly for different users and content.
    # This ensures the endpoint is not tied to a single hardcoded input.
    @pytest.mark.parametrize("payload", [
        {"title": "Test post", "body": "Test body", "userId": 1},
        {"title": "Another post", "body": "Another body", "userId": 2},
    ])
    def test_create_post_returns_201(self, payload):
        """
        Test that POST /posts successfully creates a new post for different payloads.
        Verifies that:
        - HTTP 201 Created is returned
        - the response contains the same title as sent in the request
        """
        r = requests.post(f"{BASE_URL}/posts", json=payload)
        assert r.status_code == 201
        assert r.json()["title"] == payload["title"]

    # Not parametrized: this test verifies a single, well-defined behaviour —
    # that DELETE returns HTTP 200 OK. The JSONPlaceholder API always returns 200
    # regardless of the post ID, so testing multiple IDs would add no value.
    def test_delete_post_returns_200(self):
        """
        Test that DELETE /posts/{id} successfully deletes a post.
        Verifies that the endpoint returns HTTP 200 OK upon deletion.
        A specific post (ID=1) is used as a representative example.
        """
        r = requests.delete(f"{BASE_URL}/posts/1")
        assert r.status_code == 200