# zaim-sqlite

[![PyPI version](https://badge.fury.io/py/zaim-sqlite.svg)](https://badge.fury.io/py/zaim-sqlite)
![build](https://github.com/ryohidaka/zaim-sqlite/workflows/Build/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Zaim のデータを SQLite DB に格納する Python パッケージ

## Installation

You can install this library using PyPI:

```shell
pip install zaim-sqlite
```

## 使用方法

```py
from zaim_sqlite import ZaimSqlite

database = "sqlite:///db/zaim.db"

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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
