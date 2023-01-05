from pathlib import Path
from datetime import datetime
import pytz

# ファイル出力処理
try:
    # 現在時刻取得
    dtNow = datetime.now(pytz.timezone('Asia/Tokyo'))

    # 検索対象のフォルダを選択
    target_path = Path("面談シート")

    # フォルダが存在しなければ例外を投げる
    if not (Path(target_path).exists()):
        raise FileNotFoundError

    # フォルダー内の中のすべてのファイルを取得
    path_list = target_path.iterdir()

    # ファイルリストの出力先ファイルを指定
    output_path = Path("file_list.txt")

    # 出力先ファイルが存在しなければファイル作成
    if not (Path(output_path).exists()):
        filePath = Path(output_path)
        filePath.open(mode="w")
        print("ファイルを作成しました。")
    
    # 書き込み対象のファイルを開く
    with output_path.open(mode="w",encoding="utf8") as f:
        fileCount = 0
        # 書き込んだ時間をファイルに書き込み
        f.write(str(dtNow))
        f.write("\n")
        for path in path_list:
            # ファイル名を書き込み
            f.write(path.name)
            f.write("\n")
            fileCount = fileCount + 1
        print("ファイルが" + str(fileCount) + "個存在しました。")
    print("ファイルの書き込みに成功しました。")

except FileNotFoundError as e:
    print('フォルダが存在しません。処理を終了します。')

except Exception as e:
    print(e)
    print('エラーが発生しました。処理を終了します。')


