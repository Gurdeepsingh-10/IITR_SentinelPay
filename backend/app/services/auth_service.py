from app.db.prisma import db
from app.utils.password import hash_password, verify_password
from app.utils.tokens import create_access_token

async def signup(email: str, password: str):
    user = await db.user.create(
        data={
            "email": email,
            "passwordHash": hash_password(password),
            "profile": {"create": {}}
        }
    )
    return create_access_token(user.id)

async def login(email: str, password: str):
    user = await db.user.find_unique(where={"email": email})
    if not user or not verify_password(password, user.passwordHash):
        return None
    return create_access_token(user.id)
