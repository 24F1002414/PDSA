# single source shortest path using Bellman ford algo

def bellmanford_list(WList,s):
    #initialisation
    infinity = float('inf')
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
    distance[s] = 0
    #compute shortest distance from source
    #repeat this n time , n-1 edge relaxing - outer loop
    for i in WList.keys():
        #check for each adjacent of u Two nested loops
        for u in WList.keys():
            for v,d in WList[u]:
                if distance[v]> distance[u]+d: 
                    distance[v] = distance[u]+d
    return distance            

edges = [
    (0,1,10),
    (0,7,8),
    (1,5,2),
    (2,1,1),
    (2,3,1),
    (3,4,3),
    (4,5,-1),
    (5,2,-2),
    (6,1,-4),
    (6,5,-1),
    (7,6,1)]

size = 8
WL = {}
for i in range(size):
    WL[i] = []
print(WL)
for u,v,d in edges:
    WL[u].append((v,d))
print(WL)

print(bellmanford_list(WL,0))



# def shortestCircularRoute(WList,S):
#     ans = float('inf')
#     for U,w in WList[S]:
#         WL_copy = copy.deepcopy(WList)
#         WL_copy[U] = [(v,wt) for v,wt in WL_copy[U] if v!=S]
#         WL_copy[S] = [(v,wt) for v,wt in WL_copy[S] if v!=U]

#         dist = dijkstra(WL_copy,U)
#         if S in dist and dist[S]<float('inf'):
#             ans = min(ans,w+dist[s])
#     return ans if ans<float('inf') else -1  

