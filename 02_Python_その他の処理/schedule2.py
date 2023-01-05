import schedule
import time

def doNotice():
    print("1分経過しました")

# schedule.every(実行時間).時間.do(関数名)
# 時間 minutes, hours, hour(毎時間), seconds, monday etc...
schedule.every(1).minutes.do(doNotice)

# 指定時間になったら、doNotice関数を実行
while True:
    schedule.run_pending()
    time.sleep(1)