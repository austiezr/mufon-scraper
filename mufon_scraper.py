import get_mufon as get
import df_creation as create
import schedule
import time

def job():
    get.get_table()
    time.sleep(5)
    create.df_create_and_merge()

schedule.every().day.at("06:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)