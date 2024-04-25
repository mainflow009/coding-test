from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))
K.sort(reverse=True)
length = len(str(N))

while True:
    num = list(product(K, repeat=length))
    for i in num:
        cnt = int(''.join(map(str, i)))
        if cnt <= N:
            print(cnt)
            exit()
    length -= 1