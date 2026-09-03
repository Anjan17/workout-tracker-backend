from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


SetType = str


class Reps(BaseModel):
    weight: float
    repititions: int


class ExerciseSet(BaseModel):
    id: str
    type: SetType
    reps: List[Reps]


class ExerciseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    muscle_group: Optional[str] = None
    sets: List[ExerciseSet]


class ExerciseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    muscle_group: Optional[str] = None
    sets: Optional[List[ExerciseSet]] = None


class ExerciseRead(BaseModel):
    id: int
    name: str
    description: Optional[str]
    muscle_group: Optional[str]
    sets: List[ExerciseSet]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
