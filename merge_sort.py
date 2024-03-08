# Merge Sort
def merge_sort(arr: list) -> list:
    return divide(arr)

def divide(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    split_index = len(arr) // 2
    arr1 = divide(arr[:split_index])
    arr2 = divide(arr[split_index:])
    return merge(arr1, arr2)

def merge(arr1: list, arr2: list) -> list:
    merged_arr = [None] * (len(arr1) + len(arr2))
    for i in range(len(merged_arr)):
        if len(arr1) == 0:
            merged_arr[i] = arr2.pop(0)
        elif len(arr2) == 0:
            merged_arr[i] = arr1.pop(0)
        else:
            min_val = None
            if arr1[0] < arr2[0]:
                min_val = arr1.pop(0)
            else:
                min_val = arr2.pop(0)
            merged_arr[i] = min_val
    return merged_arr