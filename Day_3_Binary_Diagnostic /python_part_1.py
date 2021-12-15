data = open('data.txt', 'r')
input_list = data.read().split('\n')
data.close()


length = len(input_list[0])
def to_decimal(exp):
    number = 0
    multiplier = 1

    c = len(exp) - 1
    while c > -1:
        number += (int(exp[c]) * multiplier)
        multiplier *= 2
        c -= 1
    return number


ones_count = [0 for x in range(0,length)]
zeroes_count = [0 for x in range(0,length)]
gamma = ""
epilson = ""
for exp in input_list:
    c = 0
    for e in exp:
        if(e == '1'):
            ones_count[c] += 1  
        else:
            zeroes_count[c] += 1
        c += 1

for i in range(0, length):
    if ones_count[i] >= zeroes_count[i]:
        gamma = gamma + '1'
        epilson = epilson + '0'
    else:
        gamma = gamma + '0'
        epilson = epilson + '1'

gamma = to_decimal(gamma)
epilson = to_decimal(epilson)
print(gamma * epilson)

# gamma = to_decimal(gamma)
# epilson = to_decimal(epilson)
# print(gamma * epilson)