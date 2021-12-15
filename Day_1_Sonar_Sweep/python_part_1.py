data = open('data.txt', 'r')
input_list = data.read().split('\n')
data.close()

inc = 0

for i in range(0, len(input_list)):
    if(int(input_list[i]) > int(input_list[i-1])):
        inc += 1

print(inc)
