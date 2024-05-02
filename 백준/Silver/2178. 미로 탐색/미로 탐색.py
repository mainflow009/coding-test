from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append((0,0))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if visited[nx][ny] == False and graph[nx][ny]== 1:
                queue.append((nx,ny))
                visited[nx][ny] =True
                graph[nx][ny] = graph[x][y] + 1
                
bfs()
print(graph[N-1][M-1])