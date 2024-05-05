n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

body = 0
head = 0

for i in range(n):
    a, b = ab[i]
    body += a
    head = max(head, b - a)

print(body + head)
