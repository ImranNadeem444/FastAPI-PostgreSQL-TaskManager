from pydantic import BaseModel, EmailStr


# ==========================================
# USER SIGNUP SCHEMA
# ==========================================

class UserCreate(BaseModel):

    # User email
    email: EmailStr

    # User password
    password: str


# ==========================================
# TOKEN RESPONSE SCHEMA
# ==========================================

class Token(BaseModel):

    # JWT access token
    access_token: str

    # Token type
    token_type: str