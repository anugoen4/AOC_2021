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

def valid(matrix, i, j, row, col):
    if(exists(i-1, j, row, col)):
        if(matrix[i-1][j] <= matrix[i][j]):
            return False
    if(exists(i, j-1, row, col)):
        if(matrix[i][j-1] <= matrix[i][j]):
            return False
    if(exists(i, j+1, row, col)):
        if(matrix[i][j + 1] <= matrix[i][j]):
            return False
    if(exists(i+1, j, row, col)):
        if(matrix[i+ 1][j] <= matrix[i][j]):
            return False
    
    return True

total = 0
for i in range(0, row):
    for j in range(0, col):
        if(valid(matrix, i, j, row, col)):
            print(matrix[i][j])
            total += (int(matrix[i][j]) + 1)
print(total)


