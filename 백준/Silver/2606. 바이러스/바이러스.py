import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
# 비어있는 시작 노드 첫번쨰

for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = 0 
visited = [False] * (n+1)
def BFS(start):
    global res
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                res += 1
    
    return res

print(BFS(1))