from pathlib import Path
from datetime import datetime
import pytz
from shutil import move

try:
    # 移動元（デスクトップ）のパスを取得
    target_path = Path(f"target")

    # 移動先フォルダ
    Path(f"old").mkdir(exist_ok=True)

    # 0:00を表すフォルダを作成
    today_start = datetime().timestamp(datetime.now().replace(hour=0,minute=0,second=0,microsecond=0))

    # 移動元（デスクトップ）フォルダー内の中のすべてのファイルを取得
    path_list = target_path.iterdir()

    for path in path_list:
        # ファイルであり、かつ更新日が昨日以前
        if path.is_file() and today_start - path.stat().st_mtime > 0:
            # ファイル名を取得
            file_name = path.name
            # ファイルを移動
            move((f"target/{file_name}"),f"old/")
    print("ファイルの移動に成功しました。")

except Exception as e:
    print(e)
    print('エラーが発生しました。処理を終了します。')


