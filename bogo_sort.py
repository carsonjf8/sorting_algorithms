import random

# Bogo Sort
def bogo_sort(arr: list) -> list:
    is_sorted = False
    while not is_sorted:
        random.shuffle(arr)

        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                break
    return arr