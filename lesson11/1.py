"""
Доделать в проекте FastAPI следующие ендпоинты:
    - /users/id - get
    - /quizes - get, post
    - /quizes/id - get
    
    
    
"""

from fastapi import FastAPI
from schema import *
from contextlib import asynccontextmanager
from database import create_tables, delete_tables, add_test_data
from router import user_router, quiz_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await add_test_data()
    print("------Bases build-------------")
    yield
    await delete_tables()
    print("-------------Bases droped------------")


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(quiz_router)
