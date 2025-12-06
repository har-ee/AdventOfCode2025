f = open("input")

[raw_ranges, raw_ingredients] = f.read().split("\n\n")
ranges = [tuple([int(i) for i in r.split('-')]) for r in raw_ranges.split("\n")]
ingredients = [int(i) for i in raw_ingredients.split("\n")]


def squash_range(i1, i2, j1, j2):
    if (j1 <= i1 and i1 <= j2) or (i1 <= j2 and j2 <= i2):
        return (min(i1, j1), max(i2, j2))
    return None

cur_ranges = set(ranges)
while True:
    next_ranges = set()
    for i1, i2 in cur_ranges:
        new_range = None
        for j1, j2 in cur_ranges:
            if i1 == j1 and i2 == j2:
                continue
            new_range = squash_range(i1, i2, j1, j2)
            if new_range != None:
                next_ranges.add(new_range)
                break
        if new_range == None:
            next_ranges.add((i1, i2))
    if cur_ranges == next_ranges:
        break
    cur_ranges = next_ranges

result = sum([j - i + 1 for i, j in cur_ranges])

print(result)