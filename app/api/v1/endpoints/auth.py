from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ....database.connection import get_db
from ....core.dependencies import get_current_user
from ....services.auth_service import AuthService
from ....models.schemas.user import UserResponse, UserCreate, UserLogin
from ....models.schemas.token import Token

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Create a new user account with a unique username and password.",
)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)) -> UserResponse:
    return await AuthService.register_user(db, user)


@router.post(
    "/login",
    response_model= Token,
    status_code=status.HTTP_200_OK,
    summary="User login",
    description="Authenticate a user and return an access token.",
)
async def login_user(credentials: UserLogin, db: AsyncSession = Depends(get_db)) -> Token:
    token_data = await AuthService.authenticate_user(db, credentials)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return Token(**token_data)

@router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Obter usuário atual",
    description="Retorna os dados do usuário autenticado"
)
async def get_me(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    
    username = current_user.get("username")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return await AuthService.get_current_user_info(db, username)