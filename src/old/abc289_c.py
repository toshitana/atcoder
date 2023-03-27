

def count_selections(N, M, S):
    count = 0
    for i in range(2**M):
        selected = [False] * (N + 1)
        for j in range(M):
            if i & (1<<j):
                for x in S[j]:
                    selected[x] = True
        if all(selected[1:]):
            count += 1
    return count
