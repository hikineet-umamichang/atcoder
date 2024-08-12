s = list(input())
if s[0] == "<" and s[-1] == ">" and "".join(s[1:-1]).count("=") == len(s) - 2:
    print("Yes")
else:
    print("No")
