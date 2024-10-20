from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from zaim_sqlite.model import BaseModel


class Genre(BaseModel):
    """
    カテゴリの内訳モデル
    """

    __tablename__ = "genres"
    __table_args__ = {"comment": "カテゴリの内訳情報のマスターテーブル"}

    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    active = Column(Boolean, nullable=False)
    parent_genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    sort = Column(Integer, nullable=False)
