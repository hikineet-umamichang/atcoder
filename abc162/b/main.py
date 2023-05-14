n = int(input())

a = [i if not(i % 3 == 0 or i % 5 == 0) else 0 for i in range(1, n + 1)]

print(sum(a))
