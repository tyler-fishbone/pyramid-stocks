from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from .meta import Base

# need to change this to stock info
class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key = True)
    symbol = Column(String, nullable=False, unique=True)
    body = Column(String)
    author = Colume(String)
    date = Column(DateTime)