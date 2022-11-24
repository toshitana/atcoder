import io
import sys

_INPUT = """\
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
"""

sys.stdin = io.StringIO(_INPUT)

# 遅い（main関数を使う） -> PyPyでは265 ms（Pythonでは431 ms）
def main():
    N,M = map(int,input().split())
    list1 = []
    for i in range(N):
        list1.append([])

    for i in range(M):
        a,b = map(int,input().split())
        list1[a-1].append(b)
        list1[b-1].append(a)

    for i in list1:
        s = str(len(i)) + " " + ' '.join(map(str, sorted(i)))
        print(s)

if __name__ == '__main__':
    main()