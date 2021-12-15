from functools import cmp_to_key
data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()

def append(mat, count):
    final = mat
    while(count > 1):
        new_mat = []
        for m in mat:
            if m == 9:
                new_mat.append(1)
            else:
                new_mat.append(m + 1)
        final.extend(new_mat)
        mat = new_mat
        count -= 1
    return final

def add_columns(matrix):
    for i in range(0, len(matrix)):
        mat = matrix[i]
        mat = append(mat, 5)
        matrix[i] = mat
    return matrix

def append_row(matrix, row, count):
    col = len(matrix[0])
    final = matrix
    while count > 1:
        new_mat = []
        for i in range(0, row):
            t = []
            for j in range(0, col):
                if(matrix[i][j] == 9):
                    t.append(1)
                else:
                    t.append(matrix[i][j] + 1)
            new_mat.append(t)
        final.extend(new_mat)
        matrix = new_mat
        count -= 1
    return final
        
def add_rows(matrix, row):
    matrix = append_row(matrix, row, 5)
    return matrix

def get_int(x):
    x = [int(_x) for _x in x]
    return x

def get_matrix():
    matrix = [get_int(x) for x in _list]
    return matrix

def isInsideGrid(x, y, row, col):
    return (x >= 0 and x < row and y >= 0 and y < col)

def compare(a,  b):
    if (a[2] == b[2]):
        if (a[0] != b[0]):
            return (a[0] - b[0])
        else:
            return (a[1] - b[1])
    return (a[2] - b[2])

def shortest(matrix, row, col):
    dist = [[1000000000 for i in range(0, row)] for j in range(0, col)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    st = []

    dist[0][0] = matrix[0][0]
    st.append((0, 0, dist[0][0]))
    while (len(st) != 0):
        k = st[0]
        del st[0]
        
    
        for i in range(0,4):
            x = k[0] + dx[i]
            y = k[1] + dy[i]
 
            if not (isInsideGrid(x, y, row, col)):
                continue
 
            if (dist[x][y] > dist[k[0]][k[1]] + matrix[x][y]):

                if (dist[x][y] != 1000000000):
                    temp = (x, y , dist[x][y])
                    if(temp in st):
                        st.remove(temp)

                dist[x][y] = dist[k[0]][k[1]] + matrix[x][y]
                st.append((x, y, dist[x][y]))
        sorted(st, key=cmp_to_key(compare))
    return dist[row - 1][col - 1]

matrix = get_matrix()
# row = len(matrix)
# matrix = add_columns(matrix)
# matrix = add_rows(matrix, row)
row = len(matrix)
col = len(matrix)
res = shortest(matrix, row, col)
print(res - matrix[0][0])

