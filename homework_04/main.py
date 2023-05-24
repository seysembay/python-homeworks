"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import aiohttp
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import User, Post, engine, Session, Base


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session, users):
    data = []
    for user in users:
        data.append(User(id=user.get('id'),
                         name=user.get('name'),
                         username=user.get('username'),
                         email=user.get('email'),
                         )
                    )
    session.add_all(data)
    await session.commit()


async def create_posts(session, posts):
    data = []
    for post in posts:
        data.append(Post(id=post.get('id'),
                         title=post.get('title'),
                         body=post.get('body'),
                         user_id=post.get('userId'),
                         )
                    )
        session.add_all(data)
    await session.commit()


async def async_main():
    async with aiohttp.ClientSession() as session:
        users, posts = await asyncio.gather(
            fetch_users_data(session),
            fetch_posts_data(session)
        )
        await create_database()

        async with Session() as session:
            await create_users(session, users)
            await create_posts(session, posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
