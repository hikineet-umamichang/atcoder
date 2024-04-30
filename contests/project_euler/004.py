n = int(input())

max_num = int("9" * n)
tmp1 = max_num // 11 * 11
ans = []

while tmp1 >= 10 ** (n - 1):
    tmp2 = max_num
    while tmp2 >= 10 ** (n - 1):
        product = tmp1 * tmp2
        product_head = str(product)[:n]
        product_tail = str(product)[n:]
        # print(tmp1, tmp2)
        # print(product, product_head, product_tail)

        if product_head == product_tail[::-1]:
            ans.append(product)
            break

        if product <= 10 ** (n * 2 - 1):
            break
        tmp2 -= 1
    tmp1 -= 11

print(max(ans))
