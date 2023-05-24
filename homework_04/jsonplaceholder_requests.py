"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data(session):
    async with session.get(USERS_DATA_URL) as response:
        result = await response.json()
        return result


async def fetch_posts_data(session):
    async with session.get(POSTS_DATA_URL) as response:
        result = await response.json()
        return result
