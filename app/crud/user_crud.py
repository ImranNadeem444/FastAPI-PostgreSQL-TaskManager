# ==========================================
# IMPORT DATABASE SESSION
# ==========================================

from sqlalchemy.orm import Session


# ==========================================
# IMPORT USER MODEL
# ==========================================

from app.models.user_model import User


# ==========================================
# CREATE NEW USER
# ==========================================

def create_user(
    db: Session,
    email: str,
    hashed_password: str
):

    new_user = User(
        email=email,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


# ==========================================
# GET USER BY EMAIL
# ==========================================

def get_user_by_email(
    db: Session,
    email: str
):

    return db.query(User).filter(
        User.email == email
    ).first()