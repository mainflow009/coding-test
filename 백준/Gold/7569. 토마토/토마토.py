from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
chest = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue

            if chest[nx][ny][nz] == 0:
                chest[nx][ny][nz] = chest[x][y][z] + 1
                queue.append((nx,ny,nz))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if chest[i][j][k] == 1:
                queue.append((i,j,k))

bfs()

res = 0
tmp = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if chest[i][j][k] == 0:
                tmp = True
            res = max(res, chest[i][j][k])

if tmp:
    print(-1)
else:
    print(res-1)