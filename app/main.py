from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from app.api.exercises import router as exercises_router

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)


@app.get("/")
async def root():
    return {"message": "Welcome to Hitup app !"}


app.include_router(exercises_router)
