from datetime import datetime
from sqlalchemy import Column, DateTime, String

from zaim_sqlite.lib import Base


class Place(Base):
    """
    お店情報モデル
    """

    __tablename__ = "places"
    __table_args__ = {"comment": "お店情報のマスターテーブル"}

    uid = Column(String(255), nullable=False, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
