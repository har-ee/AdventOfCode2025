f = open("input")

raw = f.read().split("\n")
parsed = [[int(str(i)) for i in l] for l in raw]

def get_best(battery):
    l = max(battery[:-1])
    rest = battery[battery.index(l)+1:len(battery)]
    r = max(rest)
    return 10* l + r

total = sum([get_best(bat) for bat in parsed])

print(total)