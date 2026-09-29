n, m = map(int, input().split())

time = 0
last_add = -1
while n < m:
    n += last_add + 2
    last_add += 2
    time += 1

print(f"Время - {time}.")
print(f"Количество дозорных - {n}.")