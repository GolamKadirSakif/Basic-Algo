import heapq
def Dijkstra(graph, start):


    queue=[]
    
    distance = {node: float("inf") for node in graph}
    
    parent = {node: None for node in graph}
    

    #Initilization

    distance[start] = 0

    heapq.heappush(queue,(0,start))



    while queue:

        y,x=heapq.heappop(queue)

        

        for i in graph[x]:
            weight=graph[x][i]
            
            if distance[i]==float("inf") or (distance[x]+weight)<distance[i]:
                heapq.heappush(queue,(weight,i))

                
                parent[i]=x
                
                distance[i]=distance[x]+weight

            else:
                
                distance[i]=distance[x]+weight


                

    print(parent)
    print(distance)


graph = {
    'A': {'B': 3, 'C': 5},
    'B': {},  # B no longer points back to A
    'C': {'D': 2},  # C only points forward
    'D': {'E': 4, 'F': 6},  # D's edges are strictly outward
    'E': {'F': 3, 'G': 7},  # E only moves forward
    'F': {'H': 8},  # F strictly directs to H
    'G': {'H': 1},  # G only moves to H
    'H': {}  # H has no outgoing edges
}


Dijkstra(graph, 'A')







# Stress-Testing
import random
import heapq

# Generate a random weighted graph with N nodes
def generate_graph(N, density=0.5):
    graph = {str(i): {} for i in range(N)}

    for i in range(N):
        for j in range(N):
            if i != j and random.random() < density:  # Control edge density
                graph[str(i)][str(j)] = random.randint(1, 20)  # Random weight

    return graph

#grah=generate_graph(1000)
#Dijkstra(grah, '1')

