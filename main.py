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


# 1.
print("1.")
print()
n: int = 4
k: int = 3
elements = list(range(1, n + 1))

for v in gen_variations(elements, k, False):
    print(v)
print()

# 2.
print("2.")
print()
n2: int = 3
m: int = 2
elements2 = list(range(1, n2 + 1))

for v in gen_variations(elements2, m, True, False):
    print(v)
print()
