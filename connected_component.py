class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,v):
        self.queue.append(v)

    def isempty(self):
        return self.queue ==[]
    
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def __str__(self):
        return str(self.queue)
    

def BFSList(AList,start_vertex):
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False
    q = Queue()

    visited[start_vertex] = True
    q.enqueue(start_vertex)

    while not q.isempty():
        curr_vertex = q.dequeue()
        for adj_vertex in AList[curr_vertex]:
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)
    return visited

# Implementation to find connected components in graph
def components(AList):
    #initialisation of component,comp_id,seen
    component = {}
    compid,seen = (0,0)

    for v in AList.keys():
        component[v] = -1

    #Repeat until seen value reached to all vertices
    while(seen<max(AList.keys())):
        #select start vertex for BFS (min vertex in graph)
        startv = min( i for i in AList.keys() if component[i] == -1)

       # Call the BFS
        visited = BFSList(AList,startv)

       # Assign compid to each reachable vertex from start vertex
        for v in visited.keys():
            if visited[v]:
                seen +=1
                component[v] = compid
        compid +=1

    return component

#main

AList = {
    0: [1],
    1: [2],
    2: [0],
    3: [4,6],
    4: [3,7],
    5: [3,7],
    6: [5],
    7: [4,8],
    8: [5,9],
    9: [8],
}

print(components(AList))


