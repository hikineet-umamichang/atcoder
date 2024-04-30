n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = 0

while k > 0:
    right += 1
    if right == n or a[right] < a[left]:
        a[left:right] = reversed(a[left:right])
        k -= 1
        left = right

print(*a)
