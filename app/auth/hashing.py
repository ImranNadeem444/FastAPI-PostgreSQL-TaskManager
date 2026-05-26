from passlib.context import CryptContext


# Create password hashing context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==========================================
# HASH PASSWORD
# ==========================================

def hash_password(password: str):

    # Convert plain password -> hashed password
    return pwd_context.hash(password)


# ==========================================
# VERIFY PASSWORD
# ==========================================

def verify_password(
    plain_password,
    hashed_password
):

    # Compare plain password with hashed password
    return pwd_context.verify(
        plain_password,
        hashed_password
    )