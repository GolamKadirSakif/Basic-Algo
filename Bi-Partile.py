def Bi(graph, start):
    queue=[]
    queue.append(start)
    visited={}
    distance = {node: float("inf") for node in graph}
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}
    color = {node: "White" for node in graph}

    visited[start]=True
    color[start]='Red'

    while queue:

        x=queue.pop(0)

        
        for i in graph[x]:
            if i in queue:
                pass
            elif visited[i]==False and color[i]=="White":
                queue.append(i)
                visited[i]=True
                parent[i]=x
                if color[x]=="White" or color[x]=="Red":
                    color[i]="Blue"
                else:
                    color[i]='Red'
            elif color[x]==color[i]:

                return -1

            

                
                         

        

    print(parent)
    print(color)


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
print(Bi(graph, 'A'))