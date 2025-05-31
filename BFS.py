def BFS(graph, start):
    queue=[]
    queue.append(start)
    visited={}
    distance = {node: float("inf") for node in graph}
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}

    for i in graph:
        visited[i]=False
    while queue:

        x=queue.pop(0)

        visited[start]=True

        for i in graph[x]:
            if i in queue:
                pass
            elif visited[i]==False:
                queue.append(i)
                visited[i]=True
                parent[i]=x
                print(i)

    print(parent)


graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C','E','F'],
    'E': ['D', 'F','G'],
    'F': ['D', 'E', 'H'],
    'G': ['E', 'H'],
    'H': ['G','F']
}
BFS(graph, 'C')