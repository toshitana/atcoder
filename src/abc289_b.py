n, m = map(int, input().split())
a = list(map(int, input().split()))

l = [i for i in range(1, n + 1)]
result = []
start = 0

def missing_numbers(n, li):
    li_set = set(li) # li の要素を集合に変換
    return [i+1 for i in range(n) if i+1 not in li_set] # 1からnまでの数字のうちliに含まれていないものをリストとして返す

lis = missing_numbers(n, a)

for i in lis:
    end = i
    result.append(l[start:end])
    start = end

def split_and_sort_list(li):
    result = []
    for sub_li in li:
        result += sub_li[::-1]
    return result

#print(split_and_sort_list(result).join(' '))

b = split_and_sort_list(result)

x = b
x = [str(i) for i in x]
print(" ".join(x))