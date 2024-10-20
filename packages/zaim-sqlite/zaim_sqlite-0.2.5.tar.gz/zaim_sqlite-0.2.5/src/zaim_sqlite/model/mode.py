from sqlalchemy import Column, String
from zaim_sqlite.model import BaseModel


class Mode(BaseModel):
    """
    方法モデル
    """

    __tablename__ = "modes"
    __table_args__ = {"comment": "方法のマスターテーブル"}

    name = Column(String(255), nullable=False)
