from datetime import datetime, timezone

from fastapi.testclient import TestClient

from app.db.session import get_db
from app.main import app


class FakeSession:
    def __init__(self):
        self.added = None
        self.committed = False

    def add(self, exercise):
        self.added = exercise

    async def commit(self):
        self.committed = True

    async def refresh(self, exercise):
        exercise.id = 1
        exercise.created_at = datetime(2026, 9, 3, tzinfo=timezone.utc)
        exercise.updated_at = datetime(2026, 9, 3, tzinfo=timezone.utc)


def test_create_exercise_persists_and_returns_exercise():
    session = FakeSession()

    async def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    try:
        response = TestClient(app).post(
            "/exercises",
            json={
                "name": "Bench press",
                "description": "Barbell chest press",
                "muscle_group": "chest",
                "sets": [
                    {
                        "id": "working-set",
                        "type": "working",
                        "reps": [{"weight": 100, "repititions": 5}],
                    }
                ],
            },
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "Bench press",
        "description": "Barbell chest press",
        "muscle_group": "chest",
        "sets": [
            {
                "id": "working-set",
                "type": "working",
                "reps": [{"weight": 100.0, "repititions": 5}],
            }
        ],
        "created_at": "2026-09-03T00:00:00Z",
        "updated_at": "2026-09-03T00:00:00Z",
    }
    assert session.committed is True
    assert session.added.name == "Bench press"
