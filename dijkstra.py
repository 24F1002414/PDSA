#Single source shortest path using dijkstra 

def dijkstras_list(WList,s):
    #Initialisation
    infinity =1+len(WList.keys()) * max([ d for u in WList.keys() for (v,d) in WList[u]])
    (visited,distance) = {},{}
    for v in WList.keys():
        visited[v],distance[v] = (False,infinity)
    distance[s] = 0
    
    #compute shortest distance for each vertex-outer loop
    for u in WList.keys():
        #find minimum distance of unvisited vertices
        min_dist = min([ distance[v] for v in WList.keys() if not visited[v]])

        #find the min distance matching vertices may be multiple vertices have same distance
        nextv_list = [ v for v in WList.keys() if (not visited[v]) and distance[v] == min_dist]

    #select alpha/numerically smaller vertex
        nextv = min(nextv_list)
        visited[nextv] = True

        #Iterate over each adjacent vertex of next_v - Inner loop
        for v,d in WList[nextv]:
            #update distance
            if distance[v] > distance[nextv] + d:
                distance[v] = distance[nextv] + d

    return distance

dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7

WL = {}
for i in range(size):
    WL[i] = []
for u,v,d in dedges:
    WL[u].append((v,d))
print(dijkstras_list(WL,0))
print(WL)