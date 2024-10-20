from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from zaim_sqlite.model import BaseModel


class Category(BaseModel):
    """
    カテゴリモデル
    """

    __tablename__ = "categories"
    __table_args__ = {"comment": "カテゴリ情報のマスターテーブル"}

    name = Column(String(255), nullable=False)
    mode_id = Column(Integer, ForeignKey("modes.id"), nullable=False)
    active = Column(Boolean, nullable=False)
    parent_category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    sort = Column(Integer, nullable=False)
