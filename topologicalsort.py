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
    
#Implementing topological short
def toposortlist(AList):

    #initial setup
    (indegree,topsort) = ({},[])
    zerodegreeq = Queue()
    for u in AList.keys():
        indegree[u] = 0

    #compute in-degree
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] +=1

    # find vertices with indegree 0 and add them to queue
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.enqueue(u)

    #Iterate until queue is empty
    while (not zerodegreeq.isempty()):
        #delete vertex with indegree zero from queue
        curr_vertex = zerodegreeq.dequeue()
        topsort.append(curr_vertex)

        #decrease current vertex in-degree
        indegree[curr_vertex] -=1

        #Nested iteration for adjacent of current vertex
        for adj_vertex in AList[curr_vertex]:
            indegree[adj_vertex] -=1
            if indegree[adj_vertex] ==0:
                zerodegreeq.enqueue(adj_vertex)

    return topsort

AList = {
    0: [2,3,4],
    1: [2,7],
    2: [5],
    3: [5,7],
    4: [7],
    5: [6],
    6: [7],
    7: [],
}

print(toposortlist(AList))