# ==========================================
# IMPORT REQUIRED MODULES
# ==========================================

from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import OAuth2PasswordBearer

from jose import (
    jwt,
    JWTError
)

from sqlalchemy.orm import Session


# ==========================================
# IMPORT DATABASE
# ==========================================

from app.database import get_db


# ==========================================
# IMPORT USER CRUD
# ==========================================

from app.crud.user_crud import get_user_by_email


# ==========================================
# IMPORT JWT SETTINGS
# ==========================================

from app.auth.jwt_handler import (
    SECRET_KEY,
    ALGORITHM
)


# ==========================================
# OAUTH2 SCHEME
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# ==========================================
# GET CURRENT AUTHENTICATED USER
# ==========================================

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    try:

        # Decode JWT token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract email
        email = payload.get("sub")

        # Invalid token
        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        # Find user in PostgreSQL
        user = get_user_by_email(
            db,
            email
        )

        # User not found
        if user is None:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Return FULL user object
        return user

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token is invalid"
        )