from functools import reduce
from operator import mul, add

f = open("input")

raw = [l.split() for l in f.read().split("\n")]

ops = {
    '+': add,
    '*': mul,
}

def calc(line):
    op = line[-1]
    nums = [int(i) for i in line[:-1]]
    return reduce(ops[op], nums)

sums = zip(*raw)

result = sum([calc(l) for l in sums])
print(result)