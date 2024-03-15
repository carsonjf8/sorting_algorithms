# Quick Sort
def quick_sort(arr: list, start: int=None, end: int=None) -> list:
    if start == None:
        start = 0
    if end == None:
        end = len(arr) - 1
    
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index)
        quick_sort(arr, pivot_index + 1, end)
    
    return arr

def partition(arr: list, start: int, end: int) -> list:
    pivot_index = get_pivot_index(arr, start, end)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    division = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[division] = arr[division], arr[i]
            division += 1
    arr[division], arr[end] = arr[end], arr[division]

    return division

def get_pivot_index(arr: list, start: int, end: int) -> int:
    middle = (end + start) // 2

    if ((arr[start] <= arr[end] and arr[start] <= arr[middle] and arr[middle] <= arr[end]) or # arr[start] <= arr[middle] <= arr[end]
        (arr[end] <= arr[start] and arr[end] <= arr[middle] and arr[middle] <= arr[start])): # arr[end] <= arr[middle] <= arr[start]
        return middle
    elif ((arr[middle] <= arr[end] and arr[middle] <= arr[start] and arr[start] <= arr[end]) or # arr[middle] <= arr[start] <= arr[end]
        (arr[end] <= arr[middle] and arr[end] <= arr[start] and arr[start] <= arr[middle])): # arr[end] <= arr[start] <= arr[middle]
        return start
    elif ((arr[start] <= arr[middle] and arr[start] <= arr[end] and arr[end] <= arr[middle]) or # arr[start] <= arr[end] <= arr[middle]
        (arr[middle] <= arr[start] and arr[middle] <= arr[end] and arr[end] <= arr[start])): # arr[middle] <= arr[end] <= arr[start]
        return end
