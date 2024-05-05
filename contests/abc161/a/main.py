xyz = list(map(int, input().split()))
xyz.insert(0, xyz.pop())
print(*xyz)
