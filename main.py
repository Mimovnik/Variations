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


print()
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
n2: int = 4
m: int = 3
elements2 = list(range(1, n2 + 1))

i = 1
combinations: list[list[int]] = gen_variations(elements2, m, True, False)
for c in combinations:
    print(str(i) + ". " + str(c))
    i += 1

print()
print("Uzupelnienie 1d.")
print()
data = get_data("italy.in", 15)
min_distance: float = math.inf
shortest_path: list[int] = []

for v in variations:
    distance: float = 0
    for vi in range(len(v) - 1):
        _, _, _, x1, y1 = data[v[vi] - 1]
        _, _, _, x2, y2 = data[v[vi + 1] - 1]
        distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance < min_distance:
        min_distance = distance
        shortest_path = v

print(shortest_path)
i = 0
for id in shortest_path:
    _, town, _, _, _ = data[id - 1]
    if i == 0:
        print(town, end="")
    else:
        print(" -> " + town, end="")
    i += 1
print()
print("Distance " + str(min_distance))

print()
print("Uzupelnienie 2d.")
print()

combinations = gen_variations(elements2, m, False, False)
greatest_average: float = -math.inf
cities_with_greatest_average: list[int] = []

for c in combinations:
    population_sum: int = 0
    for ci in range(len(c)):
        _, _, population, _, _ = data[c[ci] - 1]
        population_sum += population
    average: float = population_sum / len(c)
    if average > greatest_average:
        greatest_average = average
        cities_with_greatest_average = c

print(cities_with_greatest_average)
i = 0
for id in cities_with_greatest_average:
    _, town, _, _, _ = data[id - 1]
    if i == 0:
        print(town, end="")
    else:
        print(", " + town, end="")
    i += 1
print()
print("Average population " + str(greatest_average))
