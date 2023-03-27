from collections import defaultdict

n = int(input())

cnt = defaultdict(int)
for a in range(1, n):
    for b in range(1, n):
        if a * b >= n:
            break
        cnt[a*b] += 1

ans = 0
for c in range(1, n):
    for d in range(1, n):
        if c * d >= n:
            break
        ans += cnt[n - c*d]

print(ans)
