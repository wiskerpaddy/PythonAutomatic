import openpyxl
import sys

"""
コマンドラインから指定した個数分シートを1枚目のシートをコピーする
コピーをしたシート名は、何番目に追加したの番号にする
コピー元のシート名（1番目）は変えない
"""

def excellAddSheet(n):
    filename= 'C:\\Users\\user\\Documents\\soft learning\\03_業務効率化_仕事の内容\\test.xlsx'
    wb = openpyxl.load_workbook(filename)

    #指定回数繰り返してシートを作成
    for i in range(1,n+1):

        # originシートコピー
        wsCopy = wb.copy_worksheet(wb['origin'])
        wsCopy.title = str(i)
        print(int(wsCopy.title))

    #別名で保存
    wb.save(filename)

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        # 数字か確認
        if args[1].isdigit():
            try:
                # 引数を渡す関数
                print('1 ' + args[1])
                excellAddSheet(int(args[1]))

            except PermissionError as e:
                print('ファイルにアクセスできません。ファイルを開いている場合は閉じてください。')
 
            except Exception as e:
                print(e)
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')