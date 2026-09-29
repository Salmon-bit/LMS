def arsenal(*weapons) -> set:
    s = 0
    for w in weapons:
        s += len(w)
    x = s / len(weapons)

    output = set()
    for w in weapons:
        if len(w) <= x:
            output.add(w.title())

    return sorted(output, reverse=False)
