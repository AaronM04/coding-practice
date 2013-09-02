#!/usr/bin/python

## globals
primes_set = set()
primes_list = []

def is_prime(n):
    limit = int(round(sqrt(n)))
    i = 2
    while True:
        if i > limit:
            return True
        if n % i == 0:
            return False


def find_prime_permutations(n):
    "find the prime permutations including n"
    global primes_set
    assert n >= 1000 and n <= 9999
    perm_set = set()
    s = str(n)
    for i in xrange(4):
        for j in xrange(4):
            if j == i:
                continue
            for k in xrange(4):
                if k == i or k == j:
                    continue
                for l in xrange(4):
                    if l == i or l == j or l == k:
                        continue
                    s2 = s[i] + s[j] + s[k] + s[l]
                    n2 = int(s2)
                    if n2 in primes_set:
                        perm_set.add(n2)
    return perm_set


def find_arith_seq(_set):
    l = sorted(list(_set))
    if len(l) < 3:
        return None
    for i in xrange(1, len(l)-1):    # not either end
        for j in xrange(0, i):
            n = l[i]*2 - l[j]
            if n in _set and n != l[i] and n != l[j]:
                return (l[j], l[i], n)
    return None


if __name__ == '__main__':
    if len(primes_set) == 0:   # if not initialized
        for i in xrange(1001, 9999+1):
            if is_prime(i):
                primes_set.add(i)
                primes_list.append(i)

    solutions = set()

    for p in primes_list:
        prime_perm_set = find_prime_permutations(p)
        result = find_arith_seq(prime_perm_set)
        if result is not None:
            solutions.add(result)

    print repr(solutions)
