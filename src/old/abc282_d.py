from collections import defaultdict

def is_bipartite(n, edges):
    """
    二部グラフ判定アルゴリズム
    """
    # 各頂点を奇数番目か偶数番目の部分に割り当てる
    colors = [0] * (n + 1)

    # 隣接リストを作成する
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 幅優先探索で二部グラフであるかどうかを判定する
    from queue import Queue
    q = Queue()

    for u in range(1, n + 1):
        if colors[u] != 0:
            continue
        colors[u] =        q.put(u)
        while not q.empty():
            v = q.get()
            for to in adj_list[v]:
                if colors[to] == colors[v]:
                    return False
                if colors[to] == 0:
                    colors[to] = colors[v]
                    q.put(to)
    return True

# 入力を受け取る
N, M = map(int, input().split())

# グラフ G の边集を表す配列を用意する
edges = []
for i in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

# 結果を出力する
count = 0
for u in range(1, N + 1):
    for v in range(u + 1, N + 1):
        # 頂点 u と頂点 v を結ぶ辺が存在しない場合
        if (u, v) not in edges and (v, u) not in edges:
            # 頂点 u と頂点 v を結ぶ辺を追加し、二部グラフであるかどうかを判定する
            if is_bipartite(N, edges + [(u, v)]):
                count += 1
print(count)
