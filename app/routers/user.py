from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserResponse
from app.db.session import get_db
from app.services.user_service import get_users_filtered

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def list_users(role: Optional[str] = Query(None), status: Optional[str] = Query(None), db: AsyncSession = Depends(get_db)):
    users = await get_users_filtered(db, role=role, status=status)
    return users
