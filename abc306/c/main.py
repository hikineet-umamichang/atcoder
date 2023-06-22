n = int(input())
a = list(map(int, input().split()))

b = [[0, 0, i] for i in range(n)]

for i in range(3 * n):
    b[a[i] - 1][0] += 1
    if b[a[i] - 1][0] == 2:
        b[a[i] - 1][1] = i
import operator

b.sort(key=operator.itemgetter(1))

for x in b:
    print(x[2]+1,end=" ")
print()