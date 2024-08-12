q = int(input())
bag = [0] * (10**6 + 1)
ex = set()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        bag[query[1]] += 1
        ex.add(query[1])
    elif query[0] == 2:
        bag[query[1]] -= 1
        if bag[query[1]] == 0:
            ex.remove(query[1])
    else:
        print(len(ex))
