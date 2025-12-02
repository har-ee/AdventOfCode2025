f = open("input")

raw = f.read().split(",")
print(raw)

def parse(line):
    split_str = line.split("-")
    return int(split_str[0]), int(split_str[1])

def gen_repeated(max):
    repeated = set()

    i = 1
    while True:
        i1 = int(str(i) * 2)
        repeated.add(i1)
        if i1 > max:
            return repeated
        i += 1

def in_range(id, min, max):
    return id >= min and id <= max

inputs = [parse(l) for l in raw]
maximum = max([max([a, b]) for a,b in inputs])

invalid_ids = gen_repeated(maximum)

num_invalid = 0
for id in invalid_ids:
    for min, max in inputs:
        if in_range(id, min, max):
            num_invalid += id
            break

print(num_invalid)