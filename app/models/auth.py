from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ..database.connection import Base
from datetime import datetime, timezone

class Auth(Base):
    __tablename__ = 'authentication.auth'
    
    id_auth = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))