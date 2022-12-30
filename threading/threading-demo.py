import time
import threading


start_time = time.perf_counter()


def do_something():
    print('Sleeping 1s...')
    time.sleep(1)
    print('Done sleeping\n')

# turn these to threads instead
# do_something()
# do_something()
# ->
thread_1 = threading.Thread(target=do_something)
thread_2 = threading.Thread(target=do_something)
# won't run here yet
# to initiate thread
thread_1.start()
thread_2.start()

# join() will make sure that each thread will finish first before moving on
# (in this case to calculate and print the end time)
thread_1.join()
thread_2.join()

end_time = time.perf_counter()

print(f"Finished in {round(end_time-start_time, 2)} secs")
