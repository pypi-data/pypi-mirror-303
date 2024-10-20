from datetime import datetime
from sqlalchemy import Column, Integer, DateTime

from zaim_sqlite.lib import Base


class BaseModel(Base):
    """
    共通のベースモデル
    """

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
