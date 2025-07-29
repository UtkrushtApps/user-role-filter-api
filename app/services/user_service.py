from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from app.models.user import UserResponse
from app.db.user_model import User

async def get_users_filtered(db: AsyncSession, role: Optional[str], status: Optional[str]) -> List[UserResponse]:
    # Implementation goes here
    pass
