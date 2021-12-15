data = open('data.txt', 'r')
input_list = data.read().split('\n')
data.close()

max_elem = 0
matrix = []

def count_intersection(matrix):
    counter = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if(matrix[i][j] >= 2):
                counter += 1

    return counter

for inst in input_list:
    x1,y1 = (inst.split('->')[0]).split(',')
    x2,y2 = (inst.split('->')[1]).split(',')
    max_elem = max(max_elem, int(x1),int(y1), int(x2), int(y2))
matrix = [[0 for i in range(0, max_elem + 1)] for i in range(0, max_elem + 1)]

for inst in input_list:
    x1,y1 = (inst.split('->')[0]).split(',')
    x2,y2 = (inst.split('->')[1]).split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if(x1 == x2):
    
        t1 = min(y1,y2)
        t2 = max(y1,y2)
        while(t1 <= t2):
            matrix[x1][t1] += 1
            t1 += 1
    elif(y1 == y2):
        
        t1 = min(x1,x2)
        t2 = max(x1,x2)
        while(t1 <= t2):
            matrix[t1][y1] += 1
            t1 += 1
counter = count_intersection(matrix)
print(counter)

