data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()


def get_score(exp):
    score = 0
    for s in exp:
        score = score * 5
        if s == ')':
            score += 1
        elif s == ']':
            score += 2
        elif s == '}':
            score += 3
        elif s == '>':
            score += 4
    return score
    
def correct_me(exp):
    stack = []

    for e in exp:
        if( e in ['(', '{', '[', '<']):
            stack.append(e)
        elif e == ')':
            if(stack[len(stack) - 1] == '('):
                stack = stack[:-1]
        elif e == '}':
            if(stack[len(stack) - 1] == '{'):
                stack = stack[:-1]
        elif e == ']':
            if(stack[len(stack) - 1] == '['):
                stack = stack[:-1]
        elif e == '>':
            if(stack[len(stack) - 1] == '<'):
                stack = stack[:-1]
    temp = ''
    for s in stack:
        if s == '(':
            temp += ')'
        elif s == '{':
            temp += '}'
        elif s == '[':
            temp += ']'
        elif s == '<':
            temp += '>'
    temp = temp[::-1]
    return get_score(temp)
            

def find_illegal(exp):
    stack = []
    for e in exp:
        if e in ['(','{', '[', '<']:
            stack.append(e)
        elif e == ')':
            if(len(stack) == 0):
                return True
            if(stack[len(stack) - 1] != '('):
                return True
            stack = stack[:-1]
        elif e == '}':
            if(len(stack) == 0):
                return True
            if(stack[len(stack) - 1] != '{'):
                return True
            stack = stack[:-1]
        elif e == ']':
            if(len(stack) == 0):
                return True
            if(stack[len(stack) - 1] != '['):
                return True
            stack = stack[:-1]
        elif e == '>':
            if(len(stack) == 0):
                return True
            if(stack[len(stack) - 1] != '<'):
                return True
            stack = stack[:-1]
    return False

track = []      
for exp in _list:
    if(find_illegal(exp) == False):
        track.append(correct_me(exp))
track = sorted(track)
print(track[int(len(track)/2)])