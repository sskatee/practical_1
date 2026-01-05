#Задачи продвинутого уровня

#1
def stairs(n):
    if n <= 1:
        return 1
    x = [0] * (n + 1)
    x[0], x[1] = 1, 1
    for i in range(2, n + 1):
        x[i] = x[i - 1] + x[i - 2]
    return x[n]

print(stairs(5))  # ответ 8

#2
def max_sum(nums):
    max_cur = max_glob = nums[0]
    for x in nums[1:]:
        max_cur = max(x, max_cur + x)
        max_glob = max(max_glob, max_cur)
    return max_glob

print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  #ответ 6

#3
def min_coins(n, coins=[1, 3, 4]):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for s in range(1, n + 1):
        for coin in coins:
            if s - coin >= 0:
                dp[s] = min(dp[s], dp[s - coin] + 1)
    return dp[n]

print(min_coins(6))  # ответ 2 (3+3)

#4
def red_count(s1,s2):
    n = len(s1)
    count = 0

    for i in range(n):
        if s1[i] != s2[i]:
            count += 1
    return count

print(red_count('maybe','table')) # ответ 3
