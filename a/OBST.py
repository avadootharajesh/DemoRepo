
# OBST using Dynamic Programming

def sumfreq(freq, i, j):
    return sum(freq[i:j+1])

def obst(keys, freq, n):
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1): cost[i][i] = freq[i-1]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            cost[i][j] = float('inf')
            for r in range(i, j+1):
                c = (cost[i][r-1] if r > i else 0) + (cost[r+1][j] if r < j else 0) + sumfreq(freq, i, j)
                if c < cost[i][j]: cost[i][j] = c
    return cost[0][n-1]

if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print(obst(keys, freq, n))