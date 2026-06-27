from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ExerciseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    muscle_group: Optional[str] = None


class ExerciseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    muscle_group: Optional[str] = None


class ExerciseRead(BaseModel):
    id: int
    name: str
    description: Optional[str]
    muscle_group: Optional[str]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
