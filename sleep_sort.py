from threading import Thread
import time

# Sleep Sort
def sleep_sort(arr: list) -> list:
    sorted_arr = []
    threads_list = []
    
    for val in arr:
        thread = Thread(target=thread_run, args=(val, sorted_arr))
        threads_list.append(thread)
        thread.start()
    
    for thread in threads_list:
        thread.join()
    
    return sorted_arr

def thread_run(val: int, arr: list) -> None:
    time.sleep(val)
    arr.append(val)
