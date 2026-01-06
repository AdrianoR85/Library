from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from datetime import timedelta
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.models.schemas.user import UserCreate, UserLogin, UserResponse
from app.core.config import settings


class AuthService:

    @staticmethod
    async def register_user(db: AsyncSession, user_data: UserCreate) -> UserResponse:
        username_exists = await UserRepository.check_username_exists(
            db, user_data.username
        )
        if username_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered.",
            )

        hashed_password = hash_password(user_data.password)

        user = await UserRepository.create_user(
            db=db,
            username=user_data.username,
            hashed_password=hashed_password,
            role=user_data.role,
        )

        return UserResponse(
            id_auth=user.id_auth,
            username=user.username,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at,
        )

    @staticmethod
    async def authenticate_user(db: AsyncSession, login_data: UserLogin) -> dict:
        user = await UserRepository.get_by_username(db, login_data.username)

        if not user or not verify_password(login_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
            )

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    async def get_current_user_info(db: AsyncSession, username: str) -> UserResponse:
        user = await UserRepository.get_by_username(db, username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        return UserResponse(
            id_auth=user.id_auth,
            username=user.username,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at,
        )
