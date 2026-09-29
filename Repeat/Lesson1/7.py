import csv
import json

with open("members.csv", 'r', encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)[1:]

l1 = []
races_indexes = {}

for person in data:
    name = person[1]
    race = person[2]
    age = person[3]

    if races_indexes.get(race, None) is None:
        races_indexes[race] = len(l1)
        l1.append({"race": race, "members": [name]})
    else:
        l1[races_indexes[race]]["members"] = l1[races_indexes[race]]["members"] + [name]

for r in l1:
    r["members"] = sorted(r["members"], key=lambda x: (-len(x), x))

l1.sort(key=lambda x: x['race'])

with open("council.jsonlines", 'w', encoding="UTF-8") as f:
    output = ""
    for r in l1:
        output += json.dumps(r) + "\n"
    print(output.strip(), file=f)