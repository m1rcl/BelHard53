from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import select, ForeignKey
from schema import *


engine = create_async_engine("sqlite+aiosqlite:///db//fastapi.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class UserOrm(Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    age: Mapped[int]
    phone: Mapped[str | None]
    # quizes: Mapped["QuizOrm"] = relationship(back_populates="user")


class QuizOrm(Model):
    __tablename__ = "quiz"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    user_id: Mapped[int]  # = mapped_column(ForeignKey("user.id"), index=True)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def add_test_data():
    async with new_session() as session:
        users = [
            UserOrm(name="user1", age=11),
            UserOrm(name="user2", age=22, phone="1234567"),
            UserOrm(name="user3", age=33),
        ]
        quizes = [
            QuizOrm(name="quiz1", user_id=1),
            QuizOrm(name="quiz2", user_id=1),
            QuizOrm(name="quiz3", user_id=2),
            QuizOrm(name="quiz4", user_id=2),
            QuizOrm(name="quiz5", user_id=3),
            QuizOrm(name="quiz6", user_id=3),
        ]
        session.add_all(users)
        session.add_all(quizes)
        await session.commit()


class UserRepository:

    @classmethod
    async def add_user(cls, user: UserAdd) -> int:
        async with new_session() as session:
            data = user.model_dump()
            user = UserOrm(**data)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with new_session() as session:
            query = select(UserOrm)
            res = await session.execute(query)
            users = res.scalars().all()
            return users

    @classmethod
    async def get_user(cls, id: int) -> UserOrm:
        async with new_session() as session:
            query = select(UserOrm).filter(UserOrm.id == id)
            res = await session.execute(query)
            user = res.scalars().first()
            return user


class QuizRepository:

    @classmethod
    async def add_quiz(cls, quiz: QuizAdd) -> int:
        async with new_session() as session:
            data = quiz.model_dump()
            quiz = QuizOrm(**data)
            session.add(quiz)
            await session.flush()
            await session.commit()
            return quiz.id

    @classmethod
    async def get_quizes(cls) -> list[QuizOrm]:
        async with new_session() as session:
            query = select(QuizOrm)
            res = await session.execute(query)
            quizes = res.scalars().all()
            return quizes

    @classmethod
    async def get_quiz(cls, id: int) -> QuizOrm:
        async with new_session() as session:
            query = select(QuizOrm).filter(QuizOrm.id == id)
            res = await session.execute(query)
            quiz = res.scalars().first()
            return quiz
