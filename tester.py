import time
import random

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from radix_sort import radix_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from sleep_sort import sleep_sort
from bogo_sort import bogo_sort

SORTING_FUNC_DICT = {
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Bubble Sort': bubble_sort,
    'Merge Sort': merge_sort,
    'Radix Sort': radix_sort,
    'Quick Sort': quick_sort,
    'Heap Sort': heap_sort,
    #'Sleep Sort': sleep_sort, # disabled from testing due to how long it takes
    #'Bogo Sort': bogo_sort, # disabled from testing due to how long it takes
}

TEST_CASES_INPUT = [
    [],
    [1, 2, 3, 4, 5],
    [2, 7, 3, 9, 0, 2, 2, 5],
    [5, 4, 3, 2, 1],
]

TEST_CASES_OUTPUT = [
    [],
    [1, 2, 3, 4, 5],
    [0, 2, 2, 2, 3, 5, 7, 9],
    [1, 2, 3, 4, 5],
]

def test_all_sorters(test_type: str) -> None:
    if test_type == 'custom':
        print('Using custom tests\n')
        test_input, test_output = TEST_CASES_INPUT, TEST_CASES_OUTPUT
    elif test_type == 'random':
        count = 1000
        max_len = 1000
        max_val = 1000
        print('Using random tests: count={}, max_len={}, max_val={}\n'.format(count, max_len, max_val))
        test_input, test_output = generate_rand_tests(count, max_len, max_val)
    
    for sort_func in SORTING_FUNC_DICT:
        print('Testing ' + sort_func + '...')
        time_start = time.time()
        test(SORTING_FUNC_DICT[sort_func], test_input, test_output)
        time_end = time.time()
        total_time = time_end - time_start
        print('...Done (' + str(total_time) + 's)')
        print()

def generate_rand_tests(count: int, max_len: int, max_val: int) -> tuple[list, list]:
    test_inputs = []
    test_outputs = []

    for i in range(count):
        case_len = random.randint(0, max_len)
        case_input = []
        for j in range(case_len):
            case_input.append(random.randint(0, max_val))
        test_inputs.append(case_input)
        test_outputs.append(sorted(case_input))

    return test_inputs, test_outputs

def test(sort_func: callable, test_input: list, test_output: list) -> None:
    for (input_arr, sorted_arr) in zip(test_input, test_output):
        test_case(sort_func, input_arr.copy(), sorted_arr.copy())
        
def test_case(sort_func: callable, arr: list, expected_output: list) -> None:
    try:
        #print(arr, expected_output)
        output_arr = sort_func(arr)
        #print(output_arr == expected_output, output_arr, expected_output)
        assert output_arr == expected_output
    except:
        print(output_arr, 'does not match', expected_output)

if __name__ == '__main__':
    #test_all_sorters('custom')
    test_all_sorters('random')