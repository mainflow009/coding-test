import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))


res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x = max(res, nums[i]+nums[j]+nums[k])
            if x<=M:
                res = x

print(res)
