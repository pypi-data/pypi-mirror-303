import bcrypt

def hash_password(password: str) -> str:
    """Hash a password with a salt."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    """Check a password against a hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))