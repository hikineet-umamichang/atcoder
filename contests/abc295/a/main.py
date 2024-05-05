_ = input()
a = ["and", "not", "that", "the", "you"]
print("Yes" if len(list(filter(lambda x: x in a, list(input().split())))) else "No")
