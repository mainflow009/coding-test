from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    res = 1
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if jido[ny][nx]==1 and chk[ny][nx]==False:
                    res += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return res

cnt = 0
maxV = 0
for j in range(n):
    for i in range(m):
        if jido[j][i]==1 and chk[j][i]==False:
            chk[j][i]=True
            cnt += 1
            maxV = max(maxV, bfs(j,i))

print(cnt)
print(maxV)