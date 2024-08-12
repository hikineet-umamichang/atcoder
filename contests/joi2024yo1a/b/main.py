abc = [int(input()) for _ in range(3)]
abc.sort()
print(int(sum(abc) - abc[2] == abc[2]))
