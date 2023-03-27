n, k = map(int, input().split())
s = input()

o_count = s.count("o")
x_count = n - o_count
k_o_count = k if k <= o_count else o_count

result = list(s)
for i in range(n):
    if result[i] == "o":
        k_o_count -= 1
        if k_o_count < 0:
            result[i] = "x"

print("".join(result))
