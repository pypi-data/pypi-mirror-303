# CHANGELOG

PyPI grscheller.boring-math project.

#### Semantic versioning

* first digit
  * major event, epoch, or paradigm shift
* second digit
  * breaking API changes
  * major changes
* third digit
  * API additions
  * bug fixes
  * minor changes
  * significant documentation updates
* forth digit (development environment only)
  * commit count of "non-trivial" changes/regressions

## Releases and other important milestones

### Version 0.4.5 - PyPI release date 2024-10-18

* updated to use grscheller.fp v1.0.0
* pytest infrastructure improvements
* updated pyproject.toml
  * was lagging behind other grscheller namespace packages

### Version 0.4.4.10 - commit date 2024-09-30

* caught missing dependency in pyproject.toml
  * grscheller.fp >= 0.4.0, < 0.5"
  * version 0.4.0 is for the next fp PyPI release

### Version 0.4.4.5 - commit date 2024-09-08

* preparing to add more composite number tests
  * primality tests based on Wilson's theorem
    * becomes too slow when calculation starts using BigInts
  * added number theory symbols functions
    * implemented: `legendre_symbol(a, p)`
    * implemented: `jacobi_symbol(a, n)`

### Version 0.4.4.4 - commit date 2024-09-08

* re-implemented function primes
  * no longer using sieve of Eratosthenes algorithm
  * now using Wilson's theorem and incremental factorial generation

### Version 0.4.4 - PyPI release date 2024-09-01

* removed MathJax expressions
  * not worth the increased maintenance
  * can get almost the same results using `expresions` and unicode

### Version 0.4.3.1 - commit date 2024-08-17

* MathJax expressions used to render non-code mathematical expressions
  * pdoc accepts MathJax expressions with --math option
    * `$ pdoc --math -o . grscheller.boring_math`

### Version 0.4.3 - PyPI release date 2024-08-17

* updated to use grscheller.circular-array 3.4.1
  * this version of CA compares first with identity before trying equality
    * like Python builtins do
* now using pdoc instead of pdoc3 for documentation
* replaced github markdown with std markdown

### Version 0.4.0 - PyPI release date 2024-07-12

* updated to use grscheller.circular-array 3.3.1
* minimum Python version now 3.12
* target Python version now 3.13

### Version 0.3.1 - PyPI release date 2024-03-09

* reflecting grscheller.circular-array PyPI dependency change
  * dependencies = ["grscheller.circular-array >= 0.2.0, < 2.1"]

### Version 0.3.0 - PyPI release date 2024-03-02

* decided it a good time for a PyPI release
  * want to use some of the newer features in new endeavors
  * vastly improved documentation over last PyPI release

### Version 0.2.2.1 - commit date 2024-03-01

* greatly simplified README.md
  * due to having better control of pdoc documentation
    * allowing me to be a bit more DRY
    * now more likely to keep README.md up-to-date with detailed docs

### Version 0.2.2.0 - commit date 2024-02-28

* renamed integer_math.mkCoprime to integer_math.coprime
  * did it now before PyPI v0.3.0
* realized pdoc uses Markdown as its preferred markup language
  * some differences
    * incorporates some GitHub Markdown additions
    * will format google-style & numpydoc style comments
    * lists are one dimensional, not hierarchical

### Version 0.2.1.0 - commit date 2024-02-27

* Updated pythag3 cli script to provide more functionality
* docstring and README.md improvements

### Version 0.2.0.0 - commit date 2024-02-21

* All implementations going forward for integer_math module will use
  just integer based algorithms. I can't really compete with C based
  code from the Python standard library. The algorithms will then be
  of use if ported to a platform without floating point arithmetic.
* added two new functions to the integer_math module
  * iSqrt() finds the int square root of an int
    * does same thing as math.isqrt()
  * isSqr() return true if integer argument is a perfect square
* changed integer_math pythag3() function into a class method
  * pythag3() -> Pythag3.triples() 
  * preliminary steps
  * fould unrelated tweak to increase speed by 2X
  * removed use of floating point numbers

### Version 0.1.3 - PyPI release date 2024-02-20

* Forgot to update pyproject.toml dependencies
  * dependencies = ["grscheller.circular-array >= 0.1.1, < 1.1"]

### Version 0.1.2 - PyPI release date 2024-01-30

* now needs CircularArray v0.1.2
  * integer_math comb uses new foldL method of CircularArray
  * CircularArray was split out of grscheller.datastructures
* test suite written

### Version 0.1.1 - PyPI release date 2024-01-20

* fixed some negative value edge cases
  * lcm(0,0) now gives 0 instead of a divide by zero exception
    * some authors leave lcm(0, 0) as undefined
    * lcm(0, 0) = 0 does make sense
      * since a*0 = 0 for all a >= 0
      * 0 is the smallest non-negative integer a such that a*0 = 0
      * most math theorems remain true for this case
* README.md improvements

### Version 0.1.0 - PyPI release date 2024-01-17

* initial PyPI grscheller.boring-math release
* updated pyproject.toml to align with grscheller.datastructures

### Version 0.0.8 - commit date 2024-01-14

* changed project's name from boring_math to boring-math
* both GitHub repo and future PyPI repo
* more in alignment with what I see on PyPI
* project is grscheller.boring-math
* package is still grscheller.boring_math

### Version 0.0.8 - commit date 2024-01-14

* working on pyproject.toml infrastructure for PyPI releases
* will use Flit as the packaging/publishing tool
* replaced bin/ scripts with `boring_math.integer_math_cli` entry-points

### Version 0.0.4 - commit date 2024-01-10

* first coding changes in years!
* gh-pages configured

### Version 0.0.0.3 - commit date 2023-12-06

* added pyproject.toml

### Version 0.0.0.2 - commit date 2023-12-06

* got package working again
  * did not understand iterators that well when I first wrote this package
* replaced my `take` with `itertools.islice`
* generated docs from docstrings with pdoc3

### Version 0.0.0.1 - commit date 2023-12-06

* fixed Markdown issues with first commit
* Added .gitignore file to anticipate pytest & __pycache__ directories
 
### Version 0.0.0.0 - commit date 2023-12-06

* first commit of source code with with the old pipfile build
  infrastructure removed.
