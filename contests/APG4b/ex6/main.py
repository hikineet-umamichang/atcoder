a = list(input().split())

if a[1] in ["+", "-", "*", "/"]:
    try:
        print(int(eval("".join(a))))
    except:
        print("error")
else:
    print("error")
