import io
import sys

_INPUT = """\
1000000000 1000000000 999999999 999999999
"""

sys.stdin = io.StringIO(_INPUT)

x1,y1,x2,y2 = map(int,input().split())

if (x1 - x2)**2 + (y1 - y2)**2 > 20:
    print("No")
    exit()

#print(min(x1,x2)-10,max(x1,x2)+10)
for i in range(min(x1,x2)-10,max(x1,x2)+10):
    for j in range(min(y1,y2)-10,max(y1,y2)+10):
        if (x1 - i)**2 + (y1 - j)**2 == 5:
            if (x2 - i)**2 + (y2 - j)**2 == 5:
                print("Yes")
                exit()

print("No")