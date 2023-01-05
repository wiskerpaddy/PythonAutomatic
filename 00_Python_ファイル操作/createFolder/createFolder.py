from pathlib import Path
import os

# ファイル名のリスト
name_list = [
    "AAA株式会社",
    "BBB株式会社",
    "CCC株式会社"
]

#ファイルの作成
for name in name_list:
    #フォルダが存在しなければ処理を終了
    if not (Path(name).exists()):
        folPath = Path(name)
        folPath.mkdir()
        print("ファイルを作成しました。")
    else:
        print("フォルダが既に存在しています。")