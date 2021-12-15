data = open('data.txt', 'r')
input_list = data.read().split('\n')
data.close()

depth = 0
length = 0

for instr in input_list:
    command = instr.split(' ')[0]
    distance = int(instr.split(' ')[1])

    if(command == 'forward'):
        length += distance
    elif(command == 'up'):
        depth -= distance
    else:
        depth += distance

print(abs(depth) * abs(length))