import sys
input = sys.stdin.readline

def cantorian(n):
    if n == 1:
        return "-"
    
    cant_part = cantorian(n//3)
    result = cant_part + " " * (n//3) + cant_part

    return result

while True:
    try:
        N = int(input())
        print(cantorian(3**N))
    except:
        break