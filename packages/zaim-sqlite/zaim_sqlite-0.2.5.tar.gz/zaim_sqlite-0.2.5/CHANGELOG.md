# Changelog

## [0.2.5](https://github.com/ryohidaka/zaim-sqlite/compare/v0.2.4...v0.2.5) (2024-10-19)


### Bug Fixes

* お店情報モデルに登録日時と更新日時を追加 ([4890b30](https://github.com/ryohidaka/zaim-sqlite/commit/4890b30026c5526b8e97b11bc9e53195827f3543))

## [0.2.4](https://github.com/ryohidaka/zaim-sqlite/compare/v0.2.3...v0.2.4) (2024-10-16)


### Bug Fixes

* placesが重複して登録される不具合を修正 ([456ca23](https://github.com/ryohidaka/zaim-sqlite/commit/456ca23cefe8ec3cf3de8bc8fed7194b0825f946))

## [0.2.3](https://github.com/ryohidaka/zaim-sqlite/compare/v0.2.2...v0.2.3) (2024-07-04)


### Bug Fixes

* API未初期化時は、方法一覧を取得しない ([38577fd](https://github.com/ryohidaka/zaim-sqlite/commit/38577fde8cc813db1a90022a6dceee8ec02098bc))

## [0.2.2](https://github.com/ryohidaka/zaim-sqlite/compare/v0.2.1...v0.2.2) (2024-07-04)


### Bug Fixes

* tqdmをダウングレード ([1b55efb](https://github.com/ryohidaka/zaim-sqlite/commit/1b55efb519bd81130e13b87fc4d95c0be28a452d))

## [0.2.1](https://github.com/ryohidaka/zaim-sqlite/compare/v0.2.0...v0.2.1) (2024-07-04)


### Bug Fixes

* 依存パッケージのロックファイルを修正 ([1b47ffa](https://github.com/ryohidaka/zaim-sqlite/commit/1b47ffa758dc14235cc9f40062a3543c9aaa7e04))

## [0.2.0](https://github.com/ryohidaka/zaim-sqlite/compare/v0.1.1...v0.2.0) (2024-07-04)


### Features

* pandasをインストール ([12a1ec0](https://github.com/ryohidaka/zaim-sqlite/commit/12a1ec09ac25786c0245ec53a8f7e54d49b41c6e))
* 入出金履歴に通貨を追加 ([ea80e65](https://github.com/ryohidaka/zaim-sqlite/commit/ea80e65caa64d197896627bae39ea2db311bf7a8))
* 入出金履歴をCSVファイルに出力する処理を追加 ([1c052e0](https://github.com/ryohidaka/zaim-sqlite/commit/1c052e01e41a0fd8cbaa50b30903a536f40a34c2))

## [0.1.1](https://github.com/ryohidaka/zaim-sqlite/compare/v0.1.0...v0.1.1) (2024-07-03)


### Bug Fixes

* 文言を本家に揃える ([f5521c0](https://github.com/ryohidaka/zaim-sqlite/commit/f5521c0fa0ad8b32658c1d4e0f3b43454ed72aae))
* 種別の順序を修正 ([6097f91](https://github.com/ryohidaka/zaim-sqlite/commit/6097f91bc6c5a015b66f0007012a7f074c52fa25))

## 0.1.0 (2024-07-02)


### Features

* DB接続処理を追加 ([9962746](https://github.com/ryohidaka/zaim-sqlite/commit/996274652aec65bafa9da2955e3668170984f849))
* pyzaimの認証処理を追加 ([19e07c6](https://github.com/ryohidaka/zaim-sqlite/commit/19e07c6c5c8487bf8dc94b91386f728fb976914c))
* pyzaimをインストール ([a1487e4](https://github.com/ryohidaka/zaim-sqlite/commit/a1487e4a77e17953bcdee33626e80f7234c76596))
* sqlalchemyをインストール ([17adfbe](https://github.com/ryohidaka/zaim-sqlite/commit/17adfbebdf3e93dd4f6c69680915924ef223c20b))
* tqdmをインストール ([a7f66b0](https://github.com/ryohidaka/zaim-sqlite/commit/a7f66b08e7a34e29dabd659983a179245b5a4d28))
* upsert処理を追加 ([9209fcf](https://github.com/ryohidaka/zaim-sqlite/commit/9209fcfb1b451e9f5ee58eec8e6e328e2b69683c))
* ZaimSqliteクラスを追加 ([b24cb95](https://github.com/ryohidaka/zaim-sqlite/commit/b24cb952ff73cf27e63f52e981fdcd39fa4dba39))
* カテゴリ一覧を挿入する処理を追加 ([f8fdaea](https://github.com/ryohidaka/zaim-sqlite/commit/f8fdaea10641d0c0efdb4091d61e0bf4551dc8ea))
* ジャンル一覧を挿入する処理を追加 ([3a331ab](https://github.com/ryohidaka/zaim-sqlite/commit/3a331abc87f0921eb94d361772705b803900b9db))
* プログレスバーを追加 ([c50fe38](https://github.com/ryohidaka/zaim-sqlite/commit/c50fe3883a067df5508522775038f40fe19d5e5e))
* プロジェクトをリネーム ([a511611](https://github.com/ryohidaka/zaim-sqlite/commit/a511611c9d25308139931f6d04b62a784745c9e5))
* ログ出力を追加 ([0f2dcf0](https://github.com/ryohidaka/zaim-sqlite/commit/0f2dcf06c6a9578155dff7af965cf823196de340))
* 入出金履歴を挿入する処理を追加 ([ce1a49b](https://github.com/ryohidaka/zaim-sqlite/commit/ce1a49bdf60174f72ee457b09be9d0c472f27615))
* 口座一覧を挿入する処理を追加 ([0a34619](https://github.com/ryohidaka/zaim-sqlite/commit/0a34619838721be3f60f76fbc8a4fd2e83666f04))
* 種別一覧を挿入する処理を追加 ([af06a23](https://github.com/ryohidaka/zaim-sqlite/commit/af06a23a69eeb75f6b4f4999cfd9591f3de703da))


### Bug Fixes

* 不要なテストコードを削除 ([25553fa](https://github.com/ryohidaka/zaim-sqlite/commit/25553fa0896396da9e88f41d97510e93e9d4fddb))
* 不要な出力を削除 ([0baef7a](https://github.com/ryohidaka/zaim-sqlite/commit/0baef7aff63986ccc40c983ca05ba38a0f58abdd))


### Documentation

* キーワード情報を追加 ([7881d64](https://github.com/ryohidaka/zaim-sqlite/commit/7881d64c9a8546a26c57cf1d6419ffe51c1b4507))
* 使用方法を追記 ([d6c5db5](https://github.com/ryohidaka/zaim-sqlite/commit/d6c5db5007e94341e3c2cf55512f514490f62597))


### Miscellaneous Chores

* release 0.1.0 ([0af6508](https://github.com/ryohidaka/zaim-sqlite/commit/0af650859628a35c1bdc5116170e7298d563ea6c))
