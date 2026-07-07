from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import User
from app.schemas import UserResponse
from app.utils.security import verify_token

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user(
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(User).where(User.id == token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

@router.get("/profile", response_model=UserResponse)
async def get_user_profile(
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(User).where(User.id == token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user
