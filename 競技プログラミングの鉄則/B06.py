import io
from operator import index
import sys

_INPUT = """\
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7
"""

sys.stdin = io.StringIO(_INPUT)

# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [ None ] * Q
R = [ None ] * Q
for i in range(Q):
	L[i], R[i] = map(int, input().split())

# アタリの個数・ハズレの個数の累積和を求める
# 配列 A が 0 番目から始まっていることに注意！
Atari = [ 0 ] * (N + 1)
Hazre = [ 0 ] * (N + 1)
for i in range(1, N+1):
	# アタリについて計算
	Atari[i] = Atari[i - 1]
	if A[i - 1] == 1:
		Atari[i] += 1
	# ハズレについて計算
	Hazre[i] = Hazre[i - 1]
	if A[i - 1] == 0:
		Hazre[i] += 1

# 質問に答える
for i in range(Q):
	NumAtari = Atari[R[i]] - Atari[L[i] - 1]
	NumHazre = Hazre[R[i]] - Hazre[L[i] - 1]
	if NumAtari > NumHazre:
		print("win")
	elif NumAtari == NumHazre:
		print("draw")
	else:
		print("lose")

"""
n = int(input())
li = list(map(int,input().split()))
q = int(input())

li2 = []
sum_ = 0
for i in range(n):
    sum_ +=li[i]
    li2.append(sum_)

print(li2)
for i in range(q):
    a,b = map(int,input().split())
    a = a-1
    b = b-1
    ct = li2[b] - li2[a-1]
    print(a,b,li2[b],li2[a-1],b-a+1,ct)
    if ct*2 > b-a+1:
        print("win")
    elif ct*2 == b-a+1:
        print("draw")
    elif ct*2 < b-a+1:
        print("lose")
"""