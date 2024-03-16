# Heap Sort
def heap_sort(arr: list) -> list:
    if arr == []:
        return []
    
    sorted_arr = []

    first_non_leaf = len(arr) // 2 - 1
    for i in range(first_non_leaf, -1, -1):
        min_heapify(arr, i)

    while len(arr) > 1:
        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
        sorted_arr.append(arr[len(arr) - 1])
        arr = arr[:-1]
        min_heapify(arr, 0)
    sorted_arr.append(arr[0])

    return sorted_arr

def min_heapify(arr: list, index: int) -> None:
    arr_len = len(arr)
    smallest = index
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2

    if left_child_index < arr_len and arr[left_child_index] < arr[smallest]:
        smallest = left_child_index
    if right_child_index < arr_len and arr[right_child_index] < arr[smallest]:
        smallest = right_child_index

    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        min_heapify(arr, smallest)
