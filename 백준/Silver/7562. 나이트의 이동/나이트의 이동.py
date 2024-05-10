from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())

def bfs():
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    queue = deque()
    queue.append((startx, starty))
    while queue:
        x, y = queue.popleft()
        if x == endx and y == endy:
            return graph[x][y] - 1 # 1부터 시작했으니 목적지 도달시 1 빼줌
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0: # 아직 목적지가 아니라면
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for _ in range(T):
    l = int(input().rstrip())
    startx, starty = map(int, input().rstrip().split())
    endx, endy = map(int, input().rstrip().split())
    graph = [[0] * l for _ in range(l)]
    graph[startx][starty] = 1
    print(bfs())