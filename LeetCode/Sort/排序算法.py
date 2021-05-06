"""
冒泡排序
"""
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubbleSort_opt(arr):

    for i in range(1, len(arr)):
        swap = False
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    return arr

"""
选择排序
"""
def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

"""
插入排序
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr

"""
希尔排序
"""
def shellSort(arr):
    import math
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr

def shellSort1(arr):
    import math
    length = len(arr)
    gap = math.floor(length / 2)
    while gap:
        for i in range(gap, length):
            j = i
            current = arr[i]
            while j - gap >=0 and current < arr[j - gap]:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = current
        gap = math.floor(gap / 2)
    return arr

"""
归并排序
"""
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

"""
快速排序
"""
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


"""
堆排序
"""
def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr

def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def buildMaxHeap(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)


"""
计数排序
"""
def countingSort(arr, maxValue):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr

"""
桶排序
"""
def buckectSort(arr):
    min_num = min(arr)
    max_num = max(arr)
    bucket_range = (max_num - min_num) / len(arr) + 1
    count_list = [[] for i in range(bucket_range)]
    for i in arr:
        count_list[(i - min_num) // len(arr)].append(i)
    arr.clear()
    for i in count_list:
        for j in sorted(i):
            arr.append(j)

"""
基数排序
"""
def radixSort(arr):
    n = len(str(max(arr)))
    for i in range(n):
        bucket_list = [[] for _ in range(10)]
        for j in arr:
            bucket_list[j // (10 ** i) % 10].append(j)
        arr = [b for a in bucket_list for b in a]
    return arr



if __name__ == '__main__':
    print(countingSort([5,8,7,9,1,6,4,3,2,0, 4,3,2,1], 9))