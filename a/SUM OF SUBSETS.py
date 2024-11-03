
# Sum of Subsets

# Time Complexity : O(2^N)
# Space Complexity : O(N)

def subsetsum(arr, k):
    arr.sort()
    res = []
    
    def backtrack(i, currsum, subset):
        if currsum == k:
            res.append(subset.copy())
            return
        if currsum > k: return
        for j in range(i, len(arr)):
            subset.append(arr[j])
            backtrack(j + 1, currsum + arr[j], subset)
            subset.pop()
    backtrack(0, 0, [])
    return res

def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(subsetsum(arr, k))
    return 0

if __name__ == "__main__":
    main()