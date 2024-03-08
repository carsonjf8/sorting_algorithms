from typing import Callable, List, NoReturn
import random
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort

SORTING_FUNC_DICT = {
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Bubble Sort': bubble_sort,
    'Merge Sort': merge_sort,
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

def test_case(sort_func: Callable, arr: List, expected_output: List) -> NoReturn:
    try:
        output_arr = sort_func(arr)
        #print(output_arr == expected_output, output_arr, expected_output)
        assert output_arr == expected_output
    except:
        print(output_arr, 'does not match', expected_output)

def test(sort_func: Callable, test_input: List, test_output: List) -> NoReturn:
    for (input_arr, sorted_arr) in zip(test_input, test_output):
        test_case(sort_func, input_arr, sorted_arr)

def test_all_sorters(test_type) -> NoReturn:
    if test_type == 'custom':
        test_input, test_output = TEST_CASES_INPUT, TEST_CASES_OUTPUT
    elif test_type == 'random':
        count = 50
        max_len = 100
        max_val = 100
        test_input, test_output = generate_rand_tests(count, max_len, max_val)
    
    for sort_func in SORTING_FUNC_DICT:
        print('Testing ' + sort_func + '...')
        test(SORTING_FUNC_DICT[sort_func], test_input, test_output)
        print('...Done')
        print()

def generate_rand_tests(count: int, max_len: int, max_val: int) -> tuple[List, List]:
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

if __name__ == '__main__':
    test_all_sorters('random')