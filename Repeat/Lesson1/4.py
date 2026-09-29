def scrolls(*sc):
    to_return = []
    for s in sc:
        if "elves" in s[1].lower():
            to_return.append(s[0])

    return sorted(to_return, reverse=True)


if __name__ == "__main__":
    data = [('Quenta Silmarillion', 'elves chronicles'),
            ('The Mines of Moria', 'dwarven engineering'),
            ('The Old Forest', 'huorns and elves'),
            ('The Trees of Valinor', 'elvish botany'),
            ('The Ruin of Doriath', 'elves tragedy')]
    print(*scrolls(*data), sep='\n')