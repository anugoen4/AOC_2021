from pprint import pprint
data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()

folds = []
def get_folds_max_x_max_y(max_x, max_y):
    for inst in _list:
        if(inst == ''):
            continue

        if(inst.startswith('fold')):
            if('x' in inst):
                folds.append(('x',inst.split('=')[1]))
                continue

            if('y' in inst):
                folds.append(('y',inst.split('=')[1]))
                continue
            
        max_x = max(int(inst.split(',')[0]), max_x)
        max_y = max(int(inst.split(',')[1]), max_y)

    return (max_x, max_y)

def populate(matrix):
    for inst in _list:
        if(inst == ''):
            break

        x = int(inst.split(',')[0])
        y = int(inst.split(',')[1])
        matrix[y][x] = '#'
    return matrix

def y_fold(matrix, upper, lower, max_x, max_y):
    while(upper >= 0 and lower < max_y):
        for i in range(0, max_x ):
            if(matrix[lower][i] == '#'):
                matrix[upper][i] = '#'
        upper -= 1
        lower += 1 

    return matrix

def x_fold(matrix, left, right, max_x, max_y):
    _left = left
    _right = right
    for i in range(0, max_y):
        left = _left
        right = _right
        while(left >= 0 and right < max_x):
            if(matrix[i][right] == '#'):
                matrix[i][left] = '#'
            left -= 1
            right += 1

        matrix[i] = matrix[i][0:_left + 1]

    return matrix

def count_dots_y(matrix,x, y):
    counter = 0
    for i in range(0, y):
        for j in range(0, x ):
            if(matrix[i][j] == '#'):
                counter += 1
    return counter


def count_dots_x(matrix,x, y):
    counter = 0
    for i in range(0, y):
        for j in range(0, x):
            if(matrix[i][j] == '#'):
                counter += 1
    return counter


(max_x, max_y) = get_folds_max_x_max_y(0, 0)
matrix = [['.' for i in range(0, max_x + 1)] for j in range(0, max_y + 1)]
matrix = populate(matrix)

max_x += 1
max_y += 1

for f in folds:
    if(f[0] == 'y'):
        upper = int(f[1]) - 1
        lower = int(f[1]) + 1
        matrix = y_fold(matrix, upper, lower, max_x, max_y)  # max_x hori, max_y vertical
        matrix = matrix[:upper + 1]
        max_x = len(matrix[0])
        max_y = len(matrix)
        counter = count_dots_y(matrix, max_x, max_y)
        print(counter)
    else:
        left = int(f[1]) - 1
        right = int(f[1]) + 1
        matrix = x_fold(matrix, left, right, max_x, max_y)  # max_x hori, max_y vertical
        max_x = len(matrix[0])
        max_y = len(matrix)
        counter = count_dots_x(matrix, max_x, max_y)
        print(counter)
    break