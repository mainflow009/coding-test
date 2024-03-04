import sys
input = sys.stdin.readline

N,M = map(int, input().split())
res = []

def back(num):
    if len(res)==M:
        print(" ".join(map(str, res)))
        return
    for i in range(num, N+1):
        if i not in res:
            res.append(i)
            back(i+1)
            res.pop()

back(1)