data = open('data.txt', 'r')
da = data.read().split('\n')
data.close()
matrix = []

def get_sum(m):
    ans = 0
    for i in range(0,5):
        for j in range(0,5):
            if not (m[i][j].startswith('-')):
                ans += int(m[i][j])
    return ans

def win(m):
    for i in range(0,5):
        count = 0
        for j in range(0,5):
            if(m[i][j].startswith('-')):
                count += 1
        
        if(count == 5):

            return True
    
    for i in range(0,5):
        count = 0
        for j in range(0,5):
            if (m[j][i].startswith('-')):
                count += 1
        
        if(count == 5):

            return True

    return False


def solve(input_list, matrix):
    for elem in input_list:
        elem = int(elem)

        for m in matrix:
            for i in range(0,5):
                for j in range(0,5):
                    if(int(m[i][j]) == elem):
                        m[i][j] = '-' + m[i][j]
            if(win(m)):
                return get_sum(m) * elem
    return 1

input_list = da[0].split(',')
da = da[2:]
temp = []
for d in da:
    if(d == ''):
        matrix.append(temp)
        temp = []
    else:
        d = d.split(' ')
        t = [_ for _ in d if _ != '']
        temp.append(t)

matrix.append(temp)
ans = solve(input_list, matrix)
print(ans)