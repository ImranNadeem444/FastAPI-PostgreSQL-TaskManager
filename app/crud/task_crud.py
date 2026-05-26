from sqlalchemy.orm import Session

from app.models.task_model import Task


# ==========================================
# CREATE TASK
# ==========================================

def create_task(

    db: Session,

    task_data,

    user_id: int

):

    new_task = Task(

        title=task_data.title,

        description=task_data.description,

        completed=task_data.completed,

        # Store task owner
        user_id=user_id
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task


# ==========================================
# GET ALL TASKS OF CURRENT USER
# ==========================================

def get_all_tasks(

    db: Session,

    user_id: int

):

    return db.query(Task).filter(

        Task.user_id == user_id

    ).all()


# ==========================================
# GET SINGLE TASK OF CURRENT USER
# ==========================================

def get_task_by_id(

    db: Session,

    task_id: int,

    user_id: int

):

    return db.query(Task).filter(

        Task.id == task_id,

        Task.user_id == user_id

    ).first()


# ==========================================
# DELETE TASK OF CURRENT USER
# ==========================================

def delete_task(

    db: Session,

    task_id: int,

    user_id: int

):

    task = db.query(Task).filter(

        Task.id == task_id,

        Task.user_id == user_id

    ).first()

    if task:

        db.delete(task)

        db.commit()

    return task
# ==========================================
# UPDATE TASK OF CURRENT USER
# ==========================================

def update_task(

    db: Session,

    task_id: int,

    updated_task,

    user_id: int

):

    # Find task belonging to current user
    task = db.query(Task).filter(

        Task.id == task_id,

        Task.user_id == user_id

    ).first()

    # Task not found
    if not task:

        return None

    # Update title
    task.title = updated_task.title

    # Update description
    task.description = updated_task.description

    # Update completed status
    task.completed = updated_task.completed

    # Save changes
    db.commit()

    # Refresh updated object
    db.refresh(task)

    return task