weapon = int(input())

match weapon:
    case 1 | 2:
        print("Руби врага!")
    case 3:
        print("Стреляй метко!")
    case 4:
        print("Коли в цель!")
    case _:
        print("Бей врага камнем!")
