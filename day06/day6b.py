from functools import reduce
from operator import mul, add

f = open("input")

raw = f.read().split("\n")

ops = {
    '+': add,
    '*': mul,
}

def split_sums(rows):
    split_rows = [[]]
    for row in rows:
        if [r for r in row if r != ' ']:
            split_rows[-1].append(row)
        else:
            split_rows.append([])
    return split_rows

def parse_calc(rows):
    op = rows[0][-1]
    nums = [int(''.join([i for i in r if i.isdigit()])) for r in rows]
    return op, nums

def calc(rows):
    op, nums = parse_calc(rows)
    return reduce(ops[op], nums)

transposed = zip(*raw)
split = split_sums(transposed)

result = sum([calc(l) for l in split])
print(result)