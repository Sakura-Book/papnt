# papnt (custom)
## 変更点
- ~Render.comで使えるように、doiの機能だけ入れたwebhook_server.pyを追加~ (制限時間の関係でうまく動作しなかったので供養)
- tokenとdatabase_idを環境変数から読み込むように変更

## 使い方
1. このリポジトリをcloneする
2. `conda install .`
3. `~/.bashrc`に、以下の内容を追記する
    ```
    export token=/*自分のDBと紐づけてあるNotion Integrationのtoken*/
    export database_id=/*自分のDBのID(URLから切り取ってくる)*/
    ```
