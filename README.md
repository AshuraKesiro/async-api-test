# Async API Tests

Пример асинхронных автотестов для проверки REST API.  
Используется стек: **pytest**, **pytest-asyncio**, **httpx**.

Тесты обращаются к открытому API `jsonplaceholder.typicode.com`, чтобы показать структуру и принципы написания асинхронных тестов.

## Как запустить

```bash
pip install -r requirements.txt
pytest -v
