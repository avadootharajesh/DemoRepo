
# Quick Sort : Approach 1

def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[-1]
    return quicksort([x for x in arr[:-1] if x <= pivot]) + [pivot] + quicksort([x for x in arr[:-1] if x > pivot])

def main():
    arr = list(map(int, input().split()))
    print(quicksort(arr))

if __name__ == '__main__': main()


# Quick Sort : Approach 2

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    arr = list(map(int, input().split()))
    quicksort(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == '__main__': main()