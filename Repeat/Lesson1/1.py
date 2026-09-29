heights = list(map(int, input().split()))

for h in heights:
    if not(h >= 90 and h <= 140):
        print("Оставайся в Шире")
    else:
        print("Можешь идти")
