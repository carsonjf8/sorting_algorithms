from typing import List

# Insertion Sort
def insertion_sort(arr: List) -> List:
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
    return arr