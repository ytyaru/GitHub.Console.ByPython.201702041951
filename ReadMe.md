﻿# このソフトウェアについて

GitHubリポジトリを作成してローカルDBに登録するPythonスクリプト。 

まだコンソール出力だけでコマンドを実装していない。

# 開発環境

* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
    * [furl](https://github.com/gruns/furl)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

## 必要なデータベースを作成する

* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)
    * [GiHubApi.Authorizations.Create](https://github.com/ytyaru/GiHubApi.Authorizations.Create.20170113141429500)
* [GitHub.Repositories.Database.Create](https://github.com/ytyaru/GitHub.Repositories.Database.Create.20170114123411296)

# 実行

```dosbatch
python Main.sh
```

# 結果

リポジトリ操作の標準入出力する。

将来は以下の操作を実装したい。

* ローカルリポジトリ作成
* リモートリポジトリ作成
* 言語とByteサイズ取得
* リポジトリ情報と言語情報をローカルDBに保存
* リポジトリ集計の表示

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
