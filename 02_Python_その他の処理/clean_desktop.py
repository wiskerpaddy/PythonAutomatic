from pathlib import Path
from datetime import datetime
from shutil import move
import schedule
import time

def doMove():
    # ファイル移動処理
    try:
        # 検索対象のフォルダを選択
        target_path = Path("target")

        # フォルダが存在しなければ例外を投げる
        if not (Path(target_path).exists()):
            raise FileNotFoundError

        # 移動先フォルダを作成
        Path("new").mkdir(exist_ok=True)

        # フォルダー内の中のすべてのファイルを取得
        path_list = target_path.iterdir()

        for path in path_list:
            if path.is_file():
                file_name = path.name
                move(f"target/{file_name}","new")

        print("ファイルの移動に成功しました。")

    except FileNotFoundError as e:
        print('フォルダが存在しません。処理を終了します。')

    except Exception as e:
        print(e)
        print('エラーが発生しました。処理を終了します。')

# schedule.every(実行時間).時間.do(関数名)
# 時間 minutes, hours, hour(毎時間), seconds, monday etc...
schedule.every().day.at("00:30").do(doMove)
schedule.every().day.at("17:00").do(doMove)

# 指定時間になったら、doNotice関数を実行
while True:
    schedule.run_pending()
    time.sleep(1)