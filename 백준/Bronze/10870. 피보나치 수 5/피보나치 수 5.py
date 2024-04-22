N = int(input())

def fibo(N):
    if N > 2:
        return fibo(N-1) + fibo(N-2)
    elif N == 1:
        return 1
    elif N == 0:
        return 0
    else:
        return 1
    
print(fibo(N))