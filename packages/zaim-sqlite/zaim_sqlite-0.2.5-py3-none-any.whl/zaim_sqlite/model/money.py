from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from zaim_sqlite.model import BaseModel


class Money(BaseModel):
    """
    入出金情報モデル
    """

    __tablename__ = "money"
    __table_args__ = {"comment": "入出金情報のマスターテーブル"}

    name = Column(String(255))
    date = Column(String(255), nullable=False)
    mode_id = Column(Integer, ForeignKey("modes.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))
    from_account_id = Column(Integer, ForeignKey("accounts.id"))
    to_account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Integer, nullable=False)
    comment = Column(String(255))
    active = Column(Boolean, nullable=False)
    receipt_id = Column(Integer)
    place_uid = Column(String(255), ForeignKey("places.uid"))
    currency_code = Column(String(255))
