from pathlib import Path
from shutil import move,copy2,copytree

# ファイル出力処理
try:
    # 検索対象のフォルダを選択
    target_path = Path("target")

    # フォルダが存在しなければ例外を投げる
    if not (Path(target_path).exists()):
        raise FileNotFoundError

    # 移動先フォルダを作成
    Path("backUp").mkdir(exist_ok=True)

    # フォルダー内の中のすべてのファイルを取得
    path_list = target_path.iterdir()

    for path in path_list:
        if path.is_file():
            file_name = path.name
            copy2(f"target/{file_name}",f"backUp/{file_name}")

    print("ファイルのコピーに成功しました。")

except FileNotFoundError as e:
    print('フォルダが存在しません。処理を終了します。')

except Exception as e:
    print(e)
    print('エラーが発生しました。処理を終了します。')


