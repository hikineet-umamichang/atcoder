import inflect

n = int(input())
p = inflect.engine()

ans = ""
for i in range(1, n + 1):
    ans += p.number_to_words(i)
ans = ans.replace(" ", "")
ans = ans.replace("-", "")

print(len(ans))
# print(ans)
