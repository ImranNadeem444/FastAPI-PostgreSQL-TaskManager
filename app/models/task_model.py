# ==========================================
# IMPORT SQLALCHEMY COMPONENTS
# ==========================================

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)


# ==========================================
# IMPORT SQLALCHEMY RELATIONSHIP
# ==========================================

from sqlalchemy.orm import relationship


# ==========================================
# IMPORT DATABASE BASE
# ==========================================

from app.database import Base


# ==========================================
# TASK MODEL
# ==========================================

class Task(Base):

    # Table name
    __tablename__ = "tasks"


    # Primary key
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # Task title
    title = Column(
        String,
        index=True
    )


    # Task description
    description = Column(String)


    # Task completion status
    completed = Column(
        Boolean,
        default=False
    )


    # ==========================================
    # FOREIGN KEY
    # ==========================================

    # Connect task to users table
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    # ==========================================
    # RELATIONSHIP
    # ==========================================

    # Access task owner
    owner = relationship(
        "User",
        back_populates="tasks"
    )