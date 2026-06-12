from typing import Dict, List
class TaskError(Exception):
    """Base exception for task errors."""
    pass
class TaskNotFoundError(TaskError):
    """Raised when a task is not found."""
    pass
class InvalidTaskDataError(TaskError):
    """Raised when task data is invalid."""
    pass
tasks: dict[int, dict] = {}
next_id: int = 1
def get_all_tasks() -> List[dict]:
    """Return all tasks."""
    return list(tasks.values())


def get_task(id: int) -> dict:
    """Return one task by ID."""
    if id not in tasks:
        raise TaskNotFoundError(f"Task with ID {id} not found.")
    return tasks[id]


def create_task(data: dict) -> dict:
    """Create a new task."""
    global next_id

    if "title" not in data or not data["title"].strip():
        raise InvalidTaskDataError("Title is required.")

    task = {
        "id": next_id,
        "title": data["title"],
        "completed": data.get("completed", False)
    }

    tasks[next_id] = task
    next_id += 1

    return task


def update_task(id: int, data: dict) -> dict:
    """Update an existing task."""
    if id not in tasks:
        raise TaskNotFoundError(f"Task with ID {id} not found.")

    task = tasks[id]

    if "title" in data:
        if not data["title"].strip():
            raise InvalidTaskDataError("Title cannot be empty.")
        task["title"] = data["title"]

    if "completed" in data:
        task["completed"] = data["completed"]

    return task


def delete_task(id: int) -> bool:
    """Delete a task."""
    if id not in tasks:
        raise TaskNotFoundError(f"Task with ID {id} not found.")

    del tasks[id]
    return True

def menu() -> None:
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. View All Tasks")
        print("2. View Task By ID")
        print("3. Create Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                all_tasks = get_all_tasks()

                if not all_tasks:
                    print("No tasks found.")
                else:
                    for task in all_tasks:
                        print(task)

            elif choice == "2":
                task_id = int(input("Enter task ID: "))
                print(get_task(task_id))

            elif choice == "3":
                title = input("Enter task title: ")

                task = create_task({
                    "title": title
                })

                print("Task created:")
                print(task)

            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                title = input("Enter new title: ")
                completed = input(
                    "Completed? (yes/no): "
                ).lower() == "yes"

                updated_task = update_task(
                    task_id,
                    {
                        "title": title,
                        "completed": completed
                    }
                )

                print("Task updated:")
                print(updated_task)

            elif choice == "5":
                task_id = int(input("Enter task ID: "))

                if delete_task(task_id):
                    print("Task deleted successfully.")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except TaskError as e:
            print(f"Error: {e}")

        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    menu()