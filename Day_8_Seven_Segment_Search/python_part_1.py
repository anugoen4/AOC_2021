data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()
input_list = [x.split('|')[1][1:] for x in _list]

counter = 0
for elem in input_list:
    elem = elem.split(' ')
    print(elem)
    for e in elem:
        if(len(e) in [2,4,3,7]):
            counter += 1
print(counter)