from .meta import Base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Table,
)


association_table = Table(
    'association', Base.metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('stock_id', Integer, ForeignKey('stocks.id'))
)