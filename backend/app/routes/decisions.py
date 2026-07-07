from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Decision, User
from app.schemas import DecisionCreate, DecisionResponse, DecisionUpdate
from app.utils.security import verify_token
import uuid

router = APIRouter()

@router.post("/", response_model=DecisionResponse)
async def create_decision(
    decision_data: DecisionCreate,
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    new_decision = Decision(
        id=str(uuid.uuid4()),
        title=decision_data.title,
        description=decision_data.description,
        user_id=token,
        priority=decision_data.priority,
        status="pending"
    )
    
    db.add(new_decision)
    await db.commit()
    await db.refresh(new_decision)
    
    return new_decision

@router.get("/", response_model=list[DecisionResponse])
async def list_decisions(
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Decision).where(Decision.user_id == token).order_by(Decision.created_at.desc())
    result = await db.execute(stmt)
    decisions = result.scalars().all()
    
    return decisions

@router.get("/{decision_id}", response_model=DecisionResponse)
async def get_decision(
    decision_id: str,
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Decision).where(
        (Decision.id == decision_id) & (Decision.user_id == token)
    )
    result = await db.execute(stmt)
    decision = result.scalar_one_or_none()
    
    if not decision:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Decision not found"
        )
    
    return decision

@router.put("/{decision_id}", response_model=DecisionResponse)
async def update_decision(
    decision_id: str,
    decision_data: DecisionUpdate,
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Decision).where(
        (Decision.id == decision_id) & (Decision.user_id == token)
    )
    result = await db.execute(stmt)
    decision = result.scalar_one_or_none()
    
    if not decision:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Decision not found"
        )
    
    update_data = decision_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(decision, field, value)
    
    await db.commit()
    await db.refresh(decision)
    
    return decision

@router.delete("/{decision_id}")
async def delete_decision(
    decision_id: str,
    token: str = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Decision).where(
        (Decision.id == decision_id) & (Decision.user_id == token)
    )
    result = await db.execute(stmt)
    decision = result.scalar_one_or_none()
    
    if not decision:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Decision not found"
        )
    
    await db.delete(decision)
    await db.commit()
    
    return {"message": "Decision deleted successfully"}
