# ans = []
# i = 1


# def check(s):
#     for j in range(len(s) // 2):
#         if s[j] != s[-j - 1]:
#             return False
#     return True


# while i**3 < 10**18:
#     tmp = str(i**3)
#     if check(tmp):
#         ans.append(int(tmp))
#     i += 1
# ans.reverse()

# print(ans)

ans = [
    1331399339931331,
    1033394994933301,
    1000030000300001,
    1334996994331,
    1030607060301,
    1000300030001,
    10662526601,
    1003003001,
    1367631,
    1030301,
    1331,
    343,
    8,
    1,
]

n = int(input())
for i in range(len(ans)):
    if ans[i] <= n:
        print(ans[i])
        exit()
