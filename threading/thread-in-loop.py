import time
import threading


start_time = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds}s...')
    time.sleep(seconds)
    print('Done sleeping\n')


threads = []

for _ in range(10):     # the underscore _ is a throw away variable
    t = threading.Thread(target=do_something, args=[1])
        # to pass an argument for the do_something() function as a list with the args
    t.start()
    threads.append(t)

# we stored all the thread t from the above for loop to a list first
# before joining them

# this way we won't interrupt the created threads
for thread in threads:
    thread.join()

# join() will make sure that each thread will finish first before moving on


end_time = time.perf_counter()

print(f"Finished in {round(end_time-start_time, 2)} secs")
