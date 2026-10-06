def travel(map_file: str, key=max):
    m = []
    with open(map_file, 'r', encoding="UTF-8") as f:  # Читаем карту
        m = [list(map(int, line.strip().split())) for line in f.readlines()]

    pos = [0, 0]  # Изначальная позиция
    max_right = len(m[0]) - 1  # Правый край карты
    max_down = len(m) - 1  # Нижний край карты
    hp = m[0][0]  # Базовое здоровье

    while pos != (max_down, max_right):  # Нижний правый угол карты
        if pos[1] < max_right and pos[0] < max_down:  # Ходим куда угодно
            var_1 = m[pos[0] + 1][pos[1]]
            var_2 = m[pos[0]][pos[1] + 1]

            best_choice = key(var_1, var_2)
            if best_choice == var_1:  # Ходим вниз
                pos[0] += 1
            else:  # Ходим вправо
                pos[1] += 1
            hp += best_choice  # Обновляем необходимое здоровье
        elif pos[1] < max_right and pos[0] == max_down:  # Ходим только вправо
            hp += m[pos[0]][pos[1] + 1]
            pos[1] += 1
        elif pos[0] < max_down and pos[1] == max_right:  # Ходим только вниз
            hp += m[pos[0] + 1][pos[1]]
            pos[0] += 1
        else:  # Если условие выхода не сработает
            break

    return hp


if __name__ == "__main__":
    print(travel('map.txt', key=max))
