#Задачи продвинутого уровня

#1
def climb_stairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climb_stairs(5))  # 8

#2
def max_subarray(nums):
    max_current = max_global = nums[0]
    for x in nums[1:]:
        max_current = max(x, max_current + x)
        max_global = max(max_global, max_current)
    return max_global

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

#3
def min_coins(n, coins=[1, 3, 4]):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for s in range(1, n + 1):
        for coin in coins:
            if s - coin >= 0:
                dp[s] = min(dp[s], dp[s - coin] + 1)
    return dp[n]

print(min_coins(6))  # 2 (3+3)

#4
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1],
                                   dp[i - 1][j - 1])
    return dp[m][n]

print(levenshtein_distance("kitten", "sitting"))  # 3