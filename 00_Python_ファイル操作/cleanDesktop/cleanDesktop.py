from pathlib import Path
from datetime import datetime
import pytz
from shutil import move

try:
    # 今日の日付を取得
    today = datetime.now().strftime('%Y-%m-%d')

    # ①移動先フォルダ
    Path(f"C:/Users/user/Desktop/一時保存/{today}").mkdir(exist_ok=True)

    # 移動元（デスクトップ）のパスを取得
    target_path = Path(f"C:/Users/user/Desktop/")

    # ②移動元（デスクトップ）フォルダー内の中のすべてのファイルを取得
    path_list = target_path.iterdir()

    for path in path_list:
        if path.is_file():
            # ③ファイル名を取得
            file_name = path.name
            # ④ファイルを移動
            move((f"C:/Users/user/Desktop/{file_name}"),
            f"C:/Users/user/Desktop/一時保存/")
    print("ファイルの移動に成功しました。")

except Exception as e:
    print(e)
    print('エラーが発生しました。処理を終了します。')


