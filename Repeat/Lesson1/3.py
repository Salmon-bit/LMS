vowels = "aoueiy"

while n := input():
    if len(n) < 4:
        print("Слишком короткое.")
        continue
    elif len(n) >= 20:
        print("Слишком длинное.")
        continue
    elif n[0].lower() not in vowels:
        print("Неверное начало.")
        continue
    elif n[-1].lower() in vowels:
        print("Неверный конец.")
        continue

    need_to_continue = False
    for i in range(1, len(n)):
        a = n[i - 1].lower()
        b = n[i].lower()
        if a in vowels and b in vowels:
            print(f"Две гласные {a}{b} подряд.")
            need_to_continue = True
            break

    if need_to_continue:
        continue

    print("Красиво!")