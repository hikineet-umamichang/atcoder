from more_itertools import distinct_permutations

n, k = map(int, input().split())
s = list(input())


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


pa = set()
for x in distinct_permutations(s, k):
    if is_palindrome(x):
        pa.add("".join(x))

ans = 0
for x in distinct_permutations(s):
    tmp = "".join(list(x))

    flg = False
    for y in pa:
        if y in tmp:
            flg = True
            break
    if flg:
        continue

    ans += 1

print(ans)
