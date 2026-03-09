def max_weight(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        start, end, weight = intervals[i - 1]
        j = 0
        for k in range(i - 1, 0, -1):
            if intervals[k - 1][1] <= start:
                j = k
                break
        dp[i] = max(dp[i - 1], dp[j] + weight)
        

    return dp[n]


a = [(1, 2, 5), (3, 4, 2), (1, 3, 6),(1, 9, 12),(4, 6, 5)]
print(max_weight(a))
