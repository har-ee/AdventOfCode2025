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
    direction = (direction + (instruction.distance * dirmap[instruction.dir])) % 100
    if direction == 0:
        password += 1
        
print(password)