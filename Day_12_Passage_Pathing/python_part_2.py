data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()
graph = {}
track = []
visited = {}
counter = 0

def exactlyone(visited):
    for elem in visited:
        if(visited[elem] == 2):
            return False
    return True

def create_graph_and_visited():
    for inst in _list:
        v1 = inst.split('-')[0]
        v2 = inst.split('-')[1]
        if(v1 not in graph):
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)

        if(v2 not in graph):
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)

        if not (v1.isupper()):
            if(v1 not in visited):
                visited[v1] = 0

        if not (v2.isupper()):
            if(v2 not in visited):
                visited[v2] = 0

def print_paths(idx, visited):
    global track, counter

    if idx in visited:
        if(visited[idx] == 0):
            visited[idx] = 1
            track.append(idx)
        elif(visited[idx] == 1 and idx not in ['start', 'end']):
            if(exactlyone(visited)):
                visited[idx] = 2
                track.append(idx)
            else:
                return
        else:
            return

    
    if idx.isupper():
        track.append(idx)


    if(idx == 'end'):
        counter += 1
        

    for vertex in graph[idx]:
        print_paths(vertex, visited)
    
    if(idx in visited):
        if idx not in ['start']:
            if(visited[idx] == 1):
                visited[idx] = 0

            if(visited[idx] == 2):
                visited[idx] = 1
    track = track[:-1]
    return

    


create_graph_and_visited()
print(graph)
print_paths('start', visited)
print(counter)

            
