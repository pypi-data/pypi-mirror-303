from datetime import datetime
import importlib
from sqlalchemy import TextClause, create_engine, exc, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


def get_engine(database: str, echo: bool = False):
    """
    DBエンジンを作成する
    """
    engine = create_engine(database, echo=echo)

    return engine


def get_session(engine):
    """
    DBのセッションを作成する
    """
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    return session


def create_tables(engine):
    """
    テーブルを作成する
    """
    Base.metadata.create_all(bind=engine)


def upsert(session, model, **kwargs):
    """
    データを挿入する
    既存データがある場合は更新する
    """
    table = model.__table__
    primary_key = list(table.primary_key.columns.keys())[0]

    instance = (
        session.query(model).filter_by(**{primary_key: kwargs[primary_key]}).first()
    )

    if instance:
        # 変更があった場合、updated_atを更新
        for key, value in kwargs.items():
            if getattr(instance, key) != value:
                setattr(instance, key, value)
                instance.updated_at = datetime.now()
        session.add(instance)
    else:
        # 新しいインスタンスを挿入
        instance = model(**kwargs)
        session.add(instance)

    try:
        session.commit()
    except exc.SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()


def read_query(self) -> TextClause:
    """
    SQLファイルを読み込み。SQL文として返却する
    """
    try:
        # SQLファイルを読み込みます
        with importlib.resources.open_text(
            "zaim_sqlite.query", "money.sql", encoding="utf-8"
        ) as file:
            query = file.read()

            return text(query)
    except FileNotFoundError as e:
        self.logger.error(f"SQLファイルが見つかりません: {e}")
    except Exception as e:
        self.logger.error(f"予期しないエラーが発生しました: {e}")
