code = """
import networkx as nx
import matplotlib.pyplot as plt

def pretty_print(graph, title = "Graph Visualization",weighted = False, directed = False, heuristic = None):
    g = nx.DiGraph() if directed else nx.Graph()
    for u in graph:
        label = u
        if heuristic:
            label += "("+str(heuristic[u])+")"
        g.add_node(u, label = label)
        for v in graph[u]:
            g.add_edge(u, v, weight = graph[u][v])
    pos = nx.circular_layout(g)
    nx.draw(g, pos, 
            node_size = 1200, node_color = 'lightgreen',
            width = 1.5, edge_color = 'red',
            edgecolors = 'black', linewidths = 1.5,
            margins = 0.25, clip_on = False)
    nx.draw_networkx_labels(g, pos, labels = nx.get_node_attributes(g, 'label'),
                            font_size = 12, font_family = 'cursive')
    if weighted:
        nx.draw_networkx_edge_labels(g, pos, 
                                     edge_labels = nx.get_edge_attributes(g, 'weight'),
                                     font_size = 8, font_family = 'cursive')
    plt.suptitle(title)
    plt.axis('off')
    plt.show()
    plt.clf()

#______________________________________________

def display(graph):
    g = nx.DiGraph()
    for u in graph:
        g.add_node(u)
        for v in graph[u]:
            g.add_edge(u, v, weight = graph[u][v])
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels = True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels = nx.get_edge_attributes(g, 'weight'))
    plt.show()
    plt.clf()

#______________________________________________

def get_input(heuristic = False, weighted = False, bound = False, directed = False):
    rtn = []
    graph = {}
    rtn.append(graph)
    if heuristic:
        h = {}
        for _ in range(int(input("Enter no of nodes: "))):
            x, hval = input("Enter node and heuristic value: ").split()
            h[x] = int(hval)
        rtn.append(h)
    for _ in range(int(input("Enter no of edges: "))):
        if weighted:
            u, v, w = input("Enter (node, adj, weight): ").split()
        else:
            u, v = input("Enter (node, adj): ").split()
            w = 0
        graph[u] = graph.get(u,{})
        graph[u][v] = int(w)
        graph[v] = graph.get(v,{})
        if not directed:
            graph[v][u] = int(w)
    source, goal = input("Enter source and goal: ").split()
    if bound:
        b = int(input("Enter memory bound: "))
        rtn.append(b)
    rtn.extend([source, goal])
    return rtn

#______________________________________________

def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []


def BFS(graph, start, goal):
    queue = [start]
    visited = []
    parent = {start : None}
    while queue:
        node = queue.pop(0)#First element
        visited.append(node)
        if node == goal:
            print("Result(BFS):",print_path(node, parent))
            return True
        for adj in graph[node]:
            if adj not in visited and adj not in queue:
                queue.append(adj)
                parent[adj] = node
    return False

#______________________________________________

def DFS(graph, start, goal):
    stack = [start]
    visited = []
    parent = {start : None}
    while stack:
        node = stack.pop()#last element
        visited.append(node)
        if node == goal:
            print("Result(DFS):",print_path(node, parent))
            return True
        for adj in graph[node]:
            if adj not in visited and adj not in stack:
                stack.append(adj)
                parent[adj] = node
    return False

#______________________________________________

def UCS(graph, start, goal):
    queue = [start]
    visited = []
    parent = {start : None}
    cost = {start : 0}
    while queue:
        queue.sort(key = lambda x : cost[x])
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print("Result(UCS):",print_path(node, parent),"Path cost =",cost[node])
            return True
        for adj in graph[node]:
            if adj not in visited:
                new_cost = cost[node] + graph[node][adj]
                if adj not in queue:
                    queue.append(adj)
                elif new_cost > cost[adj]:
                    continue
                cost[adj] = new_cost
                parent[adj] = node
    return False

#______________________________________________

def DLS(graph, start, goal, limit):
    result = recursive_dls(graph, start, goal, limit, [start])
    print("Result(DLS):",result)


def recursive_dls(graph, node, goal, limit, visited):
    if node == goal:
        return [node]
    elif limit == 0:
        return 'cutoff'
    else:
        status = 'failure'
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                result = recursive_dls(graph, adj, goal, limit - 1, visited)
                if result == 'cutoff':
                    status = 'cutoff'
                    visited.remove(adj)
                elif result != 'failure':
                    return [node] + result
        return status
        
#______________________________________________

def IDS(graph, start, goal):
    depth = 0
    while True:
        result = recursive_dls(graph, start, goal, depth, [start])
        print("Result(IDS/IDDFS):",result,"at depth limit =",depth)
        if result != 'cutoff':
            return
        depth += 1

#______________________________________________

def AStar(graph, start, goal, h):
    queue = [start]
    visited = []
    parent = {start : None}
    g = {start : 0}
    f = {start : h[start]}
    while queue:
        queue.sort(key = lambda x : f[x])
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print("Result(A*):",print_path(node, parent),"Path cost =",g[node])
            return True
        for adj in graph[node]:
            if adj not in visited:
                gcost = g[node] + graph[node][adj]
                fcost = gcost + h[adj]
                if adj not in queue:
                    queue.append(adj)
                elif fcost > f[adj]:
                    continue
                g[adj] = gcost
                f[adj] = fcost
                parent[adj] = node
    return False

#______________________________________________

def IDAStar(graph, start, goal, h):
    def dfs(graph, parent, node, goal, g, h, th):
        f = g + h[node]
        if f > th:
            return None, f
        if node == goal:
            return node, f
        min_th = inf
        for adj in graph[node]:
            result, temp_th = dfs(graph, parent, adj, goal, g + graph[node][adj], h, th)
            if result is not None:
                parent[adj] = node
                return result, temp_th
            elif temp_th < min_th:
                min_th = temp_th
        return None, min_th
    
    inf = 9999999
    parent = {start : None}    
    th = h[start]
    while True:
        result, new_th = dfs(graph, parent, start, goal, 0, h, th)
        if result is not None:
            result = print_path(result, parent)
            cost = sum([graph[n1][n2] for n1, n2 in zip(result,result[1:])])
            print("Result(IDA*):",result,"Path cost =",cost)
            return
        elif new_th == inf:
            print("Result(IDA*): failure")
            return
        th = new_th

#______________________________________________

def SMAStar(graph, start, goal, h, bound):
    queue = [start]
    visited = []
    parent = {start : None}
    g = {start : 0}
    f = {start : h[start]}
    backup = {}
    while queue:
        queue.sort(key = lambda x : f[x])
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print("Result(SMA*):",print_path(node, parent),"Path cost =",g[node])
            return True
        successors = []
        for adj in graph[node]:
            if adj in visited:
                continue
            gcost = g[node] + graph[node][adj]
            fcost = gcost + h[adj]
            if adj in queue:
                if fcost >= f[adj]:
                    continue
            elif len(queue) < bound:
                    queue.append(adj)
            else:
                worst = max(queue, key = lambda x : f[x])
                if fcost < f[worst]:
                    backup[worst] = f[worst]
                    queue.remove(worst)
                    queue.append(adj)
                else:
                    continue
            g[adj] = gcost
            f[adj] = fcost
            parent[adj] = node
            successors.append(adj)
        if not successors and node in backup:
            f[node] = backup[node]
        elif not successors:
            f[node] = float('inf')
    return False

#______________________________________________

from random import randint as rint
def genetic(gen, pop):
    def show(b):
        board = [ ['_'] * n for _ in range(n)]
        for i in range(n):
            board[int(b[i])-1][i] = 'Q'
        print(f" {' '.join(['_']*n)}")
        for i in board:
            print(f"|{'|'.join(i)}|")
    def mutate(b1, b2):
        b1, b2 = list(b1), list(b2)
        x, y = rint(0,n-1), rint(0,n-1)
        b1[x], b2[x] = b2[x], b1[x]
        b1[y] = str(int(y) + 1)
        return (''.join(b1),''.join(b2))
    def crossover(b1, b2):
        b1, b2 = list(b1), list(b2)
        x = rint(1,n-1)
        b1[0:x], b2[0:x] = b2[0:x], b1[0:x]
        return (''.join(b1), ''.join(b2))
    def fitness(b):
        b = list(b)
        attacks = 0
        for i in range(n):
            for j in range(i+1, n):
                if b[i] == b[j] or abs(int(b[i]) - int(b[j])) == j - i:
                    attacks += 1
        return attacks
    n = len(pop[0])
    i = 0
    pq = []
    pq.append((fitness(pop[0]),pop[0]))
    pq.append((fitness(pop[1]),pop[1]))
    for i in range(gen+1):
        f1, b1 = pq.pop(0)
        f2, b2 = pq.pop(0)
        pq.clear()
        if f1 == 0:
            print("Goal State:",b1,"Generation:",i+1)
            show(b1)
            return
        elif f2 == 0:
            print("Goal State:",b2,"Generation:",i+1)
            show(b2)
            return
        x1, x2 = crossover(b1, b2)
        x3, x4 = crossover(b2, b1)
        new_pop = [(x1, x2), (x3, x4), mutate(x1, x2), mutate(x2, x1)]
        for child in new_pop:
            pq.append((fitness(child[0]), child[0]))
            pq.append((fitness(child[1]), child[1]))
        pq.append((f1, b1))
        pq.append((f2, b2))
        pq.sort(key = lambda x : x[0])
    print("Most Evolved State:",pq[0][1],"Generation:",i,"Attacks:",pq[0][0])
    show(pq[0][1])

#______________________________________________

import math
import random
def simulated_annealing(initsol, inittemp, alpha, iters):
    def fcost(sol):
        return sum([i**2 for i in sol])
    def successors(sol, step = 1.0):
        succ = [x + random.uniform(-step,step) for x in sol]
        return succ
    currsol = initsol
    cost = fcost(currsol)
    sol = currsol
    mincost = cost
    temp = inittemp
    for iteration in range(iters):
        neighbor = successors(currsol)
        ncost = fcost(neighbor)
        costdiff = ncost - cost
        if costdiff < 0 or random.random() < math.exp(-costdiff/temp):
            currsol = neighbor
            cost = ncost
            if cost < mincost:
                sol = currsol
                mincost = cost
        temp *= alpha
    return sol, mincost

#______________________________________________

import math 
import random
def sudoku_simulated_annealing(board, initial_temp = 1.0, cooling_rate = 0.99, min_temp = 0.001):
    def display(board):
        for row in board:
            print(' '.join(str(num) if num != 0 else '.' for num in row))
        print()
    def fill(board):
        for i in range(9):
            choices = list(set(range(1,10)) - set(board[i]) - {0})
            random.shuffle(choices)
            for j in range(9):
                if board[i][j] == 0:
                    board[i][j] = choices.pop()
    def cost(board):
        conflicts = 0
        for n in range(9):
            row = board[n]
            col = [x[n] for x in board]
            conflicts += len(row) - len(set(row))
            conflicts += len(col) - len(set(col))
        for l in [0,3,6]:
            for k in [0,3,6]:
                block = []
                for i in range(0+l,3+l):
                    for j in range(0+k,3+k):
                        block.append(board[i][j])
                conflicts += 9 - len(set(block))
        return conflicts
    def next(board, fixed):
        neighbor = [[x for x in row] for row in board]
        i = random.randint(0,8)
        cols = [j for j in range(9) if (i,j) not in fixed]
        if len(cols) >= 2:
            j1, j2 = random.sample(cols, 2)
            neighbor[i][j1], neighbor[i][j2] = neighbor[i][j2], neighbor[i][j1]
        return neighbor
    fixed = [(x,y) for x in range(9) for y in range(9) if board[x][y] != 0]
    fill(board)
    current = best = board
    temp = initial_temp
    while temp > min_temp:
        neighbor = next(current,fixed)
        delta = cost(neighbor) - cost(current)
        if delta < 0:
            current = neighbor
            if cost(neighbor) < cost(best):
                best = neighbor
        else:
            if random.random() < math.exp(-delta/temp):
                current = neighbor
        temp *= cooling_rate
    print(f"Sudoku ({'Best Possible State | Attacks = '+str(cost(best)) if cost(best) else 'Solved'})") 
    display(best)

#______________________________________________

import networkx as nx
import matplotlib.pyplot as plt
def show_tree(graph):
    graph = {node : [adj for adj in graph[node]] for node in graph}
    terminal_nodes = set()
    for node in graph:
        for i in range(len(graph[node])):
            x = str(graph[node][i])
            if x.isdigit():
                while x in terminal_nodes:
                    x+=" "
                graph[node][i] = x
                terminal_nodes.add(x)
    g = nx.DiGraph(graph)
    levels = nx.single_source_shortest_path_length(g, next(iter(g.nodes)))
    layers = {}
    for node, level in levels.items():
        layers[level] = layers.get(level, []) + [node]
    pos = {}
    for level, nodes in layers.items():
        x_offset = (len(nodes) - 1)/2
        for i, node in enumerate(nodes):
            x = i - x_offset
            y = -level
            pos[node] = (x,y)
    plt.figure(figsize = (8,4))
    nx.draw(g, pos, with_labels = True, 
            node_size = 600, node_color = 'lightgreen',
            font_size = 12, font_family = 'cursive',
            arrows = False, width = 1.5, edge_color = 'red',
            edgecolors = 'black', linewidths = 1.5,
            margins = 0.1, clip_on = False)
    plt.suptitle("Alpha Beta Pruning")
    plt.show()
    plt.clf()
MIN = -float('inf')
MAX = float('inf')
def alphabeta(node, graph, ismax, pruned = [], alpha = MIN, beta = MAX, path = {}):
    if str(node).isdigit():
        return int(node), pruned, path
    option = MIN if ismax else MAX
    for child in graph[node]:
        val, _, _ = alphabeta(child, graph, not ismax, pruned, alpha, beta, path)
        if ismax:
            option = max(option, val)
            alpha = max(option, alpha)
            path[node] = alpha
        else:
            option = min(option, val)
            beta = min(option, beta)
            path[node] = beta
        if alpha >= beta:
            i = graph[node].index(child)+1
            pruned += [f"{node}-{adj}" for adj in graph[node][i:]]
            break
    return option, pruned, path
def show_path(node, graph, path, value):
    for adj in graph[node]:
        if str(adj).isdigit():
            return [node,str(value)]
        if path[adj] == value:
            return [node] + show_path(adj, graph, path, value)

#______________________________________________

import networkx as nx
import matplotlib.pyplot as plt

def backtrack_map(graph, colors):
    def rec_backtrack(assign, graph, colors):
        if -1 not in assign.values():
            return assign
        node = [x for x in assign if assign[x] == -1][0]
        for color in colors:
            if all(assign[adj] != color for adj in graph[node]):
                assign[node] = color
                result = rec_backtrack(assign, graph, colors)
                if result:
                    return result
                assign[node] = -1
        return None

    assign = {node : -1 for node in graph}
    return rec_backtrack(assign, graph, colors)
def display_map(graph, colors = None):
    g = nx.DiGraph(graph)
    #nx.draw_circular(g, with_labels = True, node_color = colors)
    nx.draw_circular(g, with_labels = True,
                    node_size = 600, node_color = colors,
                    font_size = 12, font_family = 'cursive',
                    arrows = False, width = 1.25,
                    edgecolors = 'black', linewidths = 1.5,
                    margins = 0.375, clip_on = False)
    plt.suptitle("Map Coloring(Constraint Satisfaction Problem)")
    plt.show()
    plt.clf()

#______________________________________________

import networkx as nx
import matplotlib.pyplot as plt

def backtrack_house(houses, locs):
    def check(assign, loc):
        #constraints given in the question
        #change it accordinly
    
        a = assign['A']
        b = assign['B']
        c = assign['C']
        d = assign['D']
        
        #1. C lives in a house higher than D
        if c != -1 and d != -1 and c < d:return False
    
        #2. D lives next to A in Lower number House
        if d != -1 and a != -1 and (a - d) != 1:return False
    
        #3. There is at least one house between D and B    
        if d != -1 and b != -1 and abs(d - b) == 1:return False
    
        #4. C doesn't live in house number 3
        if c != -1 and c == 3:return False
    
        #5. B doesn't live in house number 1
        if b != -1 and b == 1:return False
            
        if loc in assign.values():
            return False
        return True
    def rec_backtrack(assign, locs):
        if check(assign, -1):
            return assign
        choices = [x for x in assign if assign[x] == -1]
        house = choices[0] if choices else None
        for loc in locs:
            if check(assign, loc):
                assign[house] = loc
                res = rec_backtrack(assign, locs)
                if res:
                    return res
                assign[house] = -1
        return None

    assign = {house : -1 for house in houses}    
    return rec_backtrack(assign, locs)
def display_house(result):
    g = nx.Graph()
    nodes = list(result.keys())
    nodes.sort(key = lambda x : result[x])
    nodes = [f"{node}({result[node]})" for node in nodes]
    for u, v in zip(nodes, nodes[1:]):
        g.add_edge(u, v)
    pos = {node : (0, i) for i, node in enumerate(nodes)}
    nx.draw(g, pos, with_labels = True,
            width = 1.5, edge_color = 'red',
            node_size = 800, node_color = 'lightgreen',
            font_size = 12, font_family = 'cursive',
            edgecolors = 'black', linewidths = 1.5,
            margins = 0.2, clip_on = False)
    plt.suptitle("House Allocation(Constraint Satisfaction Problem)")
    plt.show()
    plt.clf()

#______________________________________________

def main():
    graph = {"A" : {"B":9,"C":4,"D":7},
             "B" : {"A":9,"E":11},
             "C" : {"A":4,"E":17,"F":12},
             "D" : {"A":7,"F":14},
             "E" : {"B":11,"G":5,"C":17},
             "F" : {"D":14,"C":12,"G":9},
             "G" : {"E":5,"F":9}}
    heuristic = {"A":21,"B":14,"C":18,"D":18,"E":5,"F":8,"G":0}
    pretty_print(graph, title = "Graph", weighted = True, directed = True, heuristic = heuristic)
    display(graph)
    
    BFS(graph, "A", "F")
    
    DFS(graph, "A", "F")
    
    UCS(graph, "A", "G")
    
    DLS(graph, "A", "G", 3)
    
    IDS(graph, "A", "G")
    
    AStar(graph, "A", "G", heuristic)
    
    IDAStar(graph, "A", "G", heuristic)
    
    #graph, heuristic, bound, source, goal = get_input(heuristic = True,weighted = True,bound = True)
    SMAStar(graph, "A", "G", heuristic, bound = 3)
    
    print("Genetic Algorithm Example 1(5 Queen): ")
    genetic(1000, ["32152","24345"])
    print()
    print("Genetic Algorithm Example 2(8 Queen): ")
    genetic(1000, ["57142860","56782463"])
    print()
    
    initsol = [300.0, 400.0]
    inittemp = 1000.0
    alpha = 0.95
    iters = 500
    bestsol, cost = simulated_annealing(initsol, inittemp, alpha, iters)
    print("Simulated Annealing Best Solution:",bestsol)
    print("Simulated Annealing Best Cost:",cost)
    print()
    
    board =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    sudoku_simulated_annealing(board)
    
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'G'],
        'D' : ['H', 'I'],
        'E' : [10, 5],
        'F' : ['J', 'K'],
        'G' : ['L', 'M'],
        'H' : [11, 12],
        'I' : [8, 9],
        'J' : [8, 5],
        'K' : [12, 11],
        'L' : [12, 9],
        'M' : [8, 7],}
    show_tree(graph)
    print(graph)
    start = 'A'
    
    val, pruned, path = alphabeta(start, graph, True)#True means first node is max
    path = show_path(start, graph, path, val)
    print("Alpha Beta Pruning(Maximize):", val, " Pruned Branches:", ', '.join(pruned), " Path:",'->'.join(path))
    
    val, pruned, path = alphabeta(start, graph, False)#False means first node is min
    path = show_path(start, graph, path, val)
    print("Alpha Beta Pruning(Minimize):", val, " Pruned Branches:", ', '.join(pruned), " Path:",'->'.join(path))
    print()

    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'C', 'D', 'E'],
        'C' : ['B', 'E'],
        'D' : ['A', 'B', 'E'],
        'E' : ['B', 'C', 'D']}
    
    colors = ["red","green","blue"]
    sol = backtrack_map(graph, colors)
    print("Constraint Satisfaction Problem(Map Coloring)")
    if sol:
        display_map(graph, sol.values())
        for (node, color) in sol.items():
            print("Node:",node," Color:",color)
    else:
        print("No Solution Exists")
    print()

    #Info: "There are 4 family namely A, B, C, D there are 4 houses namely 1,2,3,4"
    #1. C lives in a house higher than D
    #2. D lives next to A in Lower number House
    #3. There is at least one house between D and B
    #4. C doesn't live in house number 3
    #5. B doesn't live in house number 1
    locs = [1,2,3,4]
    houses = ['A','B','C','D']
    sol = backtrack_house(houses, locs)
    print("Constraint Satisfaction Problem(House Allocation)")
    if sol:
        display_house(sol)
        for node in sol:
            print("House:",node," Location:",sol[node])
    else:
        print("No Solution Exists")
main()
"""
bfs = """
import networkx as nx
import matplotlib.pyplot as plt

def display(graph, directed = False):
    g = nx.DiGraph(graph) if directed else nx.Graph(graph)
    nx.draw(g, with_labels = True)
    plt.suptitle("Breadth First Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def BFS(graph, start, goal):
    queue = [start]
    visited = []
    parent = {start : None}
    while queue:
        node = queue.pop(0)#First element
        visited.append(node)
        if node == goal:
            print(f"Result(BFS {start} to {goal}):",print_path(node, parent))
            return True 
        for adj in graph[node]:
            if adj not in visited and adj not in queue:
                queue.append(adj)
                parent[adj] = node
    print(f"Result(BFS {start} to {goal}): No Solution")
    return False
def get_graph(directed = False):
    graph = {}
    print("Enter edge (u, v)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], {v.strip() for v in x[1].strip(' []').split(',') if v}
        graph[u] = graph.get(u,set()) | adj
        for v in adj:
            graph[v] = graph.get(v,set()) | ({u} if not directed else set())
        x = input()
    return graph
def example():
    graph = {"A" : ["B","C","D"],
             "B" : ["A","E"],
             "C" : ["A","E","F"],
             "D" : ["A","F"],
             "E" : ["B","G","C"],
             "F" : ["D","C","G"],
             "G" : ["E","F"]}
    display(graph)
    print(graph)
    BFS(graph, "A", "F")
    
def main():
    #example();return #Uncomment to run the example
    graph = get_graph(directed = False)#undirected graph
    source, goal = input("Enter source and goal: ").split()
    display(graph, directed = False)
    print(graph)
    BFS(graph, source, goal)
    
    #Sample output
    #Enter edge (u, v)
    #[PRESS ENTER TO STOP]
    #A B
    #A C
    #A D
    #B E
    #C E
    #C F
    #D F
    #E G
    #F G

    #Enter source and goal: A F
    #Result(BFS A to F): ['A', 'D', 'F']
main()
"""
dfs = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, directed = False):
    g = nx.DiGraph(graph) if directed else nx.Graph(graph)
    nx.draw(g, with_labels = True)
    plt.suptitle("Depth First Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def DFS(graph, start, goal):
    stack = [start]
    visited = []
    parent = {start : None}
    while stack:
        node = stack.pop()#last element
        visited.append(node)
        if node == goal:
            print(f"Result(DFS {start} to {goal}):",print_path(node, parent))
            return True
        for adj in graph[node]:
            if adj not in visited and adj not in stack:
                stack.append(adj)
                parent[adj] = node
    print(f"Result(DFS {start} to {goal}): No Solution")
    return False
def get_graph(directed = False):
    graph = {}
    print("Enter edge (u, v)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], {v.strip() for v in x[1].strip(' []').split(',') if v}
        graph[u] = graph.get(u,set()) | adj
        for v in adj:
            graph[v] = graph.get(v,set()) | ({u} if not directed else set())
        x = input()
    return graph
def example():
    graph = {"A" : ["B","C","D"],
             "B" : ["A","E"],
             "C" : ["A","E","F"],
             "D" : ["A","F"],
             "E" : ["B","G","C"],
             "F" : ["D","C","G"],
             "G" : ["E","F"]}
    display(graph)
    print(graph)
    DFS(graph, "A", "F")

def main():
    #example();return #Uncomment to run the example
    graph = get_graph(directed = False)#undirected graph
    source, goal = input("Enter source and goal: ").split()
    display(graph, directed = False)
    print(graph)
    DFS(graph, source, goal)

    #Sample output
    #Enter edge (u, v)
    #[PRESS ENTER TO STOP]
    #A B
    #A C
    #A D
    #B E
    #C E
    #C F
    #D F
    #E G
    #F G

    #Enter source and goal: A F
    #Result(DFS A to F): ['A', 'B', 'E', 'G', 'F']
main()
"""
ucs = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, directed = False):
    graph = {u : {v : {'weight' : graph[u][v]} for v in graph[u]} for u in graph}
    g = nx.from_dict_of_dicts(graph)
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels = True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels = nx.get_edge_attributes(g, 'weight'))
    plt.suptitle("Uniform Cost Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def UCS(graph, start, goal):
    queue = [start]
    visited = []
    parent = {start : None}
    cost = {start : 0}
    while queue:
        queue.sort(key = lambda x : cost[x])
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print(f"Result(UCS {start} to {goal}):",print_path(node, parent),"Path cost =",cost[node])
            return True
        for adj in graph[node]:
            if adj not in visited:
                new_cost = cost[node] + graph[node][adj]
                if adj not in queue:
                    queue.append(adj)
                elif new_cost > cost[adj]:
                    continue
                cost[adj] = new_cost
                parent[adj] = node
    print(f"Result(UCS {start} to {goal}): No Solution")
    return False
def get_graph(directed = False):
    graph = {}
    print("Enter edge (u, v, weight)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], [v.strip(' ()') for v in x[1].strip('[]').split(',') if v] 
        if len(adj) == 1:
            v, w = adj[0].split()
            adj = {v : int(w)}
        else:
            adj = {v : int(w) for v, w in zip(adj[::2],adj[1::2])}
        graph[u] = graph.get(u, {}) | adj
        for v, w in adj.items():
            graph[v] = graph.get(v, {}) | ({u : w} if not directed else {})
        x = input()
    return graph
def example():
    graph = {"A" : {"B":9,"C":4,"D":7},
             "B" : {"A":9,"E":11},
             "C" : {"A":4,"E":17,"F":12},
             "D" : {"A":7,"F":14},
             "E" : {"B":11,"G":5,"C":17},
             "F" : {"D":14,"C":12,"G":9},
             "G" : {"E":5,"F":9}}
    display(graph)
    print(graph)
    UCS(graph, "A", "G")

def main():
    #example();return #Uncomment to run the example
    graph = get_graph(directed = False)#undirected graph
    source, goal = input("Enter source and goal: ").split()
    display(graph, directed = False)
    print(graph)
    UCS(graph, source, goal)

    #Sample output
    #Enter edge (u, v, weight) 
    #[Press Enter To Stop]
    #A B 9
    #A C 4
    #A D 7
    #B E 11
    #C E 17
    #C F 12
    #D F 14
    #E G 5
    #F G 9
 
    #Enter source and goal:  A G
    #Result(UCS A to G): ['A', 'B', 'E', 'G'] Path cost = 25
main()
"""
dls = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, directed = False):
    g = nx.DiGraph(graph) if directed else nx.Graph(graph)
    nx.draw(g, with_labels = True)
    plt.suptitle("Depth Limited Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def DLS(graph, start, goal, limit):
    result = recursive_dls(graph, start, goal, limit, [start])
    print(f"Result(DLS {start} to {goal}):",result,"at depth limit =",limit)
def recursive_dls(graph, node, goal, limit, visited):
    if node == goal:
        return [node]
    elif limit == 0:
        return 'cutoff'
    else:
        status = 'failure'
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                result = recursive_dls(graph, adj, goal, limit - 1, visited)
                if result == 'cutoff':
                    status = 'cutoff'
                    visited.remove(adj)
                elif result != 'failure':
                    return [node] + result
        return status
def get_graph(directed = False):
    graph = {}
    print("Enter edge (u, v)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], {v.strip() for v in x[1].strip(' []').split(',') if v}
        graph[u] = graph.get(u,set()) | adj
        for v in adj:
            graph[v] = graph.get(v,set()) | ({u} if not directed else set())
        x = input()
    return graph
def example():
    graph = {"A" : ["B","C","D"],
             "B" : ["A","E"],
             "C" : ["A","E","F"],
             "D" : ["A","F"],
             "E" : ["B","G","C"],
             "F" : ["D","C","G"],
             "G" : ["E","F"]}
    display(graph)
    print(graph)
    DLS(graph, "A", "F", 3)

def main():
    #example();return #Uncomment to run the example
    graph = get_graph(directed = False)#undirected graph
    source, goal, limit = input("Enter source, goal and depthlimit: ").split() 
    display(graph, directed = False)
    print(graph)
    DLS(graph, source, goal, int(limit))

    #Sample output
    #Enter edge (u, v)
    #[Press Enter To Stop]
    #A B
    #A C
    #A D
    #B E
    #C E
    #C F
    #D F
    #E G
    #F G

    #Enter source, goal and depthlimit:  A G 3
    #Result(DLS A to G): ['A', 'D', 'F', 'G'] at depth limit = 3
main()
"""
ids = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, directed = False):
    g = nx.DiGraph(graph) if directed else nx.Graph(graph)
    nx.draw(g, with_labels = True)
    plt.suptitle("Iterative Deepening Depth First Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def IDS(graph, start, goal):
    depth = 0
    while True:
        result = recursive_dls(graph, start, goal, depth, [start])
        print(f"Result(IDS/IDDFS {start} to {goal}):",result,"at depth limit =",depth)
        if result != 'cutoff':
            return
        depth += 1
def recursive_dls(graph, node, goal, limit, visited):
    if node == goal:
        return [node]
    elif limit == 0:
        return 'cutoff'
    else:
        status = 'failure'
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                result = recursive_dls(graph, adj, goal, limit - 1, visited)
                if result == 'cutoff':
                    status = 'cutoff'
                    visited.remove(adj)
                elif result != 'failure':
                    return [node] + result
        return status
def get_graph(directed = False):
    graph = {}
    print("Enter edge (u, v)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], {v.strip() for v in x[1].strip(' []').split(',') if v}
        graph[u] = graph.get(u,set()) | adj
        for v in adj:
            graph[v] = graph.get(v,set()) | ({u} if not directed else set())
        x = input()
    return graph
def example():
    graph = {"A" : ["B","C","D"],
             "B" : ["A","E"],
             "C" : ["A","E","F"],
             "D" : ["A","F"],
             "E" : ["B","G","C"],
             "F" : ["D","C","G"],
             "G" : ["E","F"]}
    display(graph)
    print(graph)
    IDS(graph, "A", "F", 3)

def main():
    #example();return #Uncomment to run the example
    graph = get_graph(directed = False)#undirected graph
    source, goal = input("Enter source, goal: ").split() 
    display(graph, directed = False)
    print(graph)
    IDS(graph, source, goal)

    #Sample output
    #Enter edge (u, v)
    #[PRESS ENTER TO STOP]
    #A B
    #A C
    #A D
    #B E
    #C E
    #C F
    #D F
    #E G
    #F G
 
    #Enter source, goal:  A G
    #Result(IDS/IDDFS): cutoff at depth limit = 0
    #Result(IDS/IDDFS): cutoff at depth limit = 1
    #Result(IDS/IDDFS): cutoff at depth limit = 2
    #Result(IDS/IDDFS): ['A', 'D', 'F', 'G'] at depth limit = 3
main()
"""
astar = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, h, directed = False):
    graph = {u+" "+str(h[u]) : {v+" "+str(h[v]) : {'weight' : graph[u][v]} for v in graph[u]} for u in graph}
    g = nx.from_dict_of_dicts(graph)
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels = True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels = nx.get_edge_attributes(g, 'weight'))
    plt.suptitle("AStar Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def AStar(graph, start, goal, h):
    queue = [start]
    visited = []
    parent = {start : None}
    g = {start : 0}
    f = {start : h[start]}
    while queue:
        queue.sort(key = lambda x : f[x])
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print(f"Result(AStar {start} to {goal}):",print_path(node, parent),"Path cost =",g[node])
            return True
        for adj in graph[node]:
            if adj not in visited:
                gcost = g[node] + graph[node][adj]
                fcost = gcost + h[adj]
                if adj not in queue:
                    queue.append(adj)
                elif fcost > f[adj]:
                    continue
                g[adj] = gcost
                f[adj] = fcost
                parent[adj] = node
    print(f"Result(AStar {start} to {goal}): No Solution")
    return False
def get_graph(directed = False):
    graph = {}
    heuristic = {}
    
    print("Enter (node, heuristic)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split()
        u, heuristic[u] = x[0], int(x[1])
        graph[u] = graph.get(u, {})
        x = input()
    
    print("Enter edge (u, v, weight)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], [v.strip(' ()') for v in x[1].strip('[]').split(',') if v] 
        if len(adj) == 1:
            v, w = adj[0].split()
            adj = {v : int(w)}
        else:
            adj = {v : int(w) for v, w in zip(adj[::2],adj[1::2])}
        graph[u] = graph.get(u, {}) | adj
        for v, w in adj.items():
            graph[v] = graph.get(v, {}) | ({u : w} if not directed else {})
        x = input()
    return graph, heuristic
def example():
    graph = {"A" : {"B":9,"C":4,"D":7},
             "B" : {"A":9,"E":11},
             "C" : {"A":4,"E":17,"F":12},
             "D" : {"A":7,"F":14},
             "E" : {"B":11,"G":5,"C":17},
             "F" : {"D":14,"C":12,"G":9},
             "G" : {"E":5,"F":9}}
    heuristic = {"A":21,"B":14,"C":18,"D":18,"E":5,"F":8,"G":0}
    print("Heuristic: ",heuristic)
    print(graph)
    display(graph, heuristic)
    AStar(graph, "A", "G", heuristic)

def main():
    #example();return #Uncomment to run the example
    graph, h = get_graph(directed = False)#undirected graph
    source, goal = input("Enter source and goal: ").split()
    display(graph, h, directed = False)
    print("Heuristic: ",h)
    print(graph)
    AStar(graph, source, goal, h)

    #Sample output
    #Enter (node, heuristic)
    #[PRESS ENTER TO STOP]
    #A 21
    #B 14
    #C 18
    #D 18
    #E 5
    #F 8
    #G 0
 
    #Enter edge (u, v, weight)
    #[PRESS ENTER TO STOP]
    #A B 9
    #A C 4
    #A D 7
    #B E 11
    #C E 17
    #C F 12
    #D F 14
    #E G 5
    #F G 9
 
    #Enter source and goal:  A G
    #Result(AStar A to G): ['A', 'B', 'E', 'G'] Path cost = 25
main()
"""
idastar = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, h, directed = False):
    graph = {u+" "+str(h[u]) : {v+" "+str(h[v]) : {'weight' : graph[u][v]} for v in graph[u]} for u in graph}
    g = nx.from_dict_of_dicts(graph)
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels = True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels = nx.get_edge_attributes(g, 'weight'))
    plt.suptitle("IDAStar Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
INF = float('inf')
def IDAStar(graph, start, goal, h):    
    parent = {start : None}    
    th = h[start]
    while True:
        result, new_th = recursive_dfs(graph, parent, start, goal, 0, h, th)
        if result is not None:
            result = print_path(result, parent)
            cost = sum([graph[n1][n2] for n1, n2 in zip(result,result[1:])])
            print(f"Result(IDAStar {start} to {goal}):",result,"Path cost =",cost)
            return
        elif new_th == INF:
            print(f"Result(IDAStar {start} to {goal}): failure")
            return
        th = new_th
def recursive_dfs(graph, parent, node, goal, g, h, th):
    f = g + h[node]
    if f > th:
        return None, f
    if node == goal:
        return node, f
    min_th = INF
    for adj in graph[node]:
        result, temp_th = recursive_dfs(graph, parent, adj, goal, g + graph[node][adj], h, th)
        if result is not None:
            parent[adj] = node
            return result, temp_th
        elif temp_th < min_th:
            min_th = temp_th
    return None, min_th
def get_graph(directed = False):
    graph = {}
    heuristic = {}
    
    print("Enter (node, heuristic)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split()
        u, heuristic[u] = x[0], int(x[1])
        graph[u] = graph.get(u, {})
        x = input()
    
    print("Enter edge (u, v, weight)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], [v.strip(' ()') for v in x[1].strip('[]').split(',') if v] 
        if len(adj) == 1:
            v, w = adj[0].split()
            adj = {v : int(w)}
        else:
            adj = {v : int(w) for v, w in zip(adj[::2],adj[1::2])}
        graph[u] = graph.get(u, {}) | adj
        for v, w in adj.items():
            graph[v] = graph.get(v, {}) | ({u : w} if not directed else {})
        x = input()
    return graph, heuristic
def example():
    graph = {"A" : {"B":9,"C":4,"D":7},
             "B" : {"A":9,"E":11},
             "C" : {"A":4,"E":17,"F":12},
             "D" : {"A":7,"F":14},
             "E" : {"B":11,"G":5,"C":17},
             "F" : {"D":14,"C":12,"G":9},
             "G" : {"E":5,"F":9}}
    heuristic = {"A":21,"B":14,"C":18,"D":18,"E":5,"F":8,"G":0}
    print("Heuristic: ",heuristic)
    print(graph)
    display(graph, heuristic)
    IDAStar(graph, "A", "G", heuristic)

def main():
    #example();return #Uncomment to run the example
    graph, h = get_graph(directed = False)#undirected graph
    source, goal = input("Enter source and goal: ").split()
    display(graph, h, directed = False)
    print("Heuristic: ",h)
    print(graph)
    IDAStar(graph, source, goal, h)

    #Sample output
    #Enter (node, heuristic)
    #[PRESS ENTER TO STOP]
    #A 21
    #B 14
    #C 18
    #D 18
    #E 5
    #F 8
    #G 0
 
    #Enter edge (u, v, weight)
    #[PRESS ENTER TO STOP]
    #A B 9
    #A C 4
    #A D 7
    #B E 11
    #C E 17
    #C F 12
    #D F 14
    #E G 5
    #F G 9
 
    #Enter source and goal:  A G
    #Result(IDAStar A to G): ['A', 'B', 'E', 'G'] Path cost = 25
main()
"""
smastar = """
import networkx as nx
import matplotlib.pyplot as plt
def display(graph, h, directed = False):
    graph = {u+" "+str(h[u]) : {v+" "+str(h[v]) : {'weight' : graph[u][v]} for v in graph[u]} for u in graph}
    g = nx.from_dict_of_dicts(graph)
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels = True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels = nx.get_edge_attributes(g, 'weight'))
    plt.suptitle("SMAStar Search")
    plt.show()
    plt.clf()
def print_path(node, parent):
    if node != None:
        return print_path(parent[node], parent) + [node]
    return []
def SMAStar(graph, start, goal, h, bound):
    queue = [start]
    visited = []
    parent = {start : None}
    g = {start : 0}
    f = {start : h[start]}
    backup = {}
    while queue:
        queue.sort(key = lambda x : f[x])
        node = queue.pop(0)
        visited.append(node)
        if node == goal:
            print(f"Result(SMAStar {start} to {goal}):",print_path(node, parent),"Path cost =",g[node],"Bound =",bound)
            return True
        successors = []
        for adj in graph[node]:
            if adj in visited:
                continue
            gcost = g[node] + graph[node][adj]
            fcost = gcost + h[adj]
            if adj in queue:
                if fcost >= f[adj]:
                    continue
            elif len(queue) < bound:
                    queue.append(adj)
            else:
                worst = max(queue, key = lambda x : f[x])
                if fcost < f[worst]:
                    backup[worst] = f[worst]
                    queue.remove(worst)
                    queue.append(adj)
                else:
                    continue
            g[adj] = gcost
            f[adj] = fcost
            parent[adj] = node
            successors.append(adj)
        if not successors and node in backup:
            f[node] = backup[node]
        elif not successors:
            f[node] = float('inf')
    print(f"Result(SMAStar {start} to {goal}): No Solution Bound = ",bound)
    return False
def get_graph(directed = False):
    graph = {}
    heuristic = {}
    
    print("Enter (node, heuristic)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split()
        u, heuristic[u] = x[0], int(x[1])
        graph[u] = graph.get(u, {})
        x = input()
    
    print("Enter edge (u, v, weight)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], [v.strip(' ()') for v in x[1].strip('[]').split(',') if v] 
        if len(adj) == 1:
            v, w = adj[0].split()
            adj = {v : int(w)}
        else:
            adj = {v : int(w) for v, w in zip(adj[::2],adj[1::2])}
        graph[u] = graph.get(u, {}) | adj
        for v, w in adj.items():
            graph[v] = graph.get(v, {}) | ({u : w} if not directed else {})
        x = input()
    return graph, heuristic
def example():
    graph = {"A" : {"B":9,"C":4,"D":7},
             "B" : {"A":9,"E":11},
             "C" : {"A":4,"E":17,"F":12},
             "D" : {"A":7,"F":14},
             "E" : {"B":11,"G":5,"C":17},
             "F" : {"D":14,"C":12,"G":9},
             "G" : {"E":5,"F":9}}
    heuristic = {"A":21,"B":14,"C":18,"D":18,"E":5,"F":8,"G":0}
    print("Heuristic: ",heuristic)
    print(graph)
    display(graph, heuristic)
    SMAStar(graph, "A", "G", heuristic, 4)

def main():
    #example();return #Uncomment to run the example
    graph, h = get_graph(directed = False)#undirected graph
    source, goal, bound = input("Enter source and goal and bound: ").split()
    display(graph, h, directed = False)
    print("Heuristic: ",h)
    print(graph)
    SMAStar(graph, source, goal, h, int(bound))

    #Sample output
    #Enter (node, heuristic)
    #[PRESS ENTER TO STOP]
    #A 21
    #B 14
    #C 18
    #D 18
    #E 5
    #F 8
    #G 0
 
    #Enter edge (u, v, weight)
    #[PRESS ENTER TO STOP]
    #A B 9
    #A C 4
    #A D 7
    #B E 11
    #C E 17
    #C F 12
    #D F 14
    #E G 5
    #F G 9
 
    #Enter source and goal:  A G 4
    #Result(SMAStar A to G): ['A', 'C', 'F', 'G'] Path cost = 25 Bound = 4
main()
"""
genetic = """
from random import randint as rint
n = 8
def show(b):
    board = [['_'] * n for _ in range(n)]
    for i in range(n):
        board[int(b[i])-1][i] = 'Q'
    print(f" {' '.join(['_']*n)}")
    for i in board:
        print(f"|{'|'.join(i)}|")
def mutate(b1, b2):
    b1, b2 = list(b1), list(b2)
    x, y = rint(0,n-1), rint(0,n-1)
    b1[x], b2[x] = b2[x], b1[x]
    b1[y] = str(int(y) + 1)
    return (''.join(b1),''.join(b2))
def crossover(b1, b2):
    b1, b2 = list(b1), list(b2)
    x = rint(1,n-1)
    b1[0:x], b2[0:x] = b2[0:x], b1[0:x]
    return (''.join(b1), ''.join(b2))
def fitness(b):
    b = list(b)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if b[i] == b[j] or abs(int(b[i]) - int(b[j])) == j - i:
                attacks += 1
    return attacks
def genetic(gen, pop):
    global n 
    n = len(pop[0])
    pq = pop
    for i in range(1,gen+1):
        pq.sort(key = lambda x : fitness(x))
        b1 = pq.pop(0)
        b2 = pq.pop(0)
        pq.clear()
        if fitness(b1) == 0:
            print("Goal State:",b1,"Generation:",i)
            show(b1)
            return
        x1, x2 = crossover(b1, b2)
        x3, x4 = crossover(b2, b1)
        pq = [x1, x2, x3, x4, *mutate(x1, x2), *mutate(x2, x1), b1, b2]
    print("Most Evolved State:",pq[0],"Generation:",i,"Attacks:",fitness(pq[0]))
    show(pq[0])

def main():
    #no of queens is inferred in genetic()
    print("Genetic Algorithm Example 1(5 Queen): ")
    genetic(1000, ["32152","24345"])
    print()
    print("Genetic Algorithm Example 2(8 Queen): ")
    genetic(1000, ["57142860","56782463"])

    #Sample output
    #Genetic Algorithm Example 1(5 Queen): 
    #Most Evolved State: 14352 Generation: 1000 Attacks: 2
    #Genetic Algorithm Example 2(8 Queen): 
    #Goal State: 57142863 Generation: 1
main()
"""
sa = """
import math
import random
def simulated_annealing(initsol, inittemp, alpha, iters):
    currsol = initsol
    cost = fcost(currsol)
    sol = currsol
    mincost = cost
    temp = inittemp
    for iteration in range(iters):
        neighbor = successors(currsol)
        ncost = fcost(neighbor)
        costdiff = ncost - cost
        if costdiff < 0 or random.random() < math.exp(-costdiff/temp):
            currsol = neighbor
            cost = ncost
            if cost < mincost:
                sol = currsol
                mincost = cost
        temp *= alpha
    return sol, mincost
def fcost(sol):
    return sum([i**2 for i in sol])
def successors(sol, step = 1.0):
    succ = [x + random.uniform(-step,step) for x in sol]
    return succ

def main():
    initsol = [300.0, 400.0]
    inittemp = 1000.0
    alpha = 0.95
    iters = 500
    
    bestsol, cost = simulated_annealing(initsol, inittemp, alpha, iters)
    print("Best Solution:",bestsol)
    print("Best Cost:",cost)

    #Sample input/output (can change due to the use of random)
    #Best Solution: [225.56303970871514, 294.69364950481685]
    #Best Cost: 137723.03194110325
main()
"""
sudoku = """
import math 
import random
def display(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))
    print()
def fill(board):
    for i in range(9):
        choices = list(set(range(1,10)) - set(board[i]) - {0})
        random.shuffle(choices)
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = choices.pop()
def cost(board):
    conflicts = 0
    for n in range(9):
        row = board[n]
        col = [x[n] for x in board]
        conflicts += len(row) - len(set(row))
        conflicts += len(col) - len(set(col))
    for l in [0,3,6]:
        for k in [0,3,6]:
            block = []
            for i in range(0+l,3+l):
                for j in range(0+k,3+k):
                    block.append(board[i][j])
            conflicts += 9 - len(set(block))
    return conflicts
def next(board, fixed):
    neighbor = [[x for x in row] for row in board]
    i = random.randint(0,8)
    cols = [j for j in range(9) if (i,j) not in fixed]
    if len(cols) >= 2:
        j1, j2 = random.sample(cols, 2)
        neighbor[i][j1], neighbor[i][j2] = neighbor[i][j2], neighbor[i][j1]
    return neighbor
def simulated_annealing(board, initial_temp = 1.0, cooling_rate = 0.99, min_temp = 0.001):
    fixed = [(x,y) for x in range(9) for y in range(9) if board[x][y] != 0]
    fill(board)
    current = best = board
    temp = initial_temp
    while temp > min_temp:
        neighbor = next(current,fixed)
        delta = cost(neighbor) - cost(current)
        if delta < 0:
            current = neighbor
            if cost(neighbor) < cost(best):
                best = neighbor
        else:
            if random.random() < math.exp(-delta/temp):
                current = neighbor
        temp *= cooling_rate
    print(f"Sudoku ({'Best Possible State | Attacks = '+str(cost(best)) if cost(best) else 'Solved'})") 
    display(best)

def main():
    board =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    simulated_annealing(board)                                       
main()
"""
alphabeta = """
import networkx as nx
import matplotlib.pyplot as plt
def show_tree(graph):
    graph = {node : [adj for adj in graph[node]] for node in graph}
    terminal_nodes = set()
    for node in graph:
        for i in range(len(graph[node])):
            x = str(graph[node][i])
            if x.isdigit():
                while x in terminal_nodes:
                    x+=" "
                graph[node][i] = x
                terminal_nodes.add(x)
    g = nx.DiGraph(graph)
    levels = nx.single_source_shortest_path_length(g, next(iter(g.nodes)))
    layers = {}
    for node, level in levels.items():
        layers[level] = layers.get(level, []) + [node]
    pos = {}
    for level, nodes in layers.items():
        x_offset = (len(nodes) - 1)/2
        for i, node in enumerate(nodes):
            x = i - x_offset
            y = -level
            pos[node] = (x,y)
    plt.figure(figsize = (8,4))
    nx.draw(g, pos, with_labels = True, 
            node_size = 600, node_color = 'lightgreen',
            font_size = 12, font_family = 'cursive',
            arrows = False, width = 1.5, edge_color = 'red',
            edgecolors = 'black', linewidths = 1.5,
            margins = 0.1, clip_on = False)
    plt.suptitle("Alpha Beta Pruning")
    plt.show()
    plt.clf()
MIN = -float('inf')
MAX = float('inf')
def alphabeta(node, graph, ismax, pruned = [], alpha = MIN, beta = MAX, path = {}):
    if str(node).isdigit():
        return int(node), pruned, path
    option = MIN if ismax else MAX
    for child in graph[node]:
        val, _, _ = alphabeta(child, graph, not ismax, pruned, alpha, beta, path)
        if ismax:
            option = max(option, val)
            alpha = max(option, alpha)
            path[node] = alpha
        else:
            option = min(option, val)
            beta = min(option, beta)
            path[node] = beta
        if alpha >= beta:
            i = graph[node].index(child)+1
            pruned += [f"{node}-{adj}" for adj in graph[node][i:]]
            break
    return option, pruned, path
def show_path(node, graph, path, value):
    for adj in graph[node]:
        if str(adj).isdigit():
            return [node,str(value)]
        if path[adj] == value:
            return [node] + show_path(adj, graph, path, value)
def get_graph():
    graph = {}
    print("Enter edge (u, v)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], [v.strip() for v in x[1].strip(' []').split(',') if v]
        graph[u] = graph.get(u,[]) + adj
        x = input()
    return graph
def example():
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'G'],
        'D' : ['H', 'I'],
        'E' : [10, 5],
        'F' : ['J', 'K'],
        'G' : ['L', 'M'],
        'H' : [11, 12],
        'I' : [8, 9],
        'J' : [8, 5],
        'K' : [12, 11],
        'L' : [12, 9],
        'M' : [8, 7]}

    show_tree(graph)
    print(graph)
    start = 'A'
    
    val, pruned, path = alphabeta(start, graph, True)#True means first node is max
    path = show_path(start, graph, path, val)
    print("Alpha Beta Pruning(Maximize):", val, " Pruned Branches:", (', '.join(pruned) if pruned else None), " Path:",'->'.join(path))
    
    val, pruned, path = alphabeta(start, graph, False)#False means first node is min
    path = show_path(start, graph, path, val)
    print("Alpha Beta Pruning(Minimize):", val, " Pruned Branches:", (', '.join(pruned) if pruned else None), " Path:",'->'.join(path))

def main():
    #example();return #change the example according to question
    graph = get_graph()
    start = input("Enter start node: ")
    show_tree(graph)
    print(graph)
    val, pruned, path = alphabeta(start, graph, True)#True means first node is max
    path = show_path(start, graph, path, val)
    print("Alpha Beta Pruning(Maximize):", val, " Pruned Branches:", (', '.join(pruned) if pruned else None), " Path:",'->'.join(path))
    
    val, pruned, path = alphabeta(start, graph, False)#False means first node is min
    path = show_path(start, graph, path, val)
    print("Alpha Beta Pruning(Minimize):", val, " Pruned Branches:", (', '.join(pruned) if pruned else None), " Path:",'->'.join(path))
    #Sample output
    #Enter edge (u, v)
    #[PRESS ENTER TO STOP]
    #A B
    #A C
    #B D
    #B E
    #C F
    #C G
    #D H
    #D I
    #E 10
    #E 5
    #F J
    #F K
    #G L
    #G M
    #H 11
    #H 12
    #I 8
    #I 9
    #J 8
    #J 5
    #K 12
    #K 11
    #L 12
    #L 9
    #M 8
    #M 7

    #Alpha Beta Pruning(Maximize): 10  Pruned Branches: I-9, J-5, M-7  Path: A->B->E->10
    #Alpha Beta Pruning(Minimize): 8  Pruned Branches: I-9, J-5, M-7, K-11, L-9  Path: A->C->F->J->8

main()
"""
csp_map = """
import networkx as nx
import matplotlib.pyplot as plt
def backtrack(graph, colors):
    assign = {node : -1 for node in graph}
    return rec_backtrack(assign, graph, colors)
def rec_backtrack(assign, graph, colors):
    if -1 not in assign.values():
        return assign
    node = [x for x in assign if assign[x] == -1][0]
    for color in colors:
        if all(assign[adj] != color for adj in graph[node]):
            assign[node] = color
            result = rec_backtrack(assign, graph, colors)
            if result:
                return result
            assign[node] = -1
    return None
def display_map(graph, colors = None):
    g = nx.DiGraph(graph)
    #nx.draw_circular(g, with_labels = True, node_color = colors)
    nx.draw_circular(g, with_labels = True,
                    node_size = 600, node_color = colors,
                    font_size = 12, font_family = 'cursive',
                    arrows = False, width = 1.25,
                    edgecolors = 'black', linewidths = 1.5,
                    margins = 0.375, clip_on = False)
    plt.suptitle("Map Coloring(Constraint Satisfaction Problem)")
    plt.show()
    plt.clf()
def get_graph():
    graph = {}
    print("Enter edge (u, v)")
    print("[PRESS ENTER TO STOP]")
    x = input()
    while x:
        x = x.split(maxsplit = 1)
        u, adj = x[0], {v.strip() for v in x[1].strip(' []').split(',') if v}
        graph[u] = graph.get(u,set()) | adj
        for v in adj:
            graph[v] = graph.get(v,set()) | {u}
        x = input()
    return graph
def example():
    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'C', 'D', 'E'],
        'C' : ['B', 'E'],
        'D' : ['A', 'B', 'E'],
        'E' : ['B', 'C', 'D']}
    colors = ["red","green","blue"]
    sol = backtrack(graph, colors)
    
    if sol:
        display_map(graph, sol.values())
        for (node, color) in sol.items():
            print("Node:",node," Color:",color)
    else:
        print("No Solution Exists")
    

def main():
    #example();return #modify example accordingly
    graph = get_graph()
    #available default colors ["red","green","blue","yellow","orange","violet","pink","brown","black",etc]
    colors = ["red","green","blue"]
    sol = backtrack(graph, colors)
    
    if sol:
        display_map(graph, sol.values())
        for (node, color) in sol.items():
            print("Node:",node," Color:",color)
    else:
        print("No Solution Exists")
    
    #Sample output
    #Enter edge (u, v)
    #[PRESS ENTER TO STOP]
    #A B
    #A C
    #B C
    #B D
    #B E
    #C E
    #D E

    #Node:  A  Color: red
    #Node:  B  Color: green
    #Node:  C  Color: blue
    #Node:  D  Color: blue
    #Node:  E  Color: red
main()
"""
csp_house = """
import networkx as nx
import matplotlib.pyplot as plt
def check(assign, loc):
    #constraints given in the question
    #change it accordinly

    a = assign['A']
    b = assign['B']
    c = assign['C']
    d = assign['D']
    
    #1. C lives in a house higher than D
    if c != -1 and d != -1 and c < d:return False

    #2. D lives next to A in Lower number House
    if d != -1 and a != -1 and (a - d) != 1:return False

    #3. There is at least one house between D and B    
    if d != -1 and b != -1 and abs(d - b) == 1:return False

    #4. C doesn't live in house number 3
    if c != -1 and c == 3:return False

    #5. B doesn't live in house number 1
    if b != -1 and b == 1:return False
        
    if loc in assign.values():
        return False
    return True
def backtrack(houses, locs):
    assign = {house : -1 for house in houses}    
    return rec_backtrack(assign, locs)
def rec_backtrack(assign, locs):
    if check(assign, -1):
        return assign
    choices = [x for x in assign if assign[x] == -1]
    house = choices[0] if choices else None
    for loc in locs:
        if check(assign, loc):
            assign[house] = loc
            res = rec_backtrack(assign, locs)
            if res:
                return res
            assign[house] = -1
    return None
def display_house(result):
    g = nx.Graph()
    nodes = list(result.keys())
    nodes.sort(key = lambda x : result[x])
    nodes = [f"{node}({result[node]})" for node in nodes]
    for u, v in zip(nodes, nodes[1:]):
        g.add_edge(u, v)
    pos = {node : (0, i) for i, node in enumerate(nodes)}
    nx.draw(g, pos, with_labels = True,
            width = 1.5, edge_color = 'red',
            node_size = 800, node_color = 'lightgreen',
            font_size = 12, font_family = 'cursive',
            edgecolors = 'black', linewidths = 1.5,
            margins = 0.2, clip_on = False)
    plt.suptitle("House Allocation(Constraint Satisfaction Problem)")
    plt.show()
    plt.clf()

def main():
    #Info: "There are 4 family namely A, B, C, D there are 4 houses namely 1,2,3,4"
    #1. C lives in a house higher than D
    #2. D lives next to A in Lower number House
    #3. There is at least one house between D and B
    #4. C doesn't live in house number 3
    #5. B doesn't live in house number 1
    locs = [1,2,3,4]
    houses = ['A','B','C','D']
    sol = backtrack(houses, locs)
    if sol:
        display_house(sol)
        for node in sol:
            print("House:",node," Location:",sol[node])
    else:
        print("No Solution Exists")

    #Sample Input/Output
    #House: A  Location: 2
    #House: B  Location: 3
    #House: C  Location: 4
    #House: D  Location: 1
main()
"""
random_sampling = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'height_weight_bmi.csv'
data = pd.read_csv(file_path)

df = pd.DataFrame(data).iloc[:20]
height = df["Standing Height (cm)"].values

sample_size = 10  # Desired sample size
random_sample_no_replacement = np.random.choice(height, size=sample_size, replace=False)  # No replacement
random_sample_with_replacement = np.random.choice(height, size=sample_size, replace=True)  # With replacement

fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot the original height data
axs[0].bar(df.index, height, color='skyblue')
axs[0].set_title('Original Standing Height Data')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Height (cm)')
axs[0].grid(axis='y')

# Plot the random sample without replacement
axs[1].bar(np.arange(sample_size), random_sample_no_replacement, color='orange')
axs[1].set_title('Random Sample of Standing Height (No Replacement)')
axs[1].set_xlabel('Sample Index')
axs[1].set_ylabel('Height (cm)')
axs[1].grid(axis='y')

# Plot the random sample with replacement
axs[2].bar(np.arange(sample_size), random_sample_with_replacement, color='green')
axs[2].set_title('Random Sample of Standing Height (With Replacement)')
axs[2].set_xlabel('Sample Index')
axs[2].set_ylabel('Height (cm)')
axs[2].grid(axis='y')

plt.tight_layout()
plt.show()
"""
z_test = """
import numpy as np
import pandas as pd
#import scipy.stats as stats #comment if deprecated
from scipy import stats #use this way
import matplotlib.pyplot as plt

def random_sampling(population, sample_size, replace = False):
    random_sample = np.random.choice(population, size = sample_size, replace = replace)
    return list(random_sample)

def show_curve(z, critical):
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)  
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Z-distribution', color='blue')
    
    if tail == 1: # Left-tailed
        plt.fill_between(x, y, where=(x < critical), color='red', alpha=0.5, label='Critical Region')
    elif tail == 2: # Two-tailed
        critical_left = stats.norm.ppf(alpha / 2)
        critical_right = stats.norm.ppf(1 - alpha / 2)
        plt.fill_between(x, y, where=(x < critical_left), color='red', alpha=0.5, label='Critical Region (Left)')
        plt.fill_between(x, y, where=(x > critical_right), color='red', alpha=0.5, label='Critical Region (Right)')
    else: # Right-tailed
        plt.fill_between(x, y, where=(x > critical), color='red', alpha=0.5, label='Critical Region')

    plt.axvline(z, color='orange', linestyle='--', label='Z-Statistic') # Z-Statistic
    
    plt.title('Z-Test: Critical Region and Z-Statistic')
    plt.xlabel('Z Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid()
    plt.show()

def z_test(sample, population_mean, alpha, tail):
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)
    # Calculate Z-statistic
    z = (sample_mean - population_mean) / (sample_std / np.sqrt(n))
    if tail == 1: # Left-tailed
        critical = stats.norm.ppf(alpha)
    elif tail == 2: # Two-tailed
        critical = stats.norm.ppf(1 - alpha / 2)
    else: # Right-tailed
        critical = stats.norm.ppf(1 - alpha)
    show_curve(z, critical)
    print(f"Z-Statistic: {z:.4f}, Sample Mean: {sample_mean:.4f}")
    print(f"Critical Value: {critical:.4f}")
    if tail == 1 and z < critical:
        print(f"{z:.4f} < {critical:.4f} Reject the null hypothesis (left-tailed).")
    elif tail == 2 and (z < -critical or z > critical):
        expr = (f"{z:.4f} < {-critical:.4f}") if z < -critical else (f"{z:.4f} > {critical:.4f}")
        print(f"{expr} Reject the null hypothesis (two-tailed).")
    elif tail == 3 and z > critical:
        print(f"{z:.4f} > {critical:.4f} Reject the null hypothesis (right-tailed).")
    else:
        print(f"Fail to reject the null hypothesis.")

file_path = "height_weight_bmi.csv"
column = "Standing Height (cm)"
N = 1000
df = pd.read_csv(file_path) #dataset
df = pd.DataFrame(df).iloc[:N] #1000 records are fetched not all
population = list(df[column].values) #Height column is the population
population_mean = 180
sample_size = 10
sample = random_sampling(population, sample_size)
alpha = 0.05
tail = 1 # Change to 1 for left-tailed, 2 for two-tailed, 3 for right-tailed
z_test(sample, population_mean, alpha, tail)
"""
t_test = """
import numpy as np
import pandas as pd
#import scipy.stats as stats #comment if deprecated
from scipy import stats #use this way
import matplotlib.pyplot as plt

def random_sampling(population, sample_size, replace = False):
    random_sample = np.random.choice(population, size = sample_size, replace = replace)
    return list(random_sample)

def show_curve(t, critical):
    x = np.linspace(-4, 4, 1000)  # Range for t-distribution
    y = stats.t.pdf(x, df=len(sample) - 1)  # PDF of t-distribution
     
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='t-distribution', color='blue')

    if tail == 1: # Left-tailed
        plt.fill_between(x, y, where=(x < critical), color='red', alpha=0.5, label='Critical Region')
    elif tail == 2: # Two-tailed
        critical_left = stats.t.ppf(alpha / 2, df=len(sample) - 1)
        critical_right = stats.t.ppf(1 - alpha / 2, df=len(sample) - 1)
        plt.fill_between(x, y, where=(x < critical_left), color='red', alpha=0.5, label='Critical Region (Left)')
        plt.fill_between(x, y, where=(x > critical_right), color='red', alpha=0.5, label='Critical Region (Right)')
    else: # Right-tailed
        plt.fill_between(x, y, where=(x > critical), color='red', alpha=0.5, label='Critical Region')
    
    plt.axvline(t, color='orange', linestyle='--', label='T-Statistic') # T Statistic
    plt.title('T-Test: Critical Region and T-Statistic')
    plt.xlabel('T Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid()
    plt.show()

def t_test(sample, population_mean, alpha, tail):
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)
    t = (sample_mean - population_mean) / (sample_std / np.sqrt(n))
    dof = n - 1
    
    if tail == 1: # Left-tailed
        critical = stats.t.ppf(alpha, dof)
    elif tail == 2: # Two-tailed
        critical = stats.t.ppf(1 - alpha/2, dof)
    else: # Right-tailed
        critical = stats.t.ppf(1 - alpha, dof)
    show_curve(t, critical)
    print(f"T-Statistic: {t:.4f}, Sample Mean: {sample_mean:.4f}")
    print(f"Critical Value: {critical:.4f}")
    if tail == 1 and t < critical:
        print(f"{t:.4f} < {critical:.4f} Reject the null hypothesis (left-tailed).")
    elif tail == 2 and (t < -critical or t > critical):
        expr = (f"{t:.4f} < {-critical:.4f}") if t < -critical else (f"{t:.4f} > {critical:.4f}")
        print(f"{expr} Reject the null hypothesis (two-tailed).")
    elif tail == 3 and t > critical:
        print(f"{t:.4f} > {critical:.4f} Reject the null hypothesis (right-tailed).")
    else:
        print(f"Fail to reject the null hypothesis.")

file_path = "height_weight_bmi.csv"
column = "Standing Height (cm)"
N = 1000
df = pd.read_csv(file_path) #dataset
df = pd.DataFrame(df).iloc[:N] #1000 records are fetched not all
population = list(df[column].values) #Height column is the population
population_mean = 170
sample_size = 10
sample = random_sampling(population, sample_size)
alpha = 0.05
tail = 2 # Change to 1 for left-tailed, 2 for two-tailed, 3 for right-tailed
t_test(sample, population_mean, alpha, tail)
"""
anova = """
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

def show_curve(F_statistic, critical_value, df_between, df_within):
    x = np.linspace(0, 12, 1000)  # Range for F-distribution
    y = stats.f.pdf(x, df_between, df_within)  # PDF of F-distribution
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='F-distribution', color='blue')

    # Shade the critical region
    plt.fill_between(x, y, where=(x > critical_value), color='red', alpha=0.5, label='Critical Region')
    
    # Draw the F-statistic line
    plt.axvline(F_statistic, color='orange', linestyle='--', label='F-statistic')
    
    plt.title('ANOVA: F-Distribution and Critical Region')
    plt.xlabel('F Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid()
    plt.xlim(0, 12)  # Adjust x-axis limits
    plt.ylim(0, max(y) * 1.1)  # Adjust y-axis limits for better visibility
    plt.show()

# Step 1: Load the dataset
file_path = 'sample_data.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Assume 'Group' is the categorical column and 'Values' is the numerical column.
groups = df.groupby('School')['Values']
# Step 2: Calculate the group means and overall mean
group_means = groups.mean()
overall_mean = df['Values'].mean()

# Step 2: Group the data by 'Group' and calculate means
groups = df.groupby('School')['Values']
group_means = groups.mean()
overall_mean = df['Values'].mean()

# Step 3: Calculate SSB (Sum of Squares Between)
SSB = sum(groups.size()[group] * (group_mean - overall_mean) ** 2 
           for group, group_mean in group_means.items())

# Step 4: Calculate SSW (Sum of Squares Within)
SSW = sum(((group_data - group_means[group_name]) ** 2).sum() 
           for group_name, group_data in groups)

# Step 5: Degrees of freedom
df_between = len(group_means) - 1  # k - 1
df_within = len(df) - len(group_means)  # N - k

# Step 6: Calculate MSB and MSW
MSB = SSB / df_between
MSW = SSW / df_within

# Step 7: Calculate the F-statistic
F_statistic = MSB / MSW

# Step 8: Determine the critical F-value from the F-distribution table
alpha = 0.05  # Significance level
critical_value = stats.f.ppf(1 - alpha, df_between, df_within)

# Step 9: Print results
print(f"F-statistic: {F_statistic:.2f}")
print(f"Critical F-value: {critical_value:.2f}")

show_curve(F_statistic, critical_value, df_between, df_within)
# Step 10: Decision - Reject or Fail to Reject Null Hypothesis
if F_statistic > critical_value:
    print("Reject the null hypothesis (There is a significant difference between group means).")
else:
    print("Fail to reject the null hypothesis (No significant difference between group means).")
"""
linear = """
import numpy as np
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
mean_x = np.mean(x)
mean_y = np.mean(y)
print(x)
print(y)

SS_x = [(x1 - mean_x)**2 for x1 in x]
SS_y = [(y1 - mean_y)**2 for y1 in y]
product = [(x1 - mean_x)*(y1 - mean_y) for x1, y1 in zip(x, y)]

b1 = sum(product)/sum(SS_x)
b0 = mean_y - (b1*mean_x)

def lnr_reg(x):
    return b1*x + b0 #y = mx + c
    
print(f"B0: {b0} and B1: {b1}")
y_cap = [(b0 + b1*x1) for x1 in x]#y = mx + c (m->b1, c->b0)
num = sum([(y1 - y2)**2 for y1, y2 in zip(y_cap, y)])

SE = (num/(len(x) - 2))**0.5
if SE < 1:
    print("Standard Error =", SE, "So Accept The Model")
else:
    print("Standard Error =", SE, "So Reject The Model")

#Finding y value for new value of x
x_val = 6
print("For x =",x_val)
print(f"Linear Regression Equation: y = {b1:.2f}x + {b0:.2f}")
y_val = lnr_reg(x_val)
print("y =",y_val)
"""
logistic = """
import pandas as pd
import numpy as np

data = pd.read_csv("hours_scores_records.csv")
print(data.shape)
print(data.head())

mean_hours = data['Hours'].mean()
print("Hours Mean:", mean_hours)
mean_scores = data['Scores'].mean()
print("Scores Mean:", mean_scores)

data['Hours - Mean_Hours'] = round(data['Hours'] - mean_hours, 3)
mean1 = data['Hours - Mean_Hours'].mean()

data['Scores - Mean_Scores'] = round(data['Scores'] - mean_scores, 3)
mean2 = data['Scores - Mean_Scores'].mean()

data['product'] = data['Hours - Mean_Hours']*data['Scores - Mean_Scores']
mean3 = data['product'].mean()

data['mean_x_squared'] = data['Scores - Mean_Scores']**2
data['mean_x2_squared'] = data['Hours - Mean_Hours']**2

mean_x2 = data['mean_x2_squared'].mean()
slope = mean3/mean_x2
c = mean2 - (slope*mean1)

z = (slope*(data['Hours'].astype(float))) + c
data["y"] = 1/(1+np.exp(-z))
data.to_csv('score_updated.csv', index = False)
print(data.head())
"""