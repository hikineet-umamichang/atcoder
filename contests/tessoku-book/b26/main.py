n = int(input())

prime_table = [True] * (n + 1)
prime_table[0], prime_table[1] = False, False

for i in range(2, n + 1):
    if prime_table[i] == False:
        continue

    j = i + i
    while j <= n:
        prime_table[j] = False
        j += i

for idx, x in enumerate(prime_table):
    if x:
        print(idx)
