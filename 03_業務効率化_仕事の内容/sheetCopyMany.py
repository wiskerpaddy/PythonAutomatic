import openpyxl

### 1度だけの実行を想定                         ###
### 再度実行する際は一度追加したシートを消すこと ###

#ブックを開く
filename = 'C:/Users/user/Documents/soft learning/03_業務効率化_仕事の内容/test.xlsx'
wb = openpyxl.load_workbook(filename)

#複製するシート枚数
MyCnt = 10

#指定回数繰り返してシートを作成
for i in range(1,MyCnt+1):

    #雛形シートをコピー
    Ws = wb.copy_worksheet(wb['origin'])

    #シート名
    Shtname = str(i)
    Ws.title = Shtname

#別名で保存
wb.save(filename)