# ==========================================
# IMPORT SQLALCHEMY COMPONENTS
# ==========================================

from sqlalchemy import (
    Column,
    Integer,
    String
)


# ==========================================
# IMPORT RELATIONSHIP
# ==========================================

from sqlalchemy.orm import relationship


# ==========================================
# IMPORT DATABASE BASE
# ==========================================

from app.database import Base


# ==========================================
# USER MODEL
# ==========================================

class User(Base):

    # Table name
    __tablename__ = "users"


    # Primary key
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # User email
    email = Column(
        String,
        unique=True,
        index=True
    )


    # Hashed password
    password = Column(String)


    # ==========================================
    # RELATIONSHIP
    # ==========================================

    # One user can have many tasks
    tasks = relationship(
        "Task",
        back_populates="owner"
    )