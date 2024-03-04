import sys
input = sys.stdin.readline

N,M=map(int, input().split())
res = []

def back(num):
    if len(res)==M:
        print(" ".join(map(str, res)))
        return
    for i in range(num,N+1):
        res.append(i)
        back(i)
        res.pop()

back(1)