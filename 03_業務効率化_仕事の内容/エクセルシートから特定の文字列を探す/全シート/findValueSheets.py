import sys
import os
from openpyxl import load_workbook
from pathlib import Path

EXCEL_SUFFIX = ['.xlsx','.xlsm','.xlsb','.xltx']

def findValue(targetValue):
    # ①フォルダー内のファイル一覧を取得
    targetPath = Path("work")
    # 対象のフォルダが存在しなければ例外をスロー
    if not (Path(targetPath).exists()):
        print("『" + targetPath.name + "』が存在しません。")
        raise FileExistsError()  

    # ①フォルダー内のファイル一覧を取得
    path_list = targetPath.iterdir()

    for path in path_list:
        if not Path(path).exists():
            raise FileExistsError()

        base, ext = os.path.splitext(path)

        if 0 == EXCEL_SUFFIX.count(ext):
            print(base + "は、エクセルファイルではありません。")
            continue

        # ②-1 ファイル名取得
        pathName = path.name

        # ②-2 ブックを読み込み
        wb = load_workbook(f"work/{pathName}",read_only=True)
        # データ件数
        dateCount = 0

        for i in range(len(wb.worksheets)):
            ws = wb.worksheets[i]
            # エクセルのデータをすべて読み込む
            for row in ws:
                for column in row:
                    if str(column.value) == targetValue:
                        dateCount = dateCount + 1 
    
        print("「" + targetValue + "」は、" + path.name + "に" + str(dateCount) + "個ありました。")

if __name__ == '__main__':
    args = sys.argv
    try:
        findValue(args[1])
    except Exception as e:
        print(e)