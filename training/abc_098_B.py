"""
https://github.com/IsHYuhi/AtCoder_Python/blob/master/ABC/ABC098/B.py
非常に鮮やかな回答例だった
全箇所で切っていって、Counterで辞書型のkeysと個数を作成
.keys()でkeyのみのリストに
リスト＆リストで共通要素のみのリストにすれば、長さが共通するユニークな文字の数になる
"""

from collections import Counter
n = int(input())
s = input()
ans = 0

for i in range(n-1):
  a,b = Counter(s[:i+1]),Counter(s[i+1:])
  c = a.keys() & b.keys()
  ans = max(ans,len(c))
print(ans)