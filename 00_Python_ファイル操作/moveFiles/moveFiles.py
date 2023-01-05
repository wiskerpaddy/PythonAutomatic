from pathlib import Path
import os

# ファイル名のリスト
name_list = [
    "000145_豊原 真美",
    "000162_長谷川 祐希",
    "000112_今坂 恵理子"
]

#ファイルの作成
folName = "面談シート" #フォルダ名

for name in name_list:
    #フォルダが存在しなければ処理を終了
    if not (Path(folName).exists()):
        print("有効なPathではありません")
        break

    #フォルダ名とファイル名を連結
    joinedPath = Path(os.path.join(folName, f"{name}.docx"))
    joinedPath.open(mode="w")