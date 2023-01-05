#####################################################################
#  ・エクセルの1つ目のシートの特定の文字列の個数を検索するプログラム　 #
#####################################################################

from openpyxl import load_workbook
from pathlib import Path

SUFFIX_EXCEL = ".xlsx"

# 検索対象エクセルパス
targetExcel = "売上_新宿店" + SUFFIX_EXCEL
# 検索対象文字列
targetValue = "あいうえお"

try:
    targetPath = Path(targetExcel)
    if not Path(targetPath).exists():
        raise FileExistsError()

    # エクセルファイルを読み込む    
    wb = load_workbook(targetPath.name,read_only=True)
    ws = wb.worksheets[0]

    # データ件数
    dateCount = 0

    # エクセルのデータをすべて読み込む
    for row in ws:
        for column in row:
            if str(column.value) == targetValue:
                dateCount = dateCount + 1 
    
    print("「" + targetValue + "」は、" + str(dateCount) + "個ありました。")

except FileExistsError as e:
    print("処理を終了します。")

except Exception as e:
    print(e)
    print("異常が発生しました。処理を終了します。")