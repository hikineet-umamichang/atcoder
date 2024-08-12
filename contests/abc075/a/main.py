abc = list(map(int, input().split()))
abc.sort()

print(abc[0] if abc[1] == abc[2] else abc[2])
