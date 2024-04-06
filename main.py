import math


def gen_variations(elements: list[int], var_len: int,
                   repetition: bool = True,
                   order_matters: bool = True) -> list[list[int]]:

    variations: list[list[int]] = []

    for i in range(len(elements) ** var_len):
        variation: list[int] = []
        valid: bool = True

        for j in range(var_len):
            index: int = i // (len(elements) ** j) % len(elements)
            if not repetition and elements[index] in variation:
                valid = False
                break
            variation.insert(0, elements[index])

        if not order_matters and contains_set(variations, variation):
            valid = False

        if valid:
            variations.append(variation)

    return variations


def equal_sets(a: list[int], b: list[int]) -> bool:
    if len(a) != len(b):
        return False

    elements: list[int] = a.copy()
    for i in range(len(a)):
        if not b[i] in elements:
            return False
        elements.remove(b[i])
    return len(elements) == 0


def contains_set(aList: list[list[int]], aSet: list[int]) -> bool:
    for s in aList:
        if equal_sets(s, aSet):
            return True
    return False


def get_data(file_name: str, lines: int):
    data: list[tuple[int, str, int, float, float]] = []

    with open(file_name, 'r') as file:
        file.readline()
        for _ in range(lines):
            line = file.readline().strip().split(' ')
            id, town, population, latitude, longitude = line
            data.append((int(id), str(town), int(population),
                        float(latitude), float(longitude)))

    return data


print("Zadanie 1.")
print()
n: int = 4
k: int = 3
elements = list(range(1, n + 1))

i: int = 1
variations: list[list[int]] = gen_variations(elements, k, False)
for v in variations:
    print(str(i) + ". " + str(v))
    i += 1
print()

print("Zadanie 2.")
print()
n2: int = 3
m: int = 2
elements2 = list(range(1, n2 + 1))

i = 1
combinations: list[list[int]] = gen_variations(elements2, m, True, False)
for c in combinations:
    print(str(i) + ". " + str(c))
    i += 1
print()


print("Uzupelnienie 1d.")
print()
italy = get_data("italy.in", 15)
min_distance: float = math.inf
shortest_path: list[int] = []

for v in variations:
    distance: float = 0
    for vi in range(len(v) - 1):
        _, _, _, x1, y1 = italy[v[vi] - 1]
        _, _, _, x2, y2 = italy[v[vi + 1] - 1]
        distance += math.sqrt((x1 - x2) ** 2.0 + (y1 - y2) ** 2.0)

    if distance < min_distance:
        min_distance = distance
        shortest_path = v

print(shortest_path)
for id in shortest_path:
    indx: int = id - 1
    _, town, _, _, _ = italy[indx]
    print(" -> " + town, end="")
print()
print("Distance " + str(min_distance))
