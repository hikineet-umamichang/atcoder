n, t = map(int, input().split())
cards = []

cards.append(list(map(int, input().split())))
cards.append(list(map(int, input().split())))

if not t in cards[0]:
    t = cards[0][0]

mx = 0
player = 0
for i in range(n):
    if cards[0][i] == t and cards[1][i] > mx:
        mx = cards[1][i]
        player = i
print(player + 1)
