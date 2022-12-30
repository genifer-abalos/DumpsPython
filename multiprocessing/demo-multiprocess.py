import multiprocessing
import time

start_time = time.perf_counter()


def do_something():
    print('Sleeping 1s...')
    time.sleep(1)
    print('Done sleeping')


if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=do_something)
    process_2 = multiprocessing.Process(target=do_something)
            # pass the function name only
            # not with parenthesis since we don't want to execute it

    process_1.start()
    process_2.start()

    # join will wait until the processes finish before moving on
    process_1.join()
    process_2.join()

    end_time = time.perf_counter()
    print(f"Finished in {round(end_time-start_time, 2)} secs")




