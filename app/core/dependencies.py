"""
This module is responsible for defining the dependencies used throughout the FastAPI application, mainly, it will handle authentication and authorization mechanisms.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional, Annotated, Any, Dict
from .security import decode_access_token, verify_password
from ..models.auth import Auth
from ..database.connection import get_db

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

Token = Annotated[str, Depends(oauth2_bearer)]
DBConn = Annotated[Session, Depends(get_db)]


async def get_current_user(token: Token) -> Dict[str, Any]:
  """
  Decondify the JWT token and fetch the user from the database. 
  Returns user data or raises 401 exception.
  """
  try:
    payload = decode_access_token(token)
    if payload is None:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    username = payload.get("sub")
    user_id = payload.get("id")
    role = payload.get("role")
    
    if username is None or user_id is None or role is None: 
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    
    return { "username": username, "id": user_id, "role": role }
  
  except Exception:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")


async def authenticate_user(username: str, password: str, db: DBConn) -> Optional[Dict[str, Any]]:
  """
  Authenticate a user by verifying username and password.
  Returns user data if authentication succeeds, None otherwise.
  """
  auth = db.query(Auth).filter(Auth.username == username).first()
  if auth is None: 
    return None

  if not verify_password(password, str(auth.password)):
    return None
  
  return { "username": auth.username, "id": auth.id_auth, "role": auth.role }