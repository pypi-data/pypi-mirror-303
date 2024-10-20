import os
from pyzaim import ZaimAPI
import pandas as pd
from tqdm import tqdm
from zaim_sqlite.lib import (
    ModeEnum,
    create_tables,
    get_engine,
    get_mode_id,
    get_session,
    get_unique_places,
    init_logger,
    read_query,
    upsert,
)
from zaim_sqlite.model import Account, Category, Genre, Mode, Money, Place


def main():
    # 環境変数から各種キーを取得
    consumer_id = os.environ.get("ZAIM_CONSUMER_ID")
    consumer_secret = os.environ.get("ZAIM_CONSUMER_SECRET")
    access_token = os.environ.get("ZAIM_ACCESS_TOKEN")
    access_token_secret = os.environ.get("ZAIM_ACCESS_SECRET")
    oauth_verifier = os.environ.get("ZAIM_ACCESS_VERIFIER")
    database = os.environ.get("DB")

    # Zaim2Sqlite クラスのインスタンスを作成
    app = ZaimSqlite(
        database,
        consumer_id,
        consumer_secret,
        access_token,
        access_token_secret,
        oauth_verifier,
    )

    # 口座一覧を挿入する
    app.upsert_accounts()

    # カテゴリ一覧を挿入する
    app.upsert_categories()

    # カテゴリの内訳一覧を挿入する
    app.upsert_genres()

    # 入出金履歴を挿入する
    app.upsert_money()

    # 入出金履歴をCSVファイルに出力する
    app.to_csv("output/zaim.csv")


class ZaimSqlite:
    def __init__(
        self,
        database: str,
        consumer_id: str = None,
        consumer_secret: str = None,
        access_token: str = None,
        access_token_secret: str = None,
        oauth_verifier: str = None,
    ):
        """
        ZaimSqlite クラスの初期化。
        """
        # ロガーの初期化
        self.logger = init_logger()
        self.logger.info("[開始] Zaim2Sqlite クラスの初期化")

        # ZaimAPI の初期化が必要なパラメータのうち、少なくとも一つでも存在するかチェック
        if any(
            [
                consumer_id,
                consumer_secret,
                access_token,
                access_token_secret,
                oauth_verifier,
            ]
        ):
            # ZaimAPI の初期化
            self.api = ZaimAPI(
                consumer_id,
                consumer_secret,
                access_token,
                access_token_secret,
                oauth_verifier,
            )
        else:
            self.api = None

        # Engine の作成
        self.engine = get_engine(database)

        # Sessionの作成
        self.session = get_session(self.engine)

        # テーブルを作成する
        create_tables(self.engine)

        # 方法一覧を挿入する
        if self.api:
            self._upsert_modes()

        self.logger.info("[完了] Zaim2Sqlite クラスの初期化")

    def upsert_accounts(self):
        """
        口座一覧を挿入する
        """
        # 口座一覧を取得
        accounts = self.api.account_itos

        for key, value in tqdm(accounts.items(), desc="口座一覧"):
            value = value if value != "-" else None
            upsert(self.session, Account, id=key, name=value)

    def upsert_categories(self):
        """
        カテゴリ一覧を挿入する
        """
        # カテゴリ一覧を取得
        categories = self.api._get_category()["categories"]

        for category in tqdm(categories, desc="カテゴリ一覧"):
            upsert(
                self.session,
                Category,
                id=category["id"],
                name=category["name"],
                mode_id=get_mode_id(category["mode"]),
                active=(category["active"] == 1),
                parent_category_id=category["parent_category_id"],
                sort=category["sort"],
            )

    def upsert_genres(self):
        """
        カテゴリの内訳一覧を挿入
        """
        # カテゴリの内訳一覧を取得
        genres = self.api._get_genre()["genres"]

        for genre in tqdm(genres, desc="カテゴリの内訳一覧"):
            upsert(
                self.session,
                Genre,
                id=genre["id"],
                name=genre["name"],
                category_id=genre["category_id"],
                active=(genre["active"] == 1),
                parent_genre_id=genre["parent_genre_id"],
                sort=genre["sort"],
            )

    def upsert_money(self):
        """
        入出金履歴を挿入する
        """
        # 入出金履歴を取得
        data = self.api.get_data()

        # お店情報を挿入する
        self._upsert_places(data)

        # お店情報一覧を取得
        places = [
            {"uid": place.uid, "name": place.name}
            for place in self.session.query(Place).all()
        ]

        for money in tqdm(data, desc="入出金履歴"):
            mode_id = get_mode_id(money["mode"])
            active = money["active"] == 1

            # お店名からお店IDを取得
            place_uid = next(
                (place["uid"] for place in places if place["name"] == money["place"]),
                None,
            )

            upsert(
                self.session,
                Money,
                id=money["id"],
                name=money["name"] or None,
                date=money["date"],
                mode_id=mode_id,
                category_id=money["category_id"] or None,
                genre_id=money["genre_id"] or None,
                from_account_id=money["from_account_id"] or None,
                to_account_id=money["to_account_id"] or None,
                amount=money["amount"],
                comment=money["comment"] or None,
                active=active,
                receipt_id=money["receipt_id"] or None,
                place_uid=place_uid,
                currency_code=money["currency_code"],
            )

    def to_csv(self, csv_path: str):
        """
        入出金履歴をCSVファイルに出力する

        Parameters:
        * csv_path: 出力するCSVパス
        """
        self.logger.info("[開始] CSV出力")

        # SQL文を読み込みます
        query = read_query(self)

        try:
            # データベースからデータを取得します
            with self.engine.connect() as connection:
                result = connection.execute(query)
                df = pd.DataFrame(result.fetchall(), columns=result.keys())

            # データをCSVファイルに出力します
            df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        except pd.errors.EmptyDataError as e:
            self.logger.error(f"データベースからデータを取得できませんでした: {e}")
        except Exception as e:
            self.logger.error(f"予期しないエラーが発生しました: {e}")

        self.logger.info("[完了] CSV出力")

    def _upsert_modes(self):
        """
        方法一覧を挿入する
        """
        for mode in tqdm(ModeEnum, desc="方法一覧"):
            upsert(self.session, Mode, id=mode.value, name=mode.name.lower())

    def _upsert_places(self, data):
        """
        お店情報の挿入
        """
        places = get_unique_places(data)

        for place in tqdm(places, desc="お店情報"):
            upsert(
                self.session,
                Place,
                uid=place["place_uid"],
                name=place["place"],
            )
