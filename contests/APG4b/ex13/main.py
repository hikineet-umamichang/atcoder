n = int(input())
a = list(map(int, input().split()))
ave = sum(a) // n
print(*[abs(ave - x) for x in a], sep="\n")
