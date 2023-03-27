n = int(input())

s=[input() for i in range(n)]

count_for = s.count("For")

if count_for > n/2:
    print("Yes")
else:
    print("No")
