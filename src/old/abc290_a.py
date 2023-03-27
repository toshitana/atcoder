n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_score = 0
for i in b:
    total_score += a[i-1]

print(total_score)
