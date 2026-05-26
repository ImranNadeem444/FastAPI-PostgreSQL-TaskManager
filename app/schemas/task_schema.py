from pydantic import BaseModel, Field


# ==========================================
# BASE TASK SCHEMA
# ==========================================

# Base schema contains common fields
class TaskBase(BaseModel):

    # Task title validation
    title: str = Field(
        min_length=3,
        max_length=50,
        description="Title of the task"
    )

    # Task description validation
    description: str = Field(
        min_length=5,
        max_length=200,
        description="Task description"
    )

    # Default completed status
    completed: bool = False


# ==========================================
# CREATE TASK SCHEMA
# ==========================================

# Used when creating task
class TaskCreate(TaskBase):
    pass


# ==========================================
# RESPONSE TASK SCHEMA
# ==========================================

# Used when returning task data
class TaskResponse(TaskBase):

    # Task ID
    id: int