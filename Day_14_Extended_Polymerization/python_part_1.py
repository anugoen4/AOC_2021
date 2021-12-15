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

def modify(string, inst_map, step_count):
    while(step_count):
        new_string = ""
        for i in range(0, len(string) - 1):
            exp = string[i:i+2]
            if( i== 0):
                new_string += (exp[0] + inst_map[exp] + exp[1])
            else:
                new_string += (inst_map[exp] + exp[1])
        step_count -= 1
        # print(len(new_string))
        string = new_string
        new_string = ""
    return string

def get_diff(string):
    counter = {}
    max_count = 0
    min_count = 21881896935290

    for e in string:
        if e in counter:
            counter[e] += 1
        else:
            counter[e] = 1

    for c in counter:
        max_count = max(max_count, counter[c])
        min_count = min(min_count, counter[c])
    return max_count - min_count

inst_map, string = get_string_and_map()
string = modify(string, inst_map, 10)
res = get_diff(string)
print(res)

        