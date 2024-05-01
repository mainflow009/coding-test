from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
res = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft() 
        for i in graph[v]:
            if not visited[i]:
                res[i] = v
                queue.append(i)
                visited[i] = True

bfs(1)

for i in range(2, N+1):
    print(res[i])