from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Task, get_db
from schemas.task import TaskTitleUpdate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.patch("/{task_id}/title", response_model=TaskResponse)
def update_task_title(task_id: int, task_update: TaskTitleUpdate, db: Session = Depends(get_db)) -> TaskResponse:
    """
    Update the title of an existing task.

    This endpoint updates the title of an existing task.

    Request:
      - Method: PATCH
      - URL: /tasks/{task_id}/title
      - Body: JSON object with 'title' field.
        Example: { "title": "Updated Task Title" }

    Database Operations:
      - Updates the title of the specified task in the database.

    Response:
      - Returns the updated task as a JSON object.
        Example: { "id": 1, "title": "Updated Task Title", "completed": false, "createdAt": "2023-01-01T00:00:00Z" }
    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_task.title = task_update.title  # type: ignore
    db.commit()
    db.refresh(db_task)
    
    return TaskResponse.from_orm(db_task)
