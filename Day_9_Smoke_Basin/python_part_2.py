data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()

matrix = [list(x) for x in _list]
col = len(_list[0])
row = len(matrix)

def exists(i, j, row, col):
    if(i < 0 or i >= row or j < 0 or j >= col):
        return False

    return True

counter_max = 0
x_next = [ 0, 0 , -1, 1]
y_next = [ -1 , 1, 0, 0]

def get_max(matrix, i, j, row, col):
    global c, visited

    if(i < 0 or i >= row or j < 0 or j >= col):
        return
    if(visited[i][j] == 1):
        return

    if(int(matrix[i][j]) == 9):
        return

    if(int(matrix[i][j]) != 9 and visited[i][j] == 0):
        visited[i][j] = 1
        c += 1
    else:
        visited[i][j] = 0
        c -= 1
    
    
    
    for _ in range(0, 4):
        x = i + x_next[_]
        y = j + y_next[_]
        if(exists(x, y, row, col) and visited[x][y] == 0 and int(matrix[x][y]) != 9):
            print(x,y)
            get_max(matrix, x, y, row, col)
     
    return 

track = {}
for i in range(0, row):
    for j in range(0, col):
        print("New ", i, j)
        visited = [[0 for _i in range(0, col)] for _j in range(0 , row)]
        c = 0
        get_max(matrix, i, j, row, col)
        print(c)

        if(c not in track):
            track[c] = 1
        else:
            track[c] += 1

temp = sorted(track, reverse= True)
s = []
counter = 0
for elem in temp:
    t = int(track[elem] / elem)
    counter += t
    for _ in range(0, t):
        s.append(elem)
    if(counter >= 3):
        break

print(s)
    


