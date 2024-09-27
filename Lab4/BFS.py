from collections import deque

def bfs(graph, start, target):
    if start not in graph:
        return f"Error: Starting node '{start}' is not present in the graph."
    
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(f"Visiting: {node}")
        if node == target: return f"Target node '{target}' found!"
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return f"Target node '{target}' not found."

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start_node = input("Enter the starting node for BFS: ")
target_node = input("Enter the target node for BFS: ")
result = bfs(graph, start_node, target_node)
print(result)
