import sys
from pathlib import Path
from openpyxl import load_workbook

#####################################################################
#  ・新しい納品書にはinputテキストファイルから読み込んだデータをもとに #
#  　それぞれシートを追加する                                        #
#####################################################################

def fileImport():
    customerFilePath = Path("input.txt")
    # 入力ファイルが存在しなければ例外をスロー
    if not (Path(customerFilePath).exists()):
        print("『" + customerFilePath.name + "』が存在しません。")
        raise FileExistsError()
    
    excelPath = Path("test.xlsx")
    # 出力先ファイルが存在しなければ例外をスロー
    if not (Path(excelPath).exists()):
        print("『" + excelPath.name + "』が存在しません。")
        raise FileExistsError()

    # 既存のブックを読み込む
    wb = load_workbook("test.xlsx")

    with customerFilePath.open(encoding="utf-8") as f:

        for line in f:
            sheet_name = line.rstrip('\r\n')

            # シート名確認
            dupFlag = sheetTitleCheck(sheet_name,wb)

            if dupFlag == True:
                print(sheet_name + 'は存在します。シート作成をスキップします。')
                dupFlag = False
                continue

            # シート作成
            ws_copy = wb.copy_worksheet(wb["ファイル"])
            ws_copy.title = sheet_name
            # 値の書き込み
            ws_copy["A1"].value = sheet_name
            
    # 名前をつけて保存
    # wb.save("new_test.xlsx")
    wb.save("test.xlsx") 
    print("保存に成功しました。処理を終了します。")

def sheetTitleCheck(target_name,wb):
    dupFlag = False
    #ファイル内の全てのシートをループして検索
    for ws in wb.worksheets:

        #指定シートが存在していれば、変数にTrueを格納
        if ws.title == target_name:
            dupFlag = True
    
    return dupFlag

if __name__ == '__main__':
    try:
        fileImport()

    except PermissionError as e:
        print("ファイルへの書き込みが失敗しました。")

    except FileExistsError as e:
        print("inputファイルが存在していません。")

    except ValueError as e:
        print("シート名に無効な文字列が指定されています。")

    except Exception as e:
        print(e)
        print("異常が発生しました。処理を終了します。")
    
    finally:
        print("処理を終了します。")