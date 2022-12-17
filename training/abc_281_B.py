import io
from operator import index
import sys

_INPUT = """\
X900000
"""

sys.stdin = io.StringIO(_INPUT)

# S を入力
S = input()

# S の長さが 1 以上 10 以下であるかどうかを確認
if len(S) < 1 or len(S) > 10:
  print("No")
  exit()

# S の先頭が英大文字であるかどうかを確認
if not S[0].isupper():
  print("No")
  exit()

# S の2文字目から7文字目までが 100000 以上 999999 以下の整数を
# 10 進表記して得られるかどうかを確認
try:
    num = int(S[1:7])
except:
  print("No")
  exit()
if num < 100000 or num > 999999:
  print("No")
  exit()

# S の8文字目が英大文字であるかどうかを確認
if len(S) < 8:
  print("No")
  exit()

if len(S) >= 8 and not S[7].isupper():
  print("No")
  exit()

# すべての条件を満たしているため、S は条件を満たす
print("Yes")
