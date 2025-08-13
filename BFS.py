class Queue:
    def __init__(self):
        self.queue =[]

    def isempty(self):
        return self.queue == []
    
    def enqueue(self,v):
        self.queue.append(v)

    def dequeue(self):
        v= None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def __str__(self):
        return str(self.queue)
    
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(40)
# q.enqueue(60)
# print(q)
# print(q.dequeue())
# print(q.dequeue())
# print(str(q.queue))

def BFSList(AList,start_vertex):

    #initial setup
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False
    q = Queue()

    # start from root vertex
    visited[start_vertex] = True
    q.enqueue(start_vertex)

    #iteration until all vertices are visited
    while (not q.isempty()):
        # Remove current vertex from queue and visit its neighbour
        curr_vertex = q.dequeue()
        # adj of current vertex
        for adj_vertex in AList[curr_vertex]:
            if not visited[adj_vertex]: 
                 visited[adj_vertex] = True
                 q.enqueue(adj_vertex)
    #final status of visited
    return visited

#main
AList = {0:[1,2],1:[3,4],2:[4,3],3:[4],4:[]}
print(BFSList(AList,0))