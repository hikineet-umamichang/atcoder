import time


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


import math

N = int(input())
prime = prime_list(int(math.sqrt(N)))

ans = 0
for a in range(len(prime)):
    for b in range(a + 1, len(prime)):
        tmp = prime[a] * prime[a] * prime[b]
        if tmp > 10**12/12:
            break
        for c in range(b + 1, len(prime)):
            if tmp * prime[c] * prime[c] > N:
                break
            else:
                ans += 1
                # print(prime[a], prime[b], prime[c])
print(ans)
