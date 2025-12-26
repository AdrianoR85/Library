from ..app.core.dependencies import get_current_user
from ..app.core.security import create_access_token
from ..app.database.connection import settings
from fastapi import HTTPException
from jose import jwt
import pytest


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
  encode = { 'sub': 'testuser', 'id': 1, 'role': 'user' }
  token = jwt.encode(encode, settings.SECRET_KEY, settings.ALGORITHM)

  user = await get_current_user(token=token)
  assert user == {'sub': 'testuser', 'id': 1, 'role': 'user'}


@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
  encode = { 'sub': 'testuser' }
  token = jwt.encode(encode, settings.SECRET_KEY, settings.ALGORITHM) 

  with pytest.raises(HTTPException) as exinfo:
    await get_current_user(token=token) 
  
  assert exinfo.value.status_code == 401
  assert exinfo.value.detail == 'Invalid authentication credentials'