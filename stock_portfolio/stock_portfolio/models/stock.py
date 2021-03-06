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
    companyName = Column(String)
    exchange = Column(String)
    industry = Column(String)
    website = Column(String)
    description = Column(String)
    CEO = Column(String)
    issueType = Column(String)
    sector = Column(String)
    date = Column(DateTime)