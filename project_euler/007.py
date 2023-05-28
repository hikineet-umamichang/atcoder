n = int(input())


def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(
            3 * i + 1 | 1
            for i in range(1, (n + 1) // 3 + (n % 6 == 1))
            if not (sieve[i >> 3] >> (i & 7)) & 1
        )
    return res


def is_ok(arg):
    if n >= len(prime_list(arg)):
        return True
    else:
        return False


def exponential_search():
    """
    条件を満たすまでngを倍にし続ける。
    """
    ok = 0
    ng = 1
    while is_ok(ng):
        ng *= 2

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(prime_list(exponential_search())[-1])
