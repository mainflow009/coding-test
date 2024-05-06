from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
Gs = [list(map(int, input().split())) for _ in range(N)]
map = []
price = 200 * 5 * 3

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(coordinates):
    global price
    visited = []
    total = 0
    for x, y in coordinates:
        visited.append((x,y))
        total += Gs[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) not in visited:
                total += Gs[nx][ny]
                visited.append((nx,ny))

            else:
                return
    
    price = min(price, total)

for i in range(1, N-1):
    for j in range(1, N-1):
        map.append((i,j))

for i in combinations(map, 3):
    bfs(i)

print(price)