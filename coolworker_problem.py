def coolWorkers(AList,preference):
    n = len(AList.keys())
    indegree = {}
    toposortlist = []
    for i in AList.keys():
        indegree[i] = 0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] +=1
    
    for i in range(n):
        availableTasks = [ k for k in AList if indegree[k] ==0]
        t = [(preference.index(i),i) for i in availableTasks]
        t.sort()  # sorts list t inplace (changes list t by sorting it originally)
        j= t[0][1]
        toposortlist.append(j)
        indegree[j] -=1
        for k in AList[j]:
            indegree[k] -=1
    
    return toposortlist

AList = eval(input())
preference = eval(input())
print(coolWorkers(AList, preference))