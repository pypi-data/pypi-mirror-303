# Copyright 2016-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
### Functions of a pure math integer nature

"""
from __future__ import annotations

from typing import Iterator, Optional
from grscheller.circular_array.ca import CA
from grscheller.fp.iterables import foldL

__all__ = ['gcd', 'lcm',
           'coprime', 'iSqrt', 'isSqr',
           'legendre_symbol', 'jacobi_symbol',
           'primes', 'primes_capped', 'primes_wilson',
           'comb']

# Number Theory mathematical Functions.

def gcd(m: int, n: int) -> int:
    """
    Uses Euclidean algorithm to compute the gcd of two integers.

    * takes two integers, returns gcd > 0
    * note that mathematically the gcd of 0 and 0 does not exist
    * taking `gcd(0, 0) = 1` is a better choice than `math.gcd(0, 0) = 0`
      * eliminates lcm & coprime having to edge case test
      * also `gcd(0, 0)` returning 1 instead of 0 more mathematically justified

    """
    if 0 == m == n:
        return 1
    m, n = abs(m), abs(n)
    while n > 0:
        m, n = n, m % n
    return m

def lcm(m: int, n: int) -> int:
    """
    Finds the least common multiple (lcm) of two integers.

    * takes two integers `m` and `n`
    * returns `lcm(m, n) > 0`

    """
    m //= gcd(m, n)
    return abs(m*n)

def coprime(m: int, n: int) -> tuple[int, int]:
    """
    Makes 2 integers coprime by dividing out their common factors.

    * returns `(0, 0)` when `n = m = 0`
    * returned coprimed values retain their original signs

    """
    common = gcd(m, n)
    return m//common, n//common

def iSqrt(n: int) -> int:
    """
    Integer square root of a non-negative integer.

    * return the unique `m` such that `m*m <= n < (m+1)*(m+1)`
    * raises: ValueError if `n < 0`

    """
    if n < 0:
        msg = 'iSqrt(n): n must be non-negative'
        raise ValueError(msg)
    high = n
    low = 1
    while high > low:
        high = (high + low) // 2
        low = n // high
    return high

def isSqr(n: int) -> bool:
    """
    Returns true if integer argument is a perfect square

    """
    return False if n < 0 else n == iSqrt(n)**2

def legendre_symbol(a: int, p: int) -> int:
    """
    Calculate the Legendre Symbol `(a/p)`

    Where `(a/p)` is only defined for p an odd prime,
    also `(a/p)` is periodic in `a` with period `p`.

    See https://en.wikipedia.org/wiki/Legendre_symbol
    """
    assert p > 2  # and prime!
    a = a % p

    if a == 0:
        return 0
    else:
        for x in range(1, p):
            if x*x % p == a:
                return 1
        return -1

def jacobi_symbol(a: int, n: int) -> int:
    """
    Calculate the Jacobi Symbol (a/n) 

    See https://en.wikipedia.org/wiki/Jacobi_symbol

    """
    assert n > 0 and n % 2 == 1

    a = a % n
    t = 1
    while a != 0:
        while a % 2 == 0:
            a = a // 2
            r = n % 8
            if r == 3 or r == 5:
               t = -t
        n, a = a, n
        if n % 4 == 3 and a % 4 == 3:
            t = -t
        a = a % n

    if n == 1:
        return t
    else:
        return 0

def primes_wilson(start: int=2) -> Iterator[int]:
    """
    Return a prime number iterator using Wilson's Theorem.

    Iterator starts at `start` and is infinite.

    ###### Wilson's Theorem

    `∀(n>1)`, `n` is prime if and only if `(n-1)! % n = -1`

    """
    if start < 2:
        n = 2
        fact = 1
    else:
        n = start
        fact = CA(*range(2, n)).foldL(lambda j, k: j*k, initial=1)
    while(True):
        if fact % n == n-1:
            yield n
        fact *= n
        n += 1

def primes_capped(start: int, end: int) -> Iterator[int]:
    """
    Returns all primes `p` where `start <= p <= end`

    """
    for ii in primes_wilson(start):
        if ii < end:
            yield ii
        elif ii == end:
            yield ii
            break
        else:
            break

def primes(start: int=2, end: Optional[int]=None) -> Iterator[int]:
    """
    Returns all primes `p` where `start <= p <= end`

    * If end is not given, returned iterator is infinite.

    """
    if end is None:
        return primes_wilson(start)
    else:
        return primes_capped(start, end)

_test_factors = 2*3*5*7*11*13

def is_prime(candidate: int) -> bool:
    """
    Returns true if argument is a prime number, uses Wilson's Theorem.

    """
    n = abs(candidate)
    if n < 2:
        return False
    if n < _test_factors or gcd(n, _test_factors) == 1:
        return foldL(range(2, n), lambda j, k: j*k, 1).get() % n == n-1
    else:
        return False

# Combinatorics

def comb(n: int, m: int, targetTop: int=700, targetBot: int=5) -> int:
    """
    #### Implements `C(n,m)`

    * the number of `n` items taken `m` at a time.
    * geared to works efficiently for Python's arbitrary length integers
    * default parameters geared to large values of `n` and `m`
    * the defaults work reasonably well for smaller (human size) values
    * for inner loops with smaller values, use `targetTop = targetBot = 1`
    * or just use `math.comb(n, m)` instead
    * raises ValueError if `n < 0` or `m < 0`

    """
    # edge cases
    if n < 0 or m < 0:
        raise ValueError('for C(n, m) n and m must be a non-negative ints')
    if n == m or m == 0:
        return 1
    elif m > n:
        return 0

    # using C(n, m) = C(n, n-m) to reduce number of factors in calculation
    if m > (n // 2):
        m = n - m

    # Prepare data structures
    tops: CA[int] = CA(*range(n - m + 1, n + 1))
    bots: CA[int] = CA(*range(1, m+1))

    # Compacting data structures makes algorithm work better for larger values
    size = len(tops)
    while size > targetTop:
        size -= 1
        top, bot = coprime(tops.popL() * tops.popL(), bots.popL() * bots.popL())
        tops.pushR(top)
        bots.pushR(bot)

    while size > targetBot:
        size -= 1
        bots.pushR(bots.popL() * bots.popL())

    # Cancel all factors in denominator before multiplying the remaining factors
    # in the numerator.
    for bot in bots:
        for ii in range(len(tops)):
            top, bot = coprime(tops.popL(), bot)
            if top > 1:
                tops.pushR(top)
            if bot == 1:
                break

    ans = tops.foldL(lambda x, y: x * y, initial=1)
    assert ans is not None
    return ans
