def dfs(graph, node, target, visited=None):
    if visited is None:
        visited = set()
    
    if node not in graph:
        return f"Error: Starting node '{node}' is not present in the graph."

    visited.add(node)
    print(f"Visiting: {node}")

    if node == target:
        return f"Target node '{target}' found!"

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, target, visited)
            if result: return result

    return f"Target node '{target}' not found."

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F'],
    'E': [],
    'F': []
}
start_node_dfs = input("Enter the starting node for DFS: ")
target_node_dfs = input("Enter the target node for DFS: ")
result_dfs = dfs(graph, start_node_dfs, target_node_dfs)
print(result_dfs)
