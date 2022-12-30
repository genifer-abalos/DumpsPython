import concurrent.futures
import multiprocessing
import time

start_time = time.perf_counter()


def do_something(sleep_seconds: float):
    print(f'Sleeping {sleep_seconds}s...')
    time.sleep(sleep_seconds)
    return f'Done sleeping {sleep_seconds}'


if __name__ == '__main__':

    # this method allows the ProcessPoolExecutor to decide
    #   the capability of our hardware
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     # executes a function and returns a future object
    #     # future_1 = executor.submit(do_something, 1)
    #     future_results = [executor.submit(do_something, 1.5) for _ in range(10)]
    #     for f in concurrent.futures.as_completed(future_results):
    #         print(f.result())

    # to see the execution of each process that was started
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     # executes a function and returns a future object
    #     secs = [5, 4, 3, 2, 1]
    #     future_results = [executor.submit(do_something, sec) for sec in secs]
    #     for f in concurrent.futures.as_completed(future_results):
    #         print(f.result())

    # same method sa above but using map
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # executes a function and returns a future object
        secs = [5, 4, 3, 2, 1]
        future_results = executor.map(do_something, secs)
        for future_result in future_results:
            print(future_result)

    end_time = time.perf_counter()
    print(f"Finished in {round(end_time-start_time, 2)} secs")

