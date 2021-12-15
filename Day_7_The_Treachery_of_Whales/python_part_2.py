data = open('data.txt', 'r')
input_list = data.read().split(',')
data.close()

input_list = [int(x) for x in input_list]

min_elem = min(input_list)
max_elem = max(input_list)


def compute(sum):
    return int((sum * (sum + 1)) / 2)

res = 100000000000
while(min_elem <= max_elem):
    temp = 0

    for elem in input_list:
        temp += compute((abs(elem - min_elem)))
    
    res = min(res, temp)
    min_elem += 1

print(res)
