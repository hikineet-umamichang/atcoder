a, b, c = map(int, input().split())

if pow(a, c % 102) > pow(b, c % 102):
    print(">")
elif pow(a, c % 102) < pow(b, c % 102):
    print("<")
else:
    print("=")
