from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''
'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34
'''
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if res[nx][ny] != -1: #
                continue
            res[nx][ny] = res[x][y] + 1
            queue.append((nx,ny))

    return res

res = []
x, y = 0,0
for i in range(n):
    res.append([])
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            res[i].append(0)
        elif graph[i][j] == 1:
            res[i].append(-1)
        else:
            res[i].append(0)

bfs(x,y)

for i in range(n):
    for j in range(m):
        print(res[i][j], end = ' ')
    print()