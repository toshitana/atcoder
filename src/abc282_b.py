N, M = map(int, input().split())

# 各参加者の解ける問題の番号を表すビットマスクを取得する
masks = []
for i in range(N):
    S = input()
    mask = 0
    for j in range(M):
        if S[j] == 'o':
            mask |= 1 << j
    masks.append(mask)

# 2 人の参加者で M 問全てを解けるようなペアをカウントする
count = 0
for i in range(N):
    for j in range(i + 1, N):
        if masks[i] | masks[j] == (1 << M) - 1:
            count += 1

print(count)