
graph = {
    '10': ['20', '30'],
    '20': ['40', '50'],
    '30': ['60'],
    '40': [],
    '50': ['60'],
    '60': [],
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth First Traversal")
bfs(visited,graph, '10')


