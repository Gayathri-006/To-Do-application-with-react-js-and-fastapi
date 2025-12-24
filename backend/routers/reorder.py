from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm.exc import StaleDataError
from models import Task, get_db
from schemas.reorder_request import ReorderRequest

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/reorder")
def reorder_tasks(request: ReorderRequest, db: Session = Depends(get_db)) -> dict:
    """
    Reorder tasks by their IDs.

    This endpoint receives a request containing a list of task IDs in the desired order.
    It updates the 'position' field of each task in the database to reflect the new order.

    Request:
      - Method: POST
      - URL: /tasks/reorder
      - Body: JSON object with a 'tasks' field, which is a list of task IDs in the new order.
        Example: { "tasks": [ { "id": 3, "position": 0 }, { "id": 1, "position": 1 }, { "id": 2, "position": 2 } ] }

    Database Operations:
      - For each task ID in the received list, it updates the 'position' field in the database.
      - The 'position' field is set to the index of the task ID in the list.
      - This ensures that all tasks are reordered according to the provided list.

    Response:
      - Returns a JSON object with a message indicating the success of the operation.
        Example: { "message": "Tasks reordered successfully" }
    """
    task_ids = [task.id for task in request.tasks]

    # Блокировка строк, которые мы собираемся пересортировать
    db_tasks = db.execute(select(Task).where(Task.id.in_(task_ids)).with_for_update()).scalars().all()

    if len(db_tasks) != len(task_ids):
        found_task_ids = {task.id for task in db_tasks}
        missing_task_ids = set(task_ids) - {int(task_id) for task_id in found_task_ids}
        raise HTTPException(status_code=400, detail=f"Some tasks not found: {missing_task_ids}")

    for task_data in request.tasks:
        db_task = next((task for task in db_tasks if task.id == task_data.id), None)
        if db_task:
            db_task.position = task_data.position  # type: ignore
        else:
            raise HTTPException(status_code=404, detail=f"Task with id {task_data.id} not found")

    try:
        db.commit()
    except StaleDataError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Data conflict error: {str(e)}")

    return {"message": "Tasks reordered successfully"}
