def count_marks(n, d, mid):
    x = mid
    count = 1
    while True:
        x = (x + d) % n
        if x == mid:
            break
        count += 1
    return count

t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        if count_marks(n, d, mid) < k:
            low = mid + 1
        else:
            high = mid
    print(low)
