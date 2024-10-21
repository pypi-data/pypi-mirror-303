# Daddy's boring math library

Python package of modules of a mathematical nature. The project
name was suggested by my then 13 year old daughter Mary.

* **Repositories**
  * [grscheller.boring-math][1] project on *PyPI*
  * [Source code][2] on *GitHub*
* **Detailed documentation**
  * [Detailed API documentation][3] on *GH-Pages*

## Overview

Here are the [modules](#library-modules) and
[executables](#cli-applications) which make up the
grscheller.boring-math PyPI project.

## Library Modules

### Integer Math Module

* Number Theory
  * Function **gcd**(int, int) -> int
    * greatest common divisor of two integers
    * always returns a non-negative number greater than 0
  * Function **lcm**(int, int) -> int
    * least common multiple of two integers
    * always returns a non-negative number greater than 0
  * Function **coprime**(int, int) -> tuple(int, int)
    * make 2 integers coprime by dividing out gcd
    * preserves signs of original numbers
  * Function **iSqrt**(int) -> int
    * integer square root
    * same as math.isqrt
  * Function **isSqr**(int) -> bool
    * returns true if integer argument is a perfect square
  * Function **primes**(start: int, end: int) -> Iterator[int]
    * now using *Wilson's Theorem*
  * Function **legendre_symbol**(a: int, p: int) -> int
    * where `p > 2` is a prime number
  * Function **jacobi_symbol**(a: int, n: int) -> int
    * where `n > 0`
* Combinatorics
  * Function **comb**(n: int, m: int) -> int
    * returns number of combinations of n items taken m at a time
    * pure integer implementation of math.comb

---

### Pythagorean Triple Module

* Pythagorean Triple Class
  * Method **Pythag3.triples**(a_start: int, a_max: int, max: Optional[int]) -> Iterator[int]
    * Returns an iterator of tuples of primitive *Pythagorean* triples
  * A Pythagorean triple is a tuple in positive integers (a, b, c)
    * such that `a² + b² = c²`
    * `a, b, c` represent integer sides of a right triangle
    * a *Pythagorean* triple is primitive if gcd of `a, b, c` is `1`
  * Iterator finds all primitive Pythagorean Triples
    * where `0 < a_start <= a < b < c <= max` where `a <= a_max`
    * if `max = 0` find all theoretically possible triples with `a <= a_max`

---

### Recursive Function Module

#### Ackermann's Function

* Function **ackermann_list**(m: int, n: int) -> int
  * an example of a total computable function that is not primitive recursive
  * becomes numerically intractable after `m=4`
  * see CLI section below for mathematical definition

#### Fibonacci Sequences

* Function **fibonacci**(f0: int=0, f1: int=1) -> Iterator[int]
  * returns a *Fibonacci* sequence iterator where
    * `f(0) = f0` and `f(1) = f1`
    * `f(n) = f(n-1) + f(n-2)`
  * yield defaults to `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`

* Function **rev_fibonacci**(f0: int=0, f1: int=1) -> Iterator[int]
  * returns a *Reverse Fibonacci* sequence iterator where
    * `rf(0) = f0` and `rf(1) = f1`
    * `rf(n) = rf(n-1) - rf(n-2)`
      * `rf(0) = fib(-1) = 1`
      * `rf(1) = fib(-2) = -1`
      * `rf(2) = fib(-3) = 2`
      * `rf(3) = fib(-4) = -3`
      * `rf(4) = fib(-5) = 5`
  * yield defaults to `1, -1, 2, -3, 5, -8, 13, -21, ...`

---

## CLI Applications

Implemented in an OS and package build tool independent way via the
project.scripts section of pyproject.toml.

### Ackermann's function CLI scripts

Ackermann, a student of Hilbert, discovered early examples of totally
computable functions that are not primitively recursive.

A [fairly standard][4] definition of the Ackermann function is
recursively defined for `m,n >= 0` by

```
   ackermann(0,n) = n+1
   ackermann(m,0) = ackermann(m-1,1)
   ackermann(m,n) = ackermann(m-1, ackermann(m, n-1))
```

#### CLI program **ackermann_list**

* Given two non-negative integers, evaluates Ackermann's function
* Implements the recursion via a Python array
* **Usage:** `ackerman_list m n`

---

### Pythagorean triple CLI script

Geometrically, a *Pythagorean* triangle is a right triangle with
positive integer sides.

#### CLI program **pythag3**

* Generates primitive Pythagorean triples
  * A primitive Pythagorean triple is a 3-tuple of integers `(a, b, c)` such that
    * `a³ + b³ = c³` where `a,b,c > 0` and `gcd(a,b,c) = 1`
  * The integers `a, b, c` represent the sides of a right triangle
* **Usage:** `pythag3 [m [n [max]]`
  * 3 args print all triples with `m <= a <= n` and `a < b < c <= max`
  * 2 args print all triples with `m <= a <= n`
  * 1 arg prints all triples with `a <= m`
  * 0 args print all triples with `3 <= a <= 100`

---

[1]: https://pypi.org/project/grscheller.boring-math/
[2]: https://github.com/grscheller/boring-math/
[3]: https://grscheller.github.io/boring-math/
[4]: https://mathworld.wolfram.com/AckermannFunction.html
