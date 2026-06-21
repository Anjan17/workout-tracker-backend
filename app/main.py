from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/exercises")
@app.get("/exercises/list")
async def get_exercises(offset: int = 0, limit: int = 100):
    return {
        "get exercises": {
            "offset": offset,
            "limit": limit,
        },
    }


@app.get("/exercises/{exercise_id}")
async def get_exercise_details(exercise_id: str):
    return {
        "get exercise": {
            "exercise_id": exercise_id,
        }
    }


@app.post("/exercises/{exercise_id}")
async def create_exercise(exercise_id: str):
    pass


@app.put("/exercises/{exercise_id}")
async def update_exercise(exercise_id: str):
    pass


@app.delete("/exercises/{exercise_id}")
async def delete_exercise(exercise_id: str):
    pass
