n = int(input())
a = int(input())
for i in range(n):
    op, b = input().split()
    b = int(b)
    if op == "+":
        a += b
    elif op == "-":
        a -= b
    elif op == "*":
        a *= b
    elif op == "/" and b == 0:
        exit(print("error"))
    else:
        a = int(a / b)
    print(f"{i+1}:{a}")
