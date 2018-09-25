'''
A* is a n informed search algorithm - formulated in terms of weighted graphs.
starting from a specific starting node, aims to find a path to the given goal node having the smallest cost (time, distance)
Does so by maintaining a tree of paths originating at start node and extending those paths one edge at a time until its
termination criterion is satisfied.

each iteration of main loop determines which path to extend
does so based on cost of path and an estimate of the cost required to extend the path all the way to goal
A* star selects the path that minimizes f(n) = g(n) + h(n)
where n is the last node on the path
g(n) is the cost of the path from the start node n
h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal
A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be
extended.
h(n) is problem-specific. If h(n) is admissible, meaning it never overestimates the actual cost to get to the goal, A*
is guaranteed to return a least-cost path from start to goal.
NOTE this is not guaranteed to be efficient.
'''


from implementation import *


def breadth_first_search_1(graph, start):
    # make empty Queue
    frontier = Queue()
    # put start in Queue
    frontier.put(start)

    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print(f"Visiting {current}")

        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def breadth_first_search_2(graph, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from

def breadth_first_search_3(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS

parents = breadth_first_search_3(g, (8,7), (17,2))
draw_grid(g, width=2, point_to=parents, start=(8,7), goal=(17,2))

# breadth_first_search_1(example_graph, 'D')