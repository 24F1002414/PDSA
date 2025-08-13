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
    
def BFS_parent_info_level_number(AList,start_vertex):
    #initial setup
    parent = {}
    level = {}
    for each_vertex in AList.keys():
        parent[each_vertex] = -1
        level[each_vertex] = -1
    
    # create queue object using class queue
    q = Queue()

    #start from root vertex
    level[start_vertex] = 0
    q.enqueue(start_vertex)

    # iteration until all vertices are visited
    # current_vertex = None
    while (not q.isempty()):
        current_vertex = q.dequeue()
        for adj_vertex in AList[current_vertex]:
            if level[adj_vertex] == -1:
                level[adj_vertex] = level[current_vertex]+1
                parent[adj_vertex] = current_vertex
                q.enqueue(adj_vertex)

    #status of level and parent data
    return (level,parent)

AList = {0:[1,2],1:[3,4],2:[4,3],3:[4],4:[]}
print(BFS_parent_info_level_number(AList,0))