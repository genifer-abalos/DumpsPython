import multiprocessing
import time

start_time = time.perf_counter()


def do_something(sleep_seconds: float):
    print(f'Sleeping {sleep_seconds}s...')
    time.sleep(sleep_seconds)
    print('Done sleeping')


if __name__ == '__main__':

    all_processes = []
    for _ in range(10):
        a_process = multiprocessing.Process(target=do_something, args=[1.9])
        a_process.start()
        all_processes.append(a_process)

    for process in all_processes:
        process.join()

    end_time = time.perf_counter()
    print(f"Finished in {round(end_time-start_time, 2)} secs")

