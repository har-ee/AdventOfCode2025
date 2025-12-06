f = open("input")

[raw_ranges, raw_ingredients] = f.read().split("\n\n")
ranges = [[int(i) for i in r.split('-')] for r in raw_ranges.split("\n")]
ingredients = [int(i) for i in raw_ingredients.split("\n")]

def in_range(min, max, n):
    return n >= min and n <= max

num_fresh = 0
for i in ingredients:
    for min, max in ranges:
        if in_range(min, max, i):
            num_fresh += 1
            break
print(num_fresh)