
from Space import *
from Constants import *


def DFS(g: Graph, sc: pygame.Surface):
    fps = 30
    clock = pygame.time.Clock()

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    node = g.start
    while not g.is_goal(node):
        node.set_color(yellow)
        node.draw(sc)
        pygame.display.flip()
        clock.tick(fps)

        is_open = False

        for neighbor in g.get_neighbors(node):
            print(neighbor.value)
            if neighbor.value not in closed_set and neighbor.value not in open_set:
                print(node.value)
                is_open = True
                open_set.append(neighbor.value)
                father[neighbor.value] = node.value
                neighbor.set_color(red)
                neighbor.draw(sc)
                pygame.display.flip()
                clock.tick(fps)
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        if is_open:
            node.set_color(blue)

        else:
            open_set.pop(-1)
            closed_set.append(node.value)
            node.set_color(red)

        node.draw(sc)
        node = g.grid_cells[open_set[-1]]
        pygame.display.flip()
        clock.tick(fps)

    g.start.set_color(orange)
    g.start.draw(sc)
    g.goal.set_color(purple)
    g.goal.draw(sc)

    root_node = g.goal
    des_node = g.grid_cells[father[root_node.value]]
    while des_node != g.start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        des_node.set_color(grey)
        des_node.draw(sc)
        pygame.draw.line(sc, green, (root_node.x, root_node.y),
                         (des_node.x, des_node.y), 1)
        pygame.display.flip()
        clock.tick(fps)

        root_node = des_node
        des_node = g.grid_cells[father[root_node.value]]
    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    # raise NotImplementedError('Not implemented')


def BFS(g: Graph, sc: pygame.Surface):

    fps = 30
    clock = pygame.time.Clock()
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    node = g.start
    while not g.is_goal(node):
        node.set_color(yellow)
        node.draw(sc)
        pygame.display.flip()
        clock.tick(fps)

        for neighbor in g.get_neighbors(node):
            print(neighbor.value)
            if neighbor.value not in closed_set and neighbor.value not in open_set:
                print(node.value)

                open_set.append(neighbor.value)
                father[neighbor.value] = node.value
                neighbor.set_color(red)
                neighbor.draw(sc)
                pygame.display.flip()
                clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        node.set_color(blue)
        node.draw(sc)
        pygame.display.flip()
        clock.tick(fps)
        closed_set.append(open_set.pop(0))
        node = g.grid_cells[open_set[0]]

    g.start.set_color(orange)
    g.start.draw(sc)
    g.goal.set_color(purple)
    g.goal.draw(sc)

    root_node = g.goal
    des_node = g.grid_cells[father[root_node.value]]
    while des_node != g.start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        des_node.set_color(grey)
        des_node.draw(sc)
        pygame.draw.line(sc, green, (root_node.x, root_node.y),
                         (des_node.x, des_node.y), 1)
        pygame.display.flip()
        clock.tick(fps)

        root_node = des_node
        des_node = g.grid_cells[father[root_node.value]]
    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    # raise NotImplementedError('Not implemented')


def UCS(g: Graph, sc: pygame.Surface):
    fps = 25
    clock = pygame.time.Clock()

    visited = set()
    open_set = {}
    open_set[g.start.value] = 0
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    father = [-1]*g.get_len()

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        node_value = min(open_set, key=open_set.get)
        node = g.grid_cells[node_value]
        del open_set[node_value]
        visited.add(node_value)

        node.set_color(yellow)
        node.draw(sc)
        pygame.display.flip()
        clock.tick(fps)

        if g.is_goal(node):
            break

        for neighbor in g.get_neighbors(node):
            if neighbor.value not in visited:
                if neighbor.value in open_set and open_set[neighbor.value] <= cost[node_value] + 1:
                    pass
                else:
                    open_set[neighbor.value] = cost[node_value] + 1
                    father[neighbor.value] = node_value
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.flip()
                    clock.tick(fps)

        node.set_color(blue)
        node.draw(sc)
        pygame.display.flip()
        clock.tick(fps)

    g.start.set_color(orange)
    g.start.draw(sc)
    g.goal.set_color(purple)
    g.goal.draw(sc)

    root_node = g.goal
    des_node = g.grid_cells[father[root_node.value]]
    while des_node != g.start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        des_node.set_color(grey)
        des_node.draw(sc)
        pygame.draw.line(sc, green, (root_node.x, root_node.y),
                         (des_node.x, des_node.y), 1)
        pygame.display.flip()
        clock.tick(fps)

        root_node = des_node
        des_node = g.grid_cells[father[root_node.value]]


def AStar(g: Graph, sc: pygame.Surface):
    fps = 25
    clock = pygame.time.Clock()
    open_set = set([g.start])
    closed_set = set([])
    poo = {}
    poo[g.start] = 0
    father = [-1]*g.get_len()
    par = {}
    par[g.start] = g.start

    while len(open_set) > 0:

        n = None
        for v in open_set:
            if n == None or poo[v]+g.h(v) < poo[n]+g.h(n):
                n = v
        n.set_color(yellow)
        n.draw(sc)
        pygame.display.flip()
        clock.tick(fps)
        if n == None:
            return
        if n == g.goal:
            reconst_path = []

            while par[n] != n:
                reconst_path.append(n)
                n = par[n]
            reconst_path.append(g.start)

            for n in reconst_path:
                n.set_color(grey)
                pygame.draw.line(sc, green, (n.getX(), n.getY()),
                                 (par[n].getX(), par[n].getY()))
                g.draw(sc)

        for m in g.get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                par[m] = n
                poo[m] = poo[n] + 1

                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)
                m.set_color(red)
                m.draw(sc)
                pygame.display.flip()
                clock.tick(fps)
        open_set.remove(n)
        closed_set.add(n)
        g.start.set_color(orange)
    g.start.draw(sc)
    g.goal.set_color(purple)
    g.goal.draw(sc)

    root_n = g.goal
    des_n = g.grid_cells[father[root_n.value]]
    while des_n != g.start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        des_n.set_color(grey)
        des_n.draw(sc)
        pygame.draw.line(sc, green, (root_n.x, root_n.y),
                         (des_n.x, des_n.y), 1)
        pygame.display.flip()
        clock.tick(fps)

        root_n = des_n
        des_n = g.grid_cells[father[root_n.value]]
