data = open('data.txt', 'r')
input_list = data.read().split('\n')
data.close()


length = len(input_list[0])
def to_decimal(exp):
    exp = exp[0]
    number = 0
    multiplier = 1

    c = len(exp) - 1
    while c > -1:
        number += (int(exp[c]) * multiplier)
        multiplier *= 2
        c -= 1
    return number

def solve(input_list, gas):
    universalCount = 1
    while len(input_list) > 1:
        start = input_list[0][:universalCount]
        ones_count = [0 for x in range(0,length)]
        zeroes_count = [0 for x in range(0,length)]
        for exp in input_list:
            c = 0
            
            for e in exp:
                if(e == '1'):
                    ones_count[c] += 1  
                else:
                    zeroes_count[c] += 1
                c += 1
        if (gas == 'O2'):
            if(ones_count[universalCount] >= zeroes_count[universalCount]):
                temp_list = [x for x in input_list if x.startswith(start + '1')]
            else:
                temp_list = [x for x in input_list if x.startswith(start + '0')]
            input_list = temp_list
        else:
            if(ones_count[universalCount] < zeroes_count[universalCount]):
                temp_list = [x for x in input_list if x.startswith(start + '1')]
            else:
                temp_list = [x for x in input_list if x.startswith(start + '0')]
            input_list = temp_list
        universalCount += 1
    return to_decimal(input_list)

ones_count = [0 for x in range(0,length)]
zeroes_count = [0 for x in range(0,length)]
for exp in input_list:
    
    c = 0
    for e in exp:
        if(e == '1'):
            ones_count[c] += 1  
        else:
            zeroes_count[c] += 1
        c += 1

O2_list = []
CO2_list = []
if(ones_count[0] >= zeroes_count[0]):
    O2_list = [x for x in input_list if x.startswith('1')]
    CO2_list = [x for x in input_list if x.startswith('0')]
else:
    CO2_list = [x for x in input_list if x.startswith('1')]
    O2_list = [x for x in input_list if x.startswith('0')]
    
co2 = solve(CO2_list, 'CO2')
o2 = solve(O2_list , 'O2')
print(co2 * o2)
