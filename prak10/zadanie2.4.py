def dynamic_progr(ves, price, max_ves):
    n = len(ves)
    dp = [[0 for _ in range(max_ves + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_ves + 1):
            if ves[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-ves[i-1]] + price[i-1])

    return dp[n][max_ves]
ves = [2, 3, 4, 5]
price = [3, 4, 5, 6]
max_ves = 8
max_value = dynamic_progr(ves, price, max_ves)
print(max_value)
