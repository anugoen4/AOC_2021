data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()


count = 0

def find_illegal(exp):
    stack = []
    for e in exp:
        if e in ['(','{', '[', '<']:
            stack.append(e)
        elif e == ')':
            if(len(stack) == 0):
                return ')'
            if(stack[len(stack) - 1] != '('):
                return ')'
            stack = stack[:-1]
        elif e == '}':
            if(len(stack) == 0):
                return '}'
            if(stack[len(stack) - 1] != '{'):
                return '}'
            stack = stack[:-1]
        elif e == ']':
            if(len(stack) == 0):
                return ']'
            if(stack[len(stack) - 1] != '['):
                return ']'
            stack = stack[:-1]
        elif e == '>':
            if(len(stack) == 0):
                return '>'
            if(stack[len(stack) - 1] != '<'):
                return '>'
            stack = stack[:-1]
        
        

for exp in _list:
    char = find_illegal(exp)
    print(char)
    if(char == ')'):
        count += 3
    elif(char == '}'):
        count += 1197
    elif(char == ']'):
        count += 57
    elif(char == '>'):
        count += 25137

print(count)