N, K = map(int, input().split())
cnt = 0

for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            time = str(hour).zfill(2) + str(minute).zfill(2) + str(second).zfill(2)
            if str(K) in time:
                cnt += 1

print(cnt)