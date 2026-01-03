from fastapi import APIRouter, HTTPException
from app.schemas.auth import SignupRequest, AuthResponse
from app.services.auth_service import signup, login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=AuthResponse)
async def signup_route(data: SignupRequest):
    token = await signup(data.email, data.password)
    return {"access_token": token}

@router.post("/login", response_model=AuthResponse)
async def login_route(data: SignupRequest):
    token = await login(data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}
