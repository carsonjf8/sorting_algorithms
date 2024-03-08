from typing import List

# Insertion Sort
def insertion_sort(data: List) -> List:
    for i in range(len(data) - 1):
        if data[i + 1] < data[i]:
            temp = data[i]
            data[i + 1] = data[i]
            data[i] = temp

            for j in range(i, 0, -1):
                if data[j] < data[j - 1]:
                    temp = data[j]
                    data[j - 1] = data[j]
                    data[j] = temp
                else:
                    break
    
    return data