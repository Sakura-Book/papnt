# papnt (custom)
自分用に変更を加えたものです。

## 変更点
- ~Render.comで使えるように、doiの機能だけ入れたwebhook_server.pyを追加~ (制限時間の関係でうまく動作しなかったので供養)
- tokenとdatabase_idを環境変数から読み込むように変更
- DOIのURLを書き込むように変更

## 使い方
1. pipでリポジトリをinstallする
    ```
    $ pip install git+https://github.com/Sakura-Book/papnt.git@main
    ```
2. `~/.bashrc`に、以下の内容を追記
    ```
    export tokenkey=/*自分のDBと紐づけてあるNotion Integrationのtoken*/
    export database_id=/*自分のDBのID(URLから切り取ってくる)*/
    ```
3. `~/.bashrc`の更新を反映
   ```
   $ source ~/.bashrc
   $ source ~/.bash_profile
   ```
3. papntの動作確認
    ```
    $ papnt --help
    $ papnt doi
    ```
