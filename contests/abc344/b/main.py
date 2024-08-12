a = []
try:
    while True:
        a.append(input())
except:
    a.reverse()
    print(*a, sep="\n")
