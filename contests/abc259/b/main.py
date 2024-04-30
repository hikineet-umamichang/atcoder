a, b, d = map(int, input().split())

import math

c = math.radians(d)
print(
    a * math.cos(c) - b * math.sin(c),
    a * math.sin(c) + b * math.cos(c),
)
