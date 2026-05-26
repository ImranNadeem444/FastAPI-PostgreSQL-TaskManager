# ==========================================
# IMPORT REQUIRED FASTAPI COMPONENTS
# ==========================================

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends
)


# ==========================================
# IMPORT SQLALCHEMY SESSION
# ==========================================

from sqlalchemy.orm import Session


# ==========================================
# IMPORT DATABASE DEPENDENCY
# ==========================================

from app.database import get_db


# ==========================================
# IMPORT AUTHENTICATION FUNCTION
# ==========================================

from app.auth.oauth2 import get_current_user


# ==========================================
# IMPORT PYDANTIC SCHEMAS
# ==========================================

from app.schemas.task_schema import (
    TaskCreate,
    TaskResponse
)


# ==========================================
# IMPORT CRUD FUNCTIONS
# ==========================================

from app.crud.task_crud import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    delete_task,
    update_task
)


# ==========================================
# CREATE ROUTER OBJECT
# ==========================================

router = APIRouter()


# ==========================================
# GET ALL TASKS OF CURRENT USER
# ==========================================

@router.get("/tasks")
def get_tasks(

    # Authenticated PostgreSQL user object
    current_user = Depends(get_current_user),

    # Database session
    db: Session = Depends(get_db)

):

    # Fetch ONLY current user's tasks
    tasks = get_all_tasks(
        db,
        current_user.id
    )

    return {

        "user": current_user.email,

        "tasks": tasks
    }


# ==========================================
# CREATE TASK FOR CURRENT USER
# ==========================================

@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def add_task(

    # Request body
    task: TaskCreate,

    # Authenticated PostgreSQL user object
    current_user = Depends(get_current_user),

    # Database session
    db: Session = Depends(get_db)

):

    # Save task into PostgreSQL
    return create_task(

        db,

        task,

        current_user.id
    )


# ==========================================
# GET SINGLE TASK OF CURRENT USER
# ==========================================

@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def get_single_task(

    # URL parameter
    task_id: int,

    # Authenticated PostgreSQL user object
    current_user = Depends(get_current_user),

    # Database session
    db: Session = Depends(get_db)

):

    # Fetch task from PostgreSQL
    task = get_task_by_id(

        db,

        task_id,

        current_user.id
    )

    # Task not found
    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# ==========================================
# UPDATE TASK OF CURRENT USER
# ==========================================

@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def update_single_task(

    # URL parameter
    task_id: int,

    # Updated task data
    updated_task: TaskCreate,

    # Authenticated PostgreSQL user
    current_user = Depends(get_current_user),

    # Database session
    db: Session = Depends(get_db)

):

    # Update task
    task = update_task(

        db,

        task_id,

        updated_task,

        current_user.id
    )

    # Task not found
    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# ==========================================
# DELETE TASK OF CURRENT USER
# ==========================================

@router.delete("/tasks/{task_id}")
def remove_task(

    # URL parameter
    task_id: int,

    # Authenticated PostgreSQL user object
    current_user = Depends(get_current_user),

    # Database session
    db: Session = Depends(get_db)

):

    # Delete task from PostgreSQL
    task = delete_task(

        db,

        task_id,

        current_user.id
    )

    # Task not found
    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }