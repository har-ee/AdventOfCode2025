from functools import reduce

f = open("input")

lines = f.readlines()

def step(beams_count, line):
    beams, count = beams_count
    next_beams = set()
    for b in beams:
        obstacle = line[b]
        if obstacle == '^':
            count += 1
        next_beams = next_beams.union(next_pos(b, line[b]))
    return (next_beams, count)

def next_pos(position, obstacle):
    if obstacle == '.':
        return set([position])
    elif obstacle == '^':
        return set([position-1, position+1])

start = lines[0].index('S')

beams = set([start])
count = 0
beams, count = reduce(step, lines[1:], (beams, count))

print(count)
