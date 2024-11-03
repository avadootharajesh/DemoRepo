
# Merge Sort

def mergesort(arr, left, right):
    if len(arr) < 1: return arr
    mid = left + (right - left) // 2
    mergesort(arr, left, mid)
    mergesort(arr, mid + 1, right)
    merge(arr, left, mid, right)
    
def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    for k in range(i, mid + 1): temp.append(arr[k])
    for k in range(j, right + 1): temp.append(arr[k])
    for k in range(left, right + 1): arr[k] = temp[k - left]
    
def main():
    arr = list(map(int, input().split()))
    mergesort(arr, 0, len(arr) - 1)
    print(arr)
    
if __name__ == '__main__': main()