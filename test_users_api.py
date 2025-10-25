
---

### 📄 `tests/test_users_api.py`
```python
import pytest
import httpx

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.asyncio
async def test_get_users_list():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/users")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0


@pytest.mark.asyncio
async def test_get_single_user():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/users/1")
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert "username" in user


@pytest.mark.asyncio
async def test_create_post_negative():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        payload = {"wrong_field": "test"}
        response = await client.post("/posts", json=payload)
        # jsonplaceholder допускает POST-запросы, но мы проверим, что ответ корректен
        assert response.status_code in (201, 200)
