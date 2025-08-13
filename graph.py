import numpy as np
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)

# Amat = np.zeros(shape=(size,size))
# for (i,j) in E:
#     Amat[i,j] = 1
# print(Amat)

# Amat = []
# for i in range(size):
#     row = []
#     for j in range(size):
#         row.append(0)
#     Amat.append(row.copy())
# for (i,j) in E:
#     Amat[i][j] = 1

# print(Amat)

# Alist ={}
# for i in range(size):
#     Alist[i]=[]
# for (i,j) in E:
#     Alist[i].append(j)
# print(Alist)

UE = E+[ (j,i) for (i,j) in E]
# Amat = np.zeros(shape=(size,size))
# for (i,j) in UE:
#     Amat[i,j] = 1
# print(Amat)
# #Adjacency list representation using list (undirected)
# Amat = []
# for i in range(size):
#     row = []
#     for j in range(size):
#         row.append(0)
#     Amat.append(row.copy())

# for (i,j) in UE:
#     Amat[i][j] = 1
# print(Amat)
        
#Adjacency list representation using dictionary (undirected)
AList ={}
for i in range(size):
    AList[i]=[]

for (i,j) in UE:
        AList[i].append(j)
print(AList)