y = int(input())

if y % 4:
    print(365)
elif y % 100:
    print(366)
elif y % 400:
    print(365)
else:
    print(366)
