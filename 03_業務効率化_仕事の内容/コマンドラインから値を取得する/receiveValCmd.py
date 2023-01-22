import sys


def doFunction(n):
    print('「 '+ n +' 」が入力されました。')


if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        # 引数が数値なら実行
        if args[1].isdigit():
            doFunction(int(args[1]))
        else:
            print('引数が数値ではありません。')
    else:
        print('引数が足りません。1以上の数値を引数として入力して下さい。')