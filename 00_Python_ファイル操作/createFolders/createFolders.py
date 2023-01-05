from pathlib import Path
import os

# フォルダー名の一覧が書かれたファイル
input_path = Path("customer_list.txt")

#ファイルを開く
#ファイルを使用する場合はwithを使う
with input_path.open(encoding="utf8") as f:
    for line in f:
        #改行コードを削除して読み込む
        folder_name = line.rstrip("\r\n")
        path = Path(folder_name)
        path.mkdir(exist_ok=True)