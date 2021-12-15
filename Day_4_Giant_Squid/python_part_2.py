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


def solve(check, input_list, matrix):
    final_elem = 0
    final_m = 0
    for elem in input_list:
        elem = int(elem)

        for m in range(0,len(matrix)):
            for i in range(0,5):
                for j in range(0,5):
                    if(int(matrix[m][i][j]) == elem):
                        matrix[m][i][j] = '-' + matrix[m][i][j]
            # print(m)
            if(win(matrix[m])):
                if(m in check):
                    check.remove(m)
                    if(len(check) == 0):
                        final_m = m
                        final_elem = elem
                        return final_elem * get_sum(matrix[final_m])

    

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
check = set([x for x in range(0, len(matrix))])
ans = solve(check,input_list, matrix)
print(ans)