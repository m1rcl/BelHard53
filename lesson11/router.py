from fastapi import APIRouter
from schema import *
from fastapi import FastAPI, Depends
from database import UserRepository, QuizRepository


user_router = APIRouter(prefix="/api", tags=["users"])
quiz_router = APIRouter(prefix="/api", tags=["quizes"])


@user_router.post("/users/")
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepository.add_user(user)
    return {"id": id}


@user_router.get("/users/")
async def get_users() -> list[User]:
    users = await UserRepository.get_users()
    return users


@user_router.get("/users/{user_id}/")
async def get_user(user_id: int) -> User:
    user = await UserRepository.get_user(id=user_id)
    return user


@quiz_router.post("/quizes/")
async def add_quiz(quiz: QuizAdd = Depends()) -> QuizId:
    id = await QuizRepository.add_quiz(quiz)
    return {"id": id}


@quiz_router.get("/quizes/")
async def get_quizes() -> list[Quiz]:
    quizes = await QuizRepository.get_quizes()
    return quizes


@quiz_router.get("/quizes/{quiz_id}/")
async def get_quiz(quiz_id: int) -> Quiz:
    quiz = await QuizRepository.get_quiz(id=quiz_id)
    return quiz
