data = open('data.txt', 'r')
input_list = data.read().split('\n')
data.close()

inc = 0

for i in range(3, len(input_list)):
    if(int(input_list[i]) > int(input_list[i-3])):
        inc += 1

print(inc)
