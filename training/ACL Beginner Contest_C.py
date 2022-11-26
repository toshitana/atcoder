n,m =  map(int,input().split())

li = [[0] * n for i in range(n)]

for i in range(m):
    a,b =  map(int,input().split())
    li[a-1][b-1] = 1

import numpy as np
from scipy.sparse.csgraph import connected_components

li = np.array(li)
ans, labels = connected_components(li)

print(ans - 1)