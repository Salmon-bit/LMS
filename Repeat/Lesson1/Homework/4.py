def potions(string: str) -> list[str]:
    with open("./recipes.txt", 'r', encoding="UTF-8") as f:
        data = f.readlines()[::-1]

    for potion in data:
        if string.lower() in potion.strip().split(',')[0].lower():
            return potion.strip().split(',')[1:]
