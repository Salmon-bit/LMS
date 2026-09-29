import json

with open("rings.txt", 'r', encoding="UTF-8") as f:
    data = f.readlines()

max_power = 0
strongest_ring = {
    "title": "",
    "material": "",
    "keeper": "",
    "power": 0,
    "visibility": ""
}
for ring in data:
    title, material, keeper, power = ring.split()
    power = int(power)
    visibility = "visible" if (len(title) + len(keeper) + power) % 2 == 0 else "invisible"
    if power >= max_power:
        strongest_ring["title"] = title
        strongest_ring["material"] = material
        strongest_ring["keeper"] = keeper
        strongest_ring["power"] = power
        strongest_ring["visibility"] = visibility
        max_power = power

with open("powerful.json", 'w', encoding="UTF-8") as f:
    json.dump(strongest_ring, f)