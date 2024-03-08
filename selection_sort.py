# Selection Sort
def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_val_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_val_index]:
                min_val_index = j
        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]
    return arr