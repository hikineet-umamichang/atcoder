n = int(input())
w = set(list(input().split()))

z = set(["and", "not", "that", "the", "you"])

if len(w & z):
    print("Yes")
else:
    print("No")
