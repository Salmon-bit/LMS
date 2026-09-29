def path(places, criterion):
    save_path = []
    for i in range(len(places)):
        if criterion(places[i]) and i == 0:
            return "Danger!"

        if not criterion(places[i]):
            save_path.append(places[i])
        else:
            return ', '.join(save_path)

    return ', '.join(save_path)


if __name__ == "__main__":
    def func(line):
        return len(line.split()) == 2

    data = ['Hobbiton', 'Bywater',
            'The Green Dragon', 'Bucklebury',
            'Brandywine Bridge', 'The Old Forest']
    print(path(data, criterion=func))