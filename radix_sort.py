import math

# Radix Sort
def radix_sort(arr: list) -> list:
    if arr == []:
        return []

    max_val = max(arr)
    digits = int(math.log10(max_val)) + 1

    for i in range(digits):
        arr = counting_sort_helper(arr, pow(10, i))
    
    return arr

def counting_sort_helper(arr: list, power: int) -> list:
    counts = [0] * 10
    for val in arr:
        counts[(val // power) % 10] += 1
    
    for i in range(9, 0, -1):
        counts[i] = counts[i - 1]
    counts[0] = 0
    for i in range(1, 10):
        counts[i] += counts[i - 1]
    
    sorted_arr = [None] * len(arr)
    for val in arr:
        sorted_arr[counts[(val // power) % 10]] = val
        counts[(val // power) % 10] += 1
    
    return sorted_arr