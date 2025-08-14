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
def longestpathlist(AList):

    #initial setup
    (indegree,lpath) = ({},{})
    
    for u in AList.keys():
        indegree[u],lpath[u] = 0,0

    # Update indegree values
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] +=1
    
    # Add zero degree vertices to queue
    zerodegreeq = Queue()
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.enqueue(u)

    #Repeat iteration until queue is empty
    while (not zerodegreeq.isempty()):
        curr_vertex = zerodegreeq.dequeue()
        indegree[curr_vertex] -= 1
        # Nested loop to find adjacent of current vertex
        for adj_vertex in AList[curr_vertex]:
            indegree[adj_vertex] -=1
            #update longest path value with maximum
            lpath[adj_vertex] = max(lpath[adj_vertex],lpath[curr_vertex]+1)
            if indegree[adj_vertex] ==0:
                zerodegreeq.enqueue(adj_vertex)
    return lpath

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

print(longestpathlist(AList))