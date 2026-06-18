import heapq

# heapq is a Python library used to implement a Priority Queue.
# In UCS, the node with the lowest cost is explored first,
# so a priority queue is required.

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('F', 1)],
    'E': [],
    'F': []
}

def uniform_cost_search(start, goal):

    # Priority queue storing (cost, node)
    pq = [(0, start)]

    # Set to keep track of visited nodes
    visited = set()

    # Continue until the priority queue becomes empty
    while pq:

        # Remove the node with the smallest cost
        cost, node = heapq.heappop(pq)

        # Skip if the node has already been visited
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # If the goal node is reached, return the cost
        if node == goal:
            return cost

        # Explore all neighboring nodes
        for neighbor, edge_cost in graph[node]:

            # Add unvisited neighbors to the priority queue
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor))

    # Return message if goal cannot be reached
    return "Goal not found"


start = 'A'
goal = 'F'

result = uniform_cost_search(start, goal)

# Display the minimum cost from start to goal
print("Minimum Cost:", result)