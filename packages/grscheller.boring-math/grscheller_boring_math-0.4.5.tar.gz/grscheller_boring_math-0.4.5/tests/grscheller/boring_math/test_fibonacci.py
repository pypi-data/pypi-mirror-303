# Copyright 2023-2024 Geoffrey R. Scheller
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

from grscheller.boring_math.recursive import fibonacci, rev_fibonacci

class Test_fibonacci:
    def test_fib(self) -> None:
        someFibs: list[int] = []
        fibs = fibonacci()
        fib = next(fibs)
        while(fib < 60):
            someFibs.append(fib)
            fib = next(fibs)
        assert someFibs == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        someFibs = []
        fib0 = 1
        fib1 = 1
        fibs = fibonacci(fib0, fib1)
        fib = next(fibs)
        while(fib < 90):
            someFibs.append(fib)
            fib = next(fibs)
        assert someFibs == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        someFibs = []
        fib0 = 1
        fib1 = 1
        fibs = rev_fibonacci(fib0, fib1)
        for n in range(10):
            fib = next(fibs)
            someFibs.append(fib)
        assert someFibs == [1, 0, 1, -1, 2, -3, 5, -8, 13, -21]

        someFibs = []
        fibs = rev_fibonacci()
        for n in range(10):
            fib = next(fibs)
            someFibs.append(fib)
        assert someFibs == [1, -1, 2, -3, 5, -8, 13, -21, 34, -55]

        someFibs = []
        fibs = rev_fibonacci(5, 3)
        for _ in range(12):
            fib = next(fibs)
            someFibs.append(fib)
        assert someFibs == [3, 2, 1, 1, 0, 1, -1, 2, -3, 5, -8, 13]

        someFibs = []
        fibs = fibonacci(-55, 34)
        fib = next(fibs)
        while(fib < 90):
            someFibs.append(fib)
            fib = next(fibs)
        assert someFibs == [-55, 34, -21, 13, -8, 5, -3,  2, -1,  1,  0,
                              1,  1,   2,  3,  5, 8, 13, 21, 34, 55, 89]

