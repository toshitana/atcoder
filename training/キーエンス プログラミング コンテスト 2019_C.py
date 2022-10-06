import io
from operator import le
import sys
from time import process_time_ns


_INPUT = """\
zxlxbwhcvkpvoahiohfozjtceocbsgdnpnbpuyqejdbwgnapzeyence
"""

sys.stdin = io.StringIO(_INPUT)
s = list(input())
keyence = list("keyence")

count = 0
for i in range(len(keyence)):
    start_keyence = keyence[:i]
    end_keyence = keyence[i:]
    start_s = s[:i]
    end_s = s[-(len(end_keyence)):]

    #print(start_s,end_s,start_keyence,end_keyence)
    if len(start_keyence) == 0:
        if end_s == end_keyence:
            print("YES")
            exit()
    elif len(end_keyence) == 0:
        if start_s == start_keyence:
            print("YES")
            exit()
    else:
        if end_s == end_keyence and start_s == start_keyence:
            print("YES")
            exit()

print("NO")