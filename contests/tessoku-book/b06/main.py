from itertools import accumulate

n = int(input())
a = list(map(int, input().replace("0", "-1").split()))
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

b = list(accumulate([0] + a))
for l, r in lr:
    vs = b[r] - b[l - 1]
    if vs == 0:
        print("draw")
    elif vs > 0:
        print("win")
    elif vs < 0:
        print("lose")
