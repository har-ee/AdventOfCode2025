f = open("input")

raw = f.readlines()

class instruction:
    def __init__(self, input_str):
        self.dir = input_str[0]
        self.distance = int(input_str[1:])

dirmap = {
    "R" : 1,
    "L" : -1
}

instructions = [instruction(str) for str in raw]

direction = 50

password = 0
for instruction in instructions:
    sign = dirmap[instruction.dir]
    movement = (instruction.distance * sign)
    destination = (direction + movement)

    intermediate = range(direction + sign, destination + sign, sign)
    password += sum([1 for i in intermediate if i % 100 == 0])

    direction = destination
    
print(password)