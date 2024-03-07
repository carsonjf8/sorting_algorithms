from typing import Callable, List, NoReturn
from selection_sort import selection_sort

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

def test_case(sort_func: Callable, data: List, expected_output: List) -> NoReturn:
    try:
        assert sort_func(data) == expected_output
    except:
        print(data, 'does not match', expected_output)

def test(sort_func: Callable) -> NoReturn:
    for (input_data, sorted_data) in zip(TEST_CASES_INPUT, TEST_CASES_OUTPUT):
        test_case(sort_func, input_data, sorted_data)

print('Testing Selection Sort...')
test(selection_sort)
print('...Done')
