from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from .meta import Base

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key = True)
    password = Column(String)
    email = Column(String)
    username = Column(String)