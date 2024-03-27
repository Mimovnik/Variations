def gen_variations(elements: list[int], var_len: int,
                   repetition: bool = True) -> list[list[int]]:

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

        if valid:
            variations.append(variation)

    return variations


n: int = 5
elements = list(range(1, n + 1))

for v in gen_variations(elements, n, False):
    print(v)
