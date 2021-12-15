data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()
input_list = [x.split('|')[0][:-1] for x in _list]
res_list = [x.split('|')[1][1:] for x in _list]

def f_one_four_seven_eight(input_list):
    global one, four, seven, eight
    for elem in input_list:
        if(len(elem) == 2):
            one = elem
        elif(len(elem) == 4):
            four = elem
        elif(len(elem) == 3):
            seven = elem
        elif (len(elem) == 7):
            eight = elem

def f_nine(input_list):
    global four, seven, eight, nine
    find_nine = []
    for e in four:
        if e not in find_nine:
            find_nine.append(e)

    for e in seven:
        if e not in find_nine:
            find_nine.append(e)
    find_nine = ''.join(find_nine)
    potential = ''

    for e in eight:
        if e not in find_nine:
            potential += e

    for elem in input_list:
        if(sorted(potential[0] + find_nine) == sorted(elem)):
            nine = elem
            break

    for elem in input_list:
        if(sorted(potential[1] + find_nine) == sorted(elem)):
            nine = elem
            break

def f_six(input_list):
    global one, six, eight
    for e in one:
        temp = eight.replace(e, '')

        for elem in input_list:
            if(sorted(temp) == sorted(elem)):
                six = elem
                return

def f_zero(input_list):
    global six, nine, zero
    for elem in input_list:
        if(len(elem) == 6 and elem not in [six, nine]):
            zero = elem
            return

def f_three(input_list):
    global nine, three, one
    for e in nine:
        t = nine.replace(e, '')
        for elem in input_list:
            if(sorted(t) == sorted(elem) and one[0] in elem and one[1] in elem):
                three = elem
                return

def f_five(input_list):
    global six, five
    for e in six:
        t = six.replace(e, '')
        for elem in input_list:
            if(sorted(t) == sorted(elem)):
                five = elem
                return

def f_two(input_list):
    global zero, one, two, three, four, five, six, seven, eight, nine
    for elem in input_list:
        if elem not in [zero, one, three, four, five, six, seven, eight, nine]:
            two = elem
            return

def evaluate(exp):
    exp = exp.split(' ')
    counter = ''
    for elem in exp:
        if(sorted(elem) == sorted(zero)):
            counter = counter + '0'
        elif(sorted(elem) == sorted(one)):
            counter = counter + '1'
        elif(sorted(elem) == sorted(two)):
            counter = counter + '2'
        elif(sorted(elem) == sorted(three)):
            counter = counter + '3'
        elif(sorted(elem) == sorted(four)):
            counter = counter + '4'
        elif(sorted(elem) == sorted(five)):
            counter = counter + '5'
        elif(sorted(elem) == sorted(six)):
            counter = counter + '6'
        elif(sorted(elem) == sorted(seven)):
            counter = counter + '7'
        elif(sorted(elem) == sorted(eight)):
            counter = counter + '8'
        elif(sorted(elem) == sorted(nine)):
            counter = counter + '9'
    return int(counter)
        
sum = 0         
for i in range(0,len(input_list)):
    exp = input_list[i]
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    exp = exp.split(' ')
    f_one_four_seven_eight(exp)
    f_nine(exp)
    f_six(exp)
    f_zero(exp)
    f_three(exp)
    f_five(exp)
    f_two(exp)

    print(evaluate(res_list[i]))
    sum += evaluate(res_list[i])

print(sum)



