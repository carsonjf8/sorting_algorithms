from typing import Callable, List, NoReturn
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

SORTING_FUNC_DICT = {
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Bubble Sort': bubble_sort,
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
        print(output_arr == expected_output, output_arr, expected_output)
        assert sort_func(arr) == expected_output
    except:
        print(arr, 'does not match', expected_output)

def test(sort_func: Callable) -> NoReturn:
    for (input_arr, sorted_arr) in zip(TEST_CASES_INPUT, TEST_CASES_OUTPUT):
        test_case(sort_func, input_arr, sorted_arr)

def test_all_sorters() -> NoReturn:
    for sort_func in SORTING_FUNC_DICT:
        print('Testing ' + sort_func + '...')
        test(SORTING_FUNC_DICT[sort_func])
        print('...Done')
        print()

if __name__ == '__main__':
    test_all_sorters()