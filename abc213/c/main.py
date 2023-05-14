h, w, n = map(int, input().split())

h_list = list()
w_list = list()
for _ in range(n):
    a, b = map(int, input().split())

    h_list.append(a)
    w_list.append(b)


def zaatsu(A: list) -> list:
    """
    作成: 2023/05/01
    参照: https://scrapbox.io/taq225algo/%E5%BA%A7%E6%A8%99%E5%9C%A7%E7%B8%AE
    """
    B = {a: i for i, a in enumerate(sorted(set(A)))}
    return [B[a] for a in A]


h_zaatsu = zaatsu(h_list)
w_zaatsu = zaatsu(w_list)

for i in range(n):
    print(h_zaatsu[i] + 1, w_zaatsu[i] + 1)
