from pathlib import Path

# ファイル出力処理
try:
    # 検索対象のフォルダを選択
    target_path = Path("target")

    # フォルダが存在しなければ例外を投げる
    if not (target_path.exists()):
        raise FileNotFoundError

    # フォルダー内の中のすべてのファイルを取得
    path_list = target_path.iterdir()
    seqNum = 1
    for path in path_list:
        path_after = Path(f"target/旅行写真_{seqNum}.docx")
        path.rename(path_after)
        seqNum = seqNum + 1
    print("rename処理が完了しました。")

except FileNotFoundError as e:
    print('フォルダが存在しません。処理を終了します。')

except Exception as e:
    print(e)
    print('エラーが発生しました。処理を終了します。')


