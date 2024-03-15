# Bubble Sort
def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i  - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr