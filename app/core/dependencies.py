"""
This module is responsible for defining the dependencies used throughout the FastAPI application, mainly, it will handle authentication and authorization mechanisms.

Este arquivo conterá as dependências (dependencies) do FastAPI, principalmente para autenticação e autorização.
"""
from fastapi import Depends, HTTPException, status
from .security import decode_access_token
from ..database.connection import get_db
from psycopg import AsyncConnection
from typing import Optional, Annotated, Any, Dict 
from fastapi.security import OAuth2PasswordBearer

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

Token = Annotated[str, Depends(oauth2_bearer)]
DBConn = Annotated[AsyncConnection, Depends(get_db)]


async def get_current_user(token: Token, conn: DBConn) -> Dict[str, Any]:
  """
  Decondify the JWT token and fetch the user from the database. 
  Returns user data or raises 401 exception.
  Args:
      token (str): JWT token obtained from the Authorization header.
      conn (AsyncConnection): Asynchronous database connection.
  """
  payload = decode_access_token(token)

  if payload is None or 'sub' not in payload or 'id' not in payload:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate": "Bearer"},
    )
  # extract user identifier from token payload
  user_id: Any = payload.get("id")

  # fetch user from database
  async with conn.cursor() as cur:
    await cur.execute(
      """ SELECT id, username, email, full_name, is_active, is_superuser
          FROM authentication.auth WHERE id = %s
      """, (user_id,)   
    )   
    user_row = await cur.fetchone()

    if user_row is None:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User not found",
        headers={"WWW-Authenticate": "Bearer"},
      )
    user = {
      "id": user_row[0],
      "email": user_row[1],
      "is_active": user_row[3],
      "created_at": user_row[4],
    }

    return user

CurrentUser = Annotated[Dict[str, Any], Depends(get_current_user)]

async def get_current_active_user(current_user: CurrentUser) -> Dict[str, Any]:
  """
  Ensure the current user is active.
  Args:
      current_user (Dict[str, Any]): The current user data.
  """
  if not current_user.get("is_active", False):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
  return current_user   

