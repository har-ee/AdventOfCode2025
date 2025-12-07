from functools import reduce

f = open("input")

lines = f.readlines()

def step(beams, line):
    next_beams = {}
    for b in beams:
        for p in next_pos(b, line[b]):
            if p in next_beams:
                next_beams[p] += beams[b]
            else:
                next_beams[p] = beams[b] 
    return next_beams

def next_pos(position, obstacle):
    if obstacle == '.':
        return set([position])
    elif obstacle == '^':
        return set([position-1, position+1])

start = lines[0].index('S')

beams = {start: 1}
beams = reduce(step, lines[1:], beams)

result = sum(beams.values())

print(result)
