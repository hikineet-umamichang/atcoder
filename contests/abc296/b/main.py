s = [input() for _ in range(8)]

h = "87654321"
w = "abcdefgh"

for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            print(w[j], h[i], sep="")
