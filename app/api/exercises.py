from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate, ExerciseRead

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


@router.post("", response_model=ExerciseRead, status_code=status.HTTP_201_CREATED)
async def create_exercise(
    exercise: ExerciseCreate,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    db_exercise = Exercise(**exercise.model_dump(mode="json"))
    db.add(db_exercise)
    await db.commit()
    await db.refresh(db_exercise)
    return db_exercise


@router.put("/{exercise_id}")
async def update_exercise(exercise_id: str):
    pass


@router.delete("/{exercise_id}")
async def delete_exercise(exercise_id: str):
    pass
