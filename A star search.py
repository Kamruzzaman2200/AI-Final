#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sohel
#
# Created:     19/05/2025
# Copyright:   (c) sohel 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 6,
    'G': 8
}

def a_star_search(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, start, [start]))
    visited = set()

    while not pq.empty():
        f, g, current, path = pq.get()
        print("Visited:", current)

        if current == goal:
            print("Goal Found!", path)
            return path

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

    print("Goal not reachable.")
    return None


a_star_search('A', 'G')
