from typing import Optional
from pydantic import BaseModel, EmailStr, ValidationError, field_validator
import json
import requests
class UserModel(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age must be greater than or equal to 0")
        return value
class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    completed: bool = False

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, value):
        allowed = ["low", "medium", "high"]
        if value.lower() not in allowed:
            raise ValueError(
                f"Priority must be one of: {', '.join(allowed)}"
            )
        return value.lower()
def create_task(data: dict) -> TaskModel:
    return TaskModel(**data)
def tasks_to_json(tasks: list[TaskModel]) -> str:
    return json.dumps(
        [task.model_dump() for task in tasks],
        indent=4
    )
class TodoAPIModel(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
if __name__ == "__main__":
    try:
        user = UserModel(
            name="Fidha",
            email="fidha@example.com",
            age=25
        )
        print("User Created:")
        print(user)
    except ValidationError as e:
        print(e)

    
    tasks = []

    task_data = {
        "title": "Learn Pydantic",
        "description": "Practice validation models",
        "priority": "high"
    }

    try:
        task = create_task(task_data)
        tasks.append(task)
        print("\nTask Created:")
        print(task)
    except ValidationError as e:
        print(e)

    
    try:
        json_output = tasks_to_json(tasks)
        print("\nTasks JSON:")
        print(json_output)
    except Exception as e:
        print(e)

    
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=5
        )

        response.raise_for_status()

        todo = TodoAPIModel(**response.json())

        print("\nParsed API Response:")
        print(todo)

    except (requests.RequestException, ValidationError) as e:
        print(e)