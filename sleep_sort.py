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

import random
def generate_rand_tests(max_len: int, max_val: int) -> tuple[list, list]:
    case_len = random.randint(0, max_len)
    case_input = []
    for j in range(case_len):
        case_input.append(random.randint(0, max_val))
    return case_input, sorted(case_input)
