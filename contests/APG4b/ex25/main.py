n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
com = input()

cm = com[:3]

if cm == "int":
    ans = a & b
elif cm == "uni":
    ans = a | b
elif cm == "sym":
    ans = a ^ b
elif cm == "inc":
    ans = list(map(lambda x: (x + 1) % 50, a))
elif cm == "dec":
    ans = list(map(lambda x: (x - 1) % 50, a))
else:
    ans = a - {int(com.split()[1])}

ans = sorted(list(ans))
print(*ans)
