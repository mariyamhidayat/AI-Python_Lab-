import heapq

# A* Search Algorithm Function
def a_star(graph, start, goal, heuristic):

    # Priority queue to store nodes that need to be explored
    open_list = []

    # Add the start node with f-cost = 0
    heapq.heappush(open_list, (0, start))

    # Stores the actual cost from start node to each node
    g_cost = {start: 0}

    # Stores parent of each node for path reconstruction
    parent = {start: None}

    # Continue until there are nodes to explore
    while open_list:

        # Remove node with smallest f-cost
        current_f, current = heapq.heappop(open_list)

        # If goal is reached, reconstruct and return the path
        if current == goal:
            path = []

            # Trace back from goal to start using parent dictionary
            while current is not None:
                path.append(current)
                current = parent[current]

            # Reverse path because it was built from goal to start
            return path[::-1]

        # Explore all neighboring nodes
        for neighbor, cost in graph[current]:

            # Calculate new g-cost
            new_g = g_cost[current] + cost

            # Update if node is not visited
            # or a shorter path is found
            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                # Store the better g-cost
                g_cost[neighbor] = new_g

                # Calculate f-cost = g(n) + h(n)
                f = new_g + heuristic[neighbor]

                # Add node to priority queue
                heapq.heappush(open_list, (f, neighbor))

                # Store parent for path reconstruction
                parent[neighbor] = current

    # Return None if no path exists
    return None


# Graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'G': []
}

# Heuristic values (estimated cost to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'G': 0
}

# Find shortest path from A to G
path = a_star(graph, 'A', 'G', heuristic)

# Print the result
print("Path:", path)