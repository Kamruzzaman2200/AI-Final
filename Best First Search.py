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
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 6,
    'G': 8
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    while not pq.empty():
        _, current = pq.get()
        if current in visited:
            continue

        print("Visited:", current)
        visited.add(current)

        if current == goal:
            print("Goal Found!")
            return

        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Call the function outside of its definition
best_first_search("A", "G")
