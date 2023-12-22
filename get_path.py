#Nikola Milovanovic
def a_star_algo(lab, start, end):
    (i_s, j_s) = [[(i, j) for j, cell in enumerate(row) if cell == start] for i, row in enumerate(lab) if start in row][0][0]
    (i_e, j_e) = [[(i, j) for j, cell in enumerate(row) if cell == end] for i, row in enumerate(lab) if end in row][0][0]
    width = len(lab[0])
    height = len(lab)
    heuristic = lambda i, j: abs(i_e - i) + abs(j_e - j)
    comp = lambda state: state[2] + state[3]
    fringe = [((i_s, j_s), list(), 0, heuristic(i_s, j_s))]
    visited = {}
    while True:
        try:
            state = fringe.pop(0)
        except:
            pass
        (i, j) = state[0]
        if lab[i][j] == end:
            path = [state[0]] + state[1]
            path.reverse()
            return path
        visited[(i, j)] = state[2] 
        (i, j) = (int(i), int(j))
        neighbor = list()
        if i > 0 and lab[i-1][j] == '0' or lab[i-1][j] == end or lab[i-1][j] == 'a' or lab[i-1][j] == 'b' or lab[i-1][j] == 'h' or lab[i-1][j] == 'i' or lab[i-1][j] == 'c' or lab[i-1][j] == 'd' or lab[i-1][j] == 'g' or lab[i-1][j] == 'f': #top
            neighbor.append((i-1, j))
        if i < height and lab[i+1][j] == '0' or lab[i+1][j] == end or lab[i+1][j] == 'a' or lab[i+1][j] == 'b' or lab[i+1][j] == 'h' or lab[i+1][j] == 'i' or lab[i+1][j] == 'c' or lab[i+1][j] == 'd'  or lab[i+1][j] == 'g' or lab[i+1][j] == 'f':#down
            neighbor.append((i+1, j))
        if j > 0 and lab[i][j-1] == '0' or lab[i][j-1] == end or lab[i][j-1] == 'a' or lab[i][j-1] == 'b' or lab[i][j-1] == 'h' or lab[i][j-1] == 'i' or lab[i][j-1] == 'c' or lab[i][j-1] == 'd'  or lab[i][j-1] == 'g' or lab[i][j-1] == 'f':#left
            neighbor.append((i, j-1))
        if j < width and lab[i][j+1] == '0' or lab[i][j+1] == end or lab[i][j+1] == 'a' or lab[i][j+1] == 'b' or lab[i][j+1] == 'h' or lab[i][j+1] == 'i' or lab[i][j+1] == 'c' or lab[i][j+1] == 'd' or lab[i][j+1] == 'g' or lab[i][j+1] == 'f':#right
            neighbor.append((i, j+1))
        for n in neighbor:
            next_cost = state[2] + 1
            if n in visited and visited[n] >= next_cost:
                continue
            fringe.append((n, [state[0]] + state[1], next_cost, heuristic(n[0], n[1])))
        fringe.sort(key=comp)
def main_start(file):
    with open(file) as f:
        maze = [list(line.strip()) for line in f]
    for sub in maze:
        for elt in sub:
                if elt==' ':
                    sub.remove(elt)
    temp_start_stop=[]
    path=[]
    door_list = []
    temp_start_stop.append(('s', 'e'))
    for k in temp_start_stop:
        start=k[0]
        end=k[1]
        temp_path = a_star_algo(maze, start, end)
        if temp_start_stop.index(k)<len(temp_start_stop)-1:
            temp_path.pop()
        for elt in temp_path:
            path.append((elt[1],elt[0]))
    toshearch=[]
    for elt in path:
        x_elt=int(elt[0])
        y_elt=int(elt[1])
        if maze[y_elt][x_elt]=="b" or maze[y_elt][x_elt]=="i" or maze[y_elt][x_elt]=="c" or maze[y_elt][x_elt]=="c" or maze[y_elt][x_elt]=="g":
            door_list.append(elt)
    for k in range(0, len(door_list)):
        elt = door_list[k]
        if maze[elt[1]][elt[0]]=="i" or maze[elt[1]][elt[0]]=="b" or maze[elt[1]][elt[0]]=="c" or maze[elt[1]][elt[0]]=="g":
            toshearch.append(maze[elt[1]][elt[0]])
    if "i" in toshearch:
        toshearch.insert(toshearch.index("i"),"h")
    if "b" in toshearch:
        toshearch.insert(toshearch.index("b"),"a")
    if "c" in toshearch:
        toshearch.insert(toshearch.index("c"),"d")
    if "g" in toshearch:
        toshearch.insert(toshearch.index("g"),"f")
    toshearch.insert(0, 's')
    toshearch.append('e')
    start_stop=[]
    for e in range(0, len(toshearch)):
        try:
            start_stop.append((toshearch[e], toshearch[e+1]))
        except:
            pass
    path=[]
    for c in start_stop:
        start=c[0]
        end=c[1]
        temp_path = a_star_algo(maze, start, end)
        for elt in temp_path:
            path.append((elt[1],elt[0]))
    return(path)