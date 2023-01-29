n,m = map(int,input().split())
s = [input() for _ in range(n)]

t = [input() for _ in range(m)]

count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
            break

print(count)
