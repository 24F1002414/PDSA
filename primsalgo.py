#Prims algo
def prims_list(WList):
    #Initialisation
    infinity = float('inf')
    (visited,distance,TE) = ({},{},[])

    for v in WList.keys():
        visited[v],distance[v] = (False,infinity)

    #Update start vertex 0 and its adjacent weights
    visited[0] = True
    for v,d in WList[0]:
        distance[v] = d 

    # Repeat the process n-1 times (ie , vertices-1)
    for i in range(1,len(WList.keys())):
        min_dist = infinity 
        nextv = None
        for u in WList.keys():
            for (v,d) in WList[u]:
                if visited[u] and (not visited[v]) and d< min_dist:
                    min_dist = d
                    nextv = v
                    nexte = (u,v)
        visited[nextv] = True
        TE.append(nexte)

        #Update the distance of unvisited adjacents
        for (v,d) in WList[nextv]:
            if not visited[v]:
                if d<distance[v]:
                    distance[v] = d
    return TE
dedges = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
size = 5
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))
print(prims_list(WL))