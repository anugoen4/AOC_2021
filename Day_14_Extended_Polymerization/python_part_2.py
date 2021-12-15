data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()

def get_string_and_map():
    inst_map = {}
    string = ""
    for exp in _list:
        if(exp == ''):
            continue
    
        if('->' in exp):
            elem1 = (exp.split('->')[0]).strip()
            elem2 = (exp.split('->')[1]).strip()

            if not (elem1 in inst_map):
                inst_map[elem1] = elem2
            continue
            
        string = exp
    return inst_map, string

def modify(string_map, inst_map, step_count):
    while(step_count):
        new_string = {}
        for elem in string_map:
            count = string_map[elem]
            

            e1 = elem[0] + inst_map[elem]
            e2 = inst_map[elem] + elem[1]

            if(e1 not in new_string):
                new_string[e1] = count
            else:
                new_string[e1] += count

            if(e2 not in new_string):
                new_string[e2] = count
            else:
                new_string[e2] += count

        string_map = new_string
        step_count -= 1
    return string_map
            
            
def get_string_map(string):
    string_map = {}
    for i in range(0, len(string) - 1):
        exp = string[i:i +2]
        if(exp not in string_map):
            string_map[exp] = 1
        else:
            string_map[exp] += 1
    return string_map

def get_diff(string_map):
    max_count = 0
    min_count = 21881896935290000000
    counter = {}
    flag = 0
    for s in string_map:
        e1 = s[0]
        e2 = s[1]
        value = string_map[s]
        if(flag == 0):
            counter[e1] = value
            counter[e2] = value
            flag = 1
        else:
            if(e2 not in counter):
                counter[e2] = value
            else:
                counter[e2] += value

    for c in counter:
        max_count = max(max_count, counter[c])
        min_count = min(min_count, counter[c])

    return max_count -  min_count

inst_map, string = get_string_and_map()
string_map = get_string_map(string)
string_map = modify(string_map, inst_map, 40)
res = get_diff(string_map)
print(res)

        