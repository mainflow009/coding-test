n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for _ in range(2, n+1):
    dp[_] = dp[_-1] + dp[_-2]

print(dp[n])
