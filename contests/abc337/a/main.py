n = int(input())
x, y = map(sum, zip(*[list(map(int, input().split())) for _ in range(n)]))
if x > y:
    print("Takahashi")
elif x == y:
    print("Draw")
else:
    print("Aoki")
