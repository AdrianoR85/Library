from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.models.auth import Auth


class UserRepository:
    
    @staticmethod
    async def get_by_username(db: AsyncSession, username: str) -> Optional[Auth]:
        result = await db.execute(select(Auth).filter(Auth.username == username))
        return result.scalar_one_or_none()
    
    
    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> Optional[Auth]:
        result = await db.execute(select(Auth).filter(Auth.id_auth == user_id))
        return result.scalar_one_or_none()

    
    @staticmethod
    async def create_user(db: AsyncSession, username: str, hashed_password: str, role: str) -> Auth:
        db_user = Auth(
            username=username,
            password=hashed_password,
            role=role
        )
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    
    
    @staticmethod
    async def update_user(db: AsyncSession, user_id: int, **kwargs) -> Optional[Auth]:
        result = await db.execute(select(Auth).filter(Auth.id_auth == user_id))
        user = result.scalar_one_or_none()
        
        if not user:
            return None
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        await db.commit()
        await db.refresh(user)
        return user
    
    
    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int) -> bool:
        result = await db.execute(select(Auth).filter(Auth.id_auth == user_id))
        user = result.scalar_one_or_none()
        
        if not user:
            return False
        
        user.is_active = bool(False)
        await db.commit()
        return True
    
    
    @staticmethod
    async def check_username_exists(db: AsyncSession, username: str) -> bool:
        result = await db.execute(select(Auth).filter(Auth.username == username))
        return result.scalar_one_or_none() is not None
