import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
s,e,cnt = 0,1,0

each = 0

while True:
    if s>e or e>N:
        break
    each = sum(nums[s:e])
    if each < M:
        e += 1
    elif each > M:
        s += 1
    else:
        cnt += 1
        e += 1

print(cnt)