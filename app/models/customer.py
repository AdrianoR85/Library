from ..database.connection import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Users(Base):
  __tablename__ = "auth"
  __table_args__ = {"schema": "authentication"}
  __table_args__ = {"schema": "customer"}

  id_user = Column(Integer, primary_key=True, index=True) 
  first_name  = Column(String)
  middle_name = Column(String)
  last_name = Column(String)
  ssn = Column(String, unique=True)
  phone = Column(String)
  status = Column(String, default="active")
  registration_date = Column()
  id_address = Column(Integer, ForeignKey("customer.address.id_address"))
  id_auth = Column(Integer, ForeignKey("authentication.auth.id_auth"))
