import sys
input = sys.stdin.readline
from itertools import combinations

hobits = []
for _ in range(9):
    hobits.append(int(input()))

hobits.sort()
total = sum(hobits)
tmp = 0

for _ in combinations(hobits, 2):
    tmp = sum(_)
    if total - tmp == 100:
        a, b = hobits.index(_[0]), hobits.index(_[1])


for _ in range(9):
    if _ == a or _ == b:
        pass
    else:
        print(hobits[_])