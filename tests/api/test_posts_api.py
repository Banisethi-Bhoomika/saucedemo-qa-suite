"""API tests against the free JSONPlaceholder service (no API key needed)."""
import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_get_single_post_schema():
    r = requests.get(f"{BASE}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"userId", "id", "title", "body"}
    assert body["id"] == 1


def test_list_posts_returns_100():
    r = requests.get(f"{BASE}/posts", timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) == 100


def test_filter_posts_by_user():
    r = requests.get(f"{BASE}/posts", params={"userId": 1}, timeout=TIMEOUT)
    assert r.status_code == 200
    posts = r.json()
    assert posts and all(p["userId"] == 1 for p in posts)


def test_create_post_echoes_payload():
    payload = {"title": "qa test", "body": "hello", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body


@pytest.mark.negative
def test_missing_post_returns_404():
    r = requests.get(f"{BASE}/posts/99999", timeout=TIMEOUT)
    assert r.status_code == 404


def test_comments_belong_to_post():
    r = requests.get(f"{BASE}/posts/1/comments", timeout=TIMEOUT)
    assert r.status_code == 200
    assert all(c["postId"] == 1 for c in r.json())
