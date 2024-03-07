from typing import List

# Selection Sort
def selection_sort(data: List) -> List:
    for i in range(len(data)):
        min_val_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_val_index]:
                min_val_index = j
        temp = data[i]
        data[i] = data[min_val_index]
        data[min_val_index] = temp
    return data