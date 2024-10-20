from sqlalchemy import Column, String

from .base import BaseModel


class Account(BaseModel):
    """
    口座モデル
    """

    __tablename__ = "accounts"
    __table_args__ = {"comment": "口座情報のマスターテーブル"}

    name = Column(String(255))
