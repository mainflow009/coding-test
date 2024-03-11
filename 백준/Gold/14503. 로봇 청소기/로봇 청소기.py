import sys
input= sys.stdin.readline

N, M = map(int, input().split())
y,x,d = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 0 : not cleared
# 1 : blocked
# 2 : cleared

while True:
    if jido[y][x] == 0:
        jido[y][x] = 2 # clear current location 
        cnt += 1

    sw = False
    for i in range(1,5):
        ny = y + dy[d-i]
        # d : current stare
        # d-i : next stare
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M:
            if jido[ny][nx] == 0:
                d = (d-i+4)%4 # rotate
                y = ny
                x = nx
                sw = True
                break
    
    if sw == False:
        ny = y - dy[d] # go to back
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if jido[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)