cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
a, b = map(int, input().split())
if cards.index(a) < cards.index(b):
    print("Bob")
elif cards.index(a) > cards.index(b):
    print("Alice")
else:
    print("Draw")
