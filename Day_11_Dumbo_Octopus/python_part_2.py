data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()

row = len(_list)
col = len(_list[0])



def list_int(exp):
    temp = [int(x) for x in exp]
    return temp

x_next = [-1, -1, -1 , 0, 0 , 1, 1, 1]
y_next = [-1, 0 , 1 , -1 , 1, -1, 0, 1]
queue = []
matrix = [list_int(x) for x in _list]


def allFlashed(matrix):
    for i in range(0, row):
        for j in range(0, col):
            if(matrix[i][j] != 0):
                return False

    return True


def exists(x, y):
    global row, col
    if(x < 0 or x >= row or y < 0 or y >= col):
        return False
    return True

def step1():
    global queue, matrix, row, col
    flag = False
    for i in range(0, row):
        for j in range(0, col):
            if(matrix[i][j] == 10):
                flag = True
                queue.append((i,j))
            else:
                matrix[i][j] += 1
                if(matrix[i][j] == 10):
                    flag = True
                    queue.append((i,j))
    return flag

def step2():
    global queue, matrix
    t = []
    for pair in queue:
        _x = pair[0]
        _y = pair[1]

        matrix[_x][_y] = 0

        for _ in range(0, 8):
            x = _x + x_next[_]
            y = _y + y_next[_]

            if(exists(x, y)):
                if(matrix[x][y] in [0,10]):
                    continue
                else:
                    matrix[x][y] += 1
                    if(matrix[x][y] == 10):
                        t.append((x,y))

    queue = t




flag = True
total = 0
step = 1
step1()

while True:
    if(allFlashed(matrix)):
        print(step , "\n\n")
        break

    step1()
    counter = 0
    while len(queue) != 0:
        counter += len(queue)
        step2()
    total += counter
    
    step += 1
