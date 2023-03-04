n, q = map(int, input().split())  # 選手数 n とイベント数 q を取得

# 選手ごとのカードの状態を初期化する
# 状態はイエローカードの枚数 (0 〜 2) と退場処分を受けたかどうかの真偽値で表す
players = [[0, False] for _ in range(n)]

# イベントを処理する
for _ in range(q):
    event = input().split()  # イベントを取得
    x = int(event[1]) - 1  # 選手番号を 0-indexed に変換する

    if event[0] == "1":  # イエローカードを提示する
        if players[x][1]:  # 既に退場処分を受けていたら何もしない
            continue
        players[x][0] += 1  # イエローカードの枚数を増やす
        if players[x][0] == 2:  # イエローカードが 2 枚なら退場処分を与える
            players[x][1] = True

    elif event[0] == "2":  # レッドカードを提示する
        if players[x][1]:  # 既に退場処分を受けていたら何もしない
            continue
        players[x][1] = True  # 退場処分を与える

    elif event[0] == "3":  # 退場処分を受けたかを質問する
        if players[x][1]:  # 退場処分を受けていたら Yes を出力する
            print("Yes")
        else:  # 退場処分を受けていなかったら No を出力する
            print("No")
