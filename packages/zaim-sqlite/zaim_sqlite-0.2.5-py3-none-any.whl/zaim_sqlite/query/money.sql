SELECT
    money.date AS "日付",
    modes.name AS "方法",
    IFNULL (categories.name, '-') AS "カテゴリ",
    IFNULL (genres.name, '-') AS "カテゴリの内訳",
    IFNULL (from_account.name, '-') AS "支払元",
    IFNULL (to_account.name, '-') AS "入金先",
    IFNULL (money.name, '') AS "品目",
    money.comment AS "メモ",
    IFNULL (places.name, '-') AS "お店",
    money.currency_code AS "通貨",
    CASE
        WHEN modes.name = 'income' THEN money.amount
        ELSE 0
    END AS "収入",
    CASE
        WHEN modes.name = 'payment' THEN money.amount
        ELSE 0
    END AS "支出",
    CASE
        WHEN modes.name = 'transfer' THEN money.amount
        ELSE 0
    END AS "振替"
FROM
    money
    INNER JOIN modes on money.mode_id = modes.id
    LEFT JOIN categories on money.category_id = categories.id
    LEFT JOIN genres on money.genre_id = genres.id
    LEFT JOIN accounts AS from_account on money.from_account_id = from_account.id
    LEFT JOIN accounts AS to_account on money.to_account_id = to_account.id
    LEFT JOIN places on money.place_uid = places.uid