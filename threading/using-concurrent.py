import time
import concurrent.futures       # faster than threading


start_time = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds}s...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


# (A) using ThreadPoolExecutor ---> Sleeping 5,4,3,2,1 Then Done 1,2,3,4,5
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # future_1 = executor.submit(do_something, 1)    # (function_name, args)
#     secs = [5, 4, 3, 2, 1]
#     # future_results = [executor.submit(do_something, 1) for _ in range(10)]
#     future_results = [executor.submit(do_something, sec) for sec in secs]
#     # print(future_1.result())
#     for f in concurrent.futures.as_completed(future_results):
#         print(f.result())

# (B) using ThreadPoolExecutor with map ---> Sleeping 5,4,3,2,1 The Done 5,4,3,2,1
with concurrent.futures.ThreadPoolExecutor() as executor:
    # future_1 = executor.submit(do_something, 1)    # (function_name, args)
    secs = [5, 4, 3, 2, 1]
    future_results = executor.map(do_something, secs)       # map will return with the order that they started
    for future_result in future_results:
        print(future_result)


end_time = time.perf_counter()

print(f"Finished in {round(end_time-start_time, 2)} secs")
