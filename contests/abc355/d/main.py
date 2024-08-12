from atcoder.segtree import SegTree

n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
lr.sort()
l, r = zip(*lr)

G = SegTree(max, 10**6, l)

ans = 0
