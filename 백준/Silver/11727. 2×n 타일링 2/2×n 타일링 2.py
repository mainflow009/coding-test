n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for _ in range(2,n+1):
    dp[_] = dp[_-2] * 2 + dp[_-1]

print(dp[n] % 10007)