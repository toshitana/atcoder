# 入力から N 個の整数のペア (Ai, Bi) を読み込む
n = int(input().strip())
pairs = []
for i in range(n):
    a, b = map(int, input().strip().split())
    pairs.append((a, b))

# 各ペアの Ai + Bi の値を計算する
results = [a + b for a, b in pairs]

# 計算結果を出力する
for result in results:
    print(result)
