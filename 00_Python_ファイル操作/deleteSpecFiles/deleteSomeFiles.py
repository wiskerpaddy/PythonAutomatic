from pathlib import Path
from datetime import datetime
import pytz
from shutil import move

try:
    # 移動元（デスクトップ）のパスを取得
    target_path = Path(f"target")

    # 移動元（デスクトップ）フォルダー内の中のすべてのファイルを取得
    path_list = target_path.iterdir()
    for path in path_list:
        # ファイルであり、かつ更新日が昨日以前
        if path.is_file() and "コピー" in path.name:
            # ファイル名を取得
            path.unlink()
    print("ファイルの削除に成功しました。")

except Exception as e:
    print(e)
    print('エラーが発生しました。処理を終了します。')