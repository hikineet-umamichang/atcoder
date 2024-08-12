n = int(input())
b = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    11,
    22,
    33,
    44,
    55,
    66,
    77,
    88,
    99,
]
if n <= 19:
    print(b[n - 1])
    exit()

tmp = str(n - 10)
print(tmp)
