# pip install schedule
import schedule
from schedule import every, repeat
from datetime import time, timedelta,datetime
import time as tm


@repeat(every(5).seconds, message="Say hi")
@repeat(every(2).seconds, message="Say hello")
def job(message):
    print(f"The message is: {message}")


def break_reminder():
    print(f"Take a break!")


def stock_market_opens():
    print(f"The ph stock market opens")


# def job():
#     print(f"Do this job")


# j1 = schedule.every(5).seconds.do(job_func=job)
# schedule.every().minute.at(time_str=":40").do(job_func=job)
# schedule.every().day.at(time_str="03:25").do(job_func=job)
# schedule.every().day.at(time_str="03:25").do(job_func=job)
counter = 0
start = tm.perf_counter()
while True:
    schedule.run_pending()
    tm.sleep(1)
    counter += 1
    # print(f"Elapsed time = {tm.perf_counter() - start}s")
    # if counter == 10:
    #     schedule.cancel_job(job=j1)
    # print(datetime.now())
# References:
# https://www.youtube.com/watch?v=yDPQfj4bZY8