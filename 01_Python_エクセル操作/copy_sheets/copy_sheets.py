#####################################################################
#  ・既存の納品書（エクセル）をベースに新しい納品書（エクセル）を作成  #
#  ・新しい納品書にはテキストファイルから読み込んだデータをもとに、    #
#  　それぞれシートを追加する                                        #
#####################################################################

from pathlib import Path
from openpyxl import load_workbook

try:
    customerFilePath = Path("customer.txt")
    # 入力ファイルが存在しなければ例外をスロー
    if not (Path(customerFilePath).exists()):
        print("『" + customerFilePath.name + "』が存在しません。")
        raise FileExistsError()
    
    excelPath = Path("ファイル_ひな形.xlsx")
    # 出力先ファイルが存在しなければ例外をスロー
    if not (Path(excelPath).exists()):
        print("『" + excelPath.name + "』が存在しません。")
        raise FileExistsError()

    # 既存のブックを読み込む
    wb = load_workbook("ファイル_ひな形.xlsx")

    with customerFilePath.open(encoding="utf-8") as f:
        for line in f:
            sheet_name = line.rstrip('\r\n')
            # シート作成
            ws_copy = wb.copy_worksheet(wb["ファイル"])
            ws_copy.title = sheet_name
            # 値の書き込み
            ws_copy["A7"].value = sheet_name
            
    # 先頭シートを削除
    wb.remove(wb.worksheets[0])
    # 名前をつけて保存
    wb.save("new_sheets.xlsx")
    print("保存に成功しました。処理を終了します。")
    
except FileExistsError as e:
    print("処理を終了します。")

except Exception as e:
    print(e)
    print("異常が発生しました。処理を終了します。")