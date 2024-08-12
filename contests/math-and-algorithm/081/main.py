n = int(input())

a = n // 10000
n -= a * 10000
b = n // 5000
n -= b * 5000
c = n // 1000

print(a + b + c)
