from collections import deque

toys_materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while toys_materials and magic_levels:
    material = toys_materials.pop() if magic_levels[0] or not toys_materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        toys_materials.append(material + magic_level)
    elif product > 0:
        toys_materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if toys_materials:
    print(f"Materials left: {', '.join([str(x) for x in toys_materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
