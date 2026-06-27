from fastapi import APIRouter

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("")
@router.get("/list")
async def get_exercises(offset: int = 0, limit: int = 100):
    return {
        "get exercises": {
            "offset": offset,
            "limit": limit,
        },
    }


@router.get("/{exercise_id}")
async def get_exercise_details(exercise_id: str):
    return {
        "get exercise": {
            "exercise_id": exercise_id,
        }
    }


@router.post("/{exercise_id}")
async def create_exercise(exercise_id: str):
    pass


@router.put("/{exercise_id}")
async def update_exercise(exercise_id: str):
    pass


@router.delete("/{exercise_id}")
async def delete_exercise(exercise_id: str):
    pass
