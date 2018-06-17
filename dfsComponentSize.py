def dfsComponentSize(matrix, vertex):
    q=[vertex]
    v=[]
    while len(q)>0:
        cur = q.pop()
        v.append(cur)
        for i in range(len(matrix[cur])):
            if matrix[cur][i] and i not in v:
                v.append(i)
    return len(v)