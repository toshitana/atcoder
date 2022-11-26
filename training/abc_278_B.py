import io
import sys

_INPUT = """\
20 40
"""

sys.stdin = io.StringIO(_INPUT)

H,M = map(int,input().split())

H_li = list(map(str,str(H).zfill(2)))
M_li = list(map(str,str(M).zfill(2)))

def judge(H_li,M_li):
    h = int(H_li[0] + M_li[0])
    m = int(H_li[1] + M_li[1])
    if h == 24 and m >= 0:
        return False
    if 0 <=  m <= 59:
        if 0 <= h <=24:
            return True
    else:
        return False

while True:
    H_li = list(map(str,str(H).zfill(2)))
    M_li = list(map(str,str(M).zfill(2)))
    if judge(H_li,M_li):
        print(str(H).zfill(2),str(M).zfill(2))
        exit()

    if 0 <=  M < 59:
        M +=1
    else:
        M = 0
        if H == 24:
            H = 0
        else:
            H +=1
    if H == 24 and M == 0:
        H =0
        M = 0