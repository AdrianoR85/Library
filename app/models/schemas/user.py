from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import datetime


class UserBase(BaseModel):
  username: str = Field(..., min_length=3, max_length=20, description="Unique Username")
  role: str = Field(..., description="Type of user: customer, admin, or staff")

  @field_validator('username')
  @classmethod
  def validate_username(cls, value:str) -> str:
    if ' ' in value:
      raise ValueError("Username cannot have spaces")
    return value.lower()

  @field_validator('role')
  @classmethod
  def validate_role(cls, value:str) -> str:
    if value not in ["customer", "admin", "staff"]:
      raise ValueError('Role must be "customer", "admin" or "staff"')
    return value  


class UserCreate(UserBase):
  password: str = Field(..., min_length=6, description="Password must be at least 6 characters")

  @field_validator("password")
  @classmethod
  def validate_password(cls, value: str) -> str:
    if len(value) < 6:
      raise ValueError("The password must be at least 6 characters")
    if not any(char.isdigit() for char in value):
      raise ValueError("The password must contain at least one number")
    if not any(char.isalpha() for char in value):
      raise ValueError("The password must contain at least one letter")    
    return value
  

class UserLogin(BaseModel):
  username: str = Field(..., description="Username or staff registration")
  password: str = Field(..., description="User password")


class UserResponse(UserBase):
  id_auth: int
  is_active: bool
  created_at: datetime

  model_config = ConfigDict(from_attributes=True)


class UserInDB(UserResponse):
  password: str # password hash. Never return to a client!