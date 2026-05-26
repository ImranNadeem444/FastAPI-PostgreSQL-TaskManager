from fastapi import Depends, HTTPException

from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from app.auth.jwt_handler import (
    SECRET_KEY,
    ALGORITHM
)


# ==========================================
# OAUTH2 SCHEME
# ==========================================

# OAuth2PasswordBearer extracts token
# from Authorization header
#
# Example:
#
# Authorization: Bearer TOKEN
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# ==========================================
# GET CURRENT USER
# ==========================================

def get_current_user(

    # Depends() automatically extracts token
    token: str = Depends(oauth2_scheme)

):

    try:

        # Decode JWT token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract email from token
        email = payload.get("sub")

        # If email missing
        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        # Return authenticated user email
        return email

    except JWTError:

        # Invalid token error
        raise HTTPException(
            status_code=401,
            detail="Token is invalid"
        )