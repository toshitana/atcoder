# 入力から N 人のハンドルネームを読み込む
n, k = map(int, input().strip().split())
names = [input().strip() for _ in range(n)]

# 上位 K 人のハンドルネームに区切って、辞書順にソートする
names = sorted(names[:k])

# 上位 K 人のハンドルネームを出力する
for name in names:
    print(name)
