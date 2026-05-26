# ==========================================
# IMPORT REQUIRED FASTAPI COMPONENTS
# ==========================================

from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)


# ==========================================
# IMPORT OAUTH2 LOGIN FORM
# ==========================================

from fastapi.security import OAuth2PasswordRequestForm


# ==========================================
# IMPORT DATABASE SESSION
# ==========================================

from sqlalchemy.orm import Session


# ==========================================
# IMPORT DATABASE DEPENDENCY
# ==========================================

from app.database import get_db


# ==========================================
# IMPORT PYDANTIC SCHEMA
# ==========================================

from app.schemas.auth_schema import UserCreate


# ==========================================
# IMPORT USER CRUD FUNCTIONS
# ==========================================

from app.crud.user_crud import (
    create_user,
    get_user_by_email
)


# ==========================================
# IMPORT PASSWORD HASHING FUNCTIONS
# ==========================================

from app.auth.hashing import (
    hash_password,
    verify_password
)


# ==========================================
# IMPORT JWT TOKEN FUNCTION
# ==========================================

from app.auth.jwt_handler import (
    create_access_token
)


# ==========================================
# CREATE ROUTER OBJECT
# ==========================================

router = APIRouter()


# ==========================================
# USER SIGNUP ROUTE
# ==========================================

@router.post("/signup")
def signup(

    user: UserCreate,

    db: Session = Depends(get_db)

):

    # Check if email already exists
    existing_user = get_user_by_email(
        db,
        user.email
    )

    # If duplicate email found
    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Convert plain password into hashed password
    hashed_password = hash_password(
        user.password
    )

    # Store user into PostgreSQL
    create_user(
        db,
        user.email,
        hashed_password
    )

    # Return success response
    return {
        "message": "User created successfully"
    }


# ==========================================
# USER LOGIN ROUTE
# ==========================================

@router.post("/login")
def login(

    # OAuth2 form automatically expects:
    #
    # username
    # password
    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)

):

    # Find user in PostgreSQL
    existing_user = get_user_by_email(
        db,
        form_data.username
    )

    # If user not found
    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Verify entered password
    is_valid = verify_password(

        # Plain password entered by user
        form_data.password,

        # Stored hashed password
        existing_user.password
    )

    # If password incorrect
    if not is_valid:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    # Create JWT token
    access_token = create_access_token(
        data={

            # Store email inside JWT token
            "sub": existing_user.email
        }
    )

    # Return JWT token
    return {

        # JWT access token
        "access_token": access_token,

        # Token type
        "token_type": "bearer"
    }