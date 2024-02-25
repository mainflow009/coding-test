'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

import sys

input = sys.stdin.readline

N = int(input())
jido = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

res = []
each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4): #4방향 살피기
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if jido[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if jido[j][i] == 1 and chk[j][i] == False:
           chk[j][i] = True
           each = 0
           dfs(j,i)
           res.append(each)

res.sort()
print(len(res))
for i in res:
    print(i)