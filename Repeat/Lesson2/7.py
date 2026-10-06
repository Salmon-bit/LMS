import random
from openpyxl import Workbook

enemy_string = input()

enemy_types = [
    enemy.strip()
    for enemy in enemy_string.split(", ")
    if enemy.strip()
]

workbook = Workbook()
sheet = workbook.active
sheet.title = "Враги"

sheet.append(["Тип войск", "Количество", "Опасность"])

total_enemies = 0

for enemy_type in enemy_types:
    quantity = random.randint(50, 500)
    danger = random.randint(1, 10)

    sheet.append([enemy_type, quantity, danger])
    total_enemies += quantity

sheet.append(["ИТОГО", total_enemies, None])

sheet.column_dimensions["A"].width = 20
sheet.column_dimensions["B"].width = 15
sheet.column_dimensions["C"].width = 12

workbook.save("enemies.xlsx")
