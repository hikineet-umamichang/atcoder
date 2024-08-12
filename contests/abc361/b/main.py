ax1, ay1, az1, ax2, ay2, az2 = map(int, input().split())
gx1, gy1, gz1, gx2, gy2, gz2 = map(int, input().split())


def check(l1, r1, l2, r2):
    if r1 <= l2 or r2 <= l1:
        return False
    else:
        return True


if (
    check(ax1, ax2, gx1, gx2)
    and check(ay1, ay2, gy1, gy2)
    and check(az1, az2, gz1, gz2)
):
    print("Yes")
else:
    print("No")
