from pprint import pprint
data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()

# Add Puzzle input given in data.txt
# run this file and find output in res.txt
# Copy res.txt content into data.txt
# run java file

def get_int(x):
    x = [int(_x) for _x in x]
    return x

def get_matrix():
    matrix = [get_int(x) for x in _list]
    return matrix

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

matrix = get_matrix()
row = len(matrix)
matrix =  add_columns(matrix)
matrix = add_rows(matrix, row)
pprint(matrix)

file = open('res.txt', 'w')
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        file.write(str(matrix[i][j]))
    file.write('\n')