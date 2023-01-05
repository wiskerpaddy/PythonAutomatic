import schedule
import time

def doNotice():
    print("お昼になりました")

schedule.every().day.at("23:11").do(doNotice)

# 指定時間になったら、doNotice関数を実行
while True:
    schedule.run_pending()
    time.sleep(1)