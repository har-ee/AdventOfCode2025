f = open("input")

raw = f.read().split("\n")
parsed = [[int(str(i)) for i in l] for l in raw]

def get_best(battery, length):
    total_str = ""
    rest = battery
    for i in range(length):
        buffer = length-i-1
        if buffer == 0:
            l = max(rest)
        else:
            l = max(rest[:-buffer])
        rest = rest[rest.index(l)+1:]
        total_str += str(l)
    return int(total_str)

total = sum([get_best(bat, 12) for bat in parsed])

print(total)