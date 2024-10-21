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

from __future__ import annotations
from grscheller.datastructures.splitends.se import SE
from grscheller.fp.iterables import concat, FM

class Test_SplitEnds:
    def test_mutate_returns_none(self) -> None:
        ps = SE[int](41)
        ret = ps.push(1,2,3) # type: ignore # my[py] warning what is being tested
        assert ret is None

    def test_pushThenPop(self) -> None:
        s1: SE[int] = SE(42)
        pushed = 21
        s1.push(pushed)
        popped = s1.pop()
        assert pushed == popped == 21

    def test_popFromEmptySplitEnd(self) -> None:
        s1: SE[int] = SE(-42)
        popped = s1.pop()
        assert popped == -42
        try:
            popped = s1.pop()
            assert False
        except ValueError as ve:
            assert True
        else:
            assert False

        s2 = SE(1, 2, 3, 42)
        nums: set[int] = set()
        while s2:
            nums.add(s2.pop())         # pop until empty
        assert nums == {2, 1, 42, 3}   # anyone home?
        assert not s2
        s2.push(42)
        try:
            assert s2.peak() == 40+2
            assert s2.pop() == 42
            assert s2.peak() == 1
            assert False
        except ValueError as ve:
            assert True
        else:
            assert False

    def test_SplitEndPushPop(self) -> None:
        s0: SE[int] = SE()
        s1 = SE(101)
        s2 = SE(*range(0,2000))

        assert len(s0) == 0
        assert len(s1) == 1
        assert len(s2) == 2000
        s0.push(21)
        s1.push(42)
        assert s2.pop() == 1999
        assert s2.pop() == 1998
        assert len(s0) == 1
        assert len(s1) == 2
        assert len(s2) == 1998
        assert s1.pop() == 42
        assert s1.pop() == 101
        s1.push(12, 13, 14)
        assert len(s1) == 3
        assert s1.pop() == 14
        assert s1.pop() == 13
        assert len(s1) == 1
        assert s1.pop() == 12
        assert len(s1) == 0

#    def test_consHeadTail(self) -> None:
#        s1: SE[int] = SE(roots_int, 1)
#        s2 = s1.cons(100)
#        head = s2.head()
#        assert head == 100
#        head = s1.head()
#        assert head == 1
#        s3 = s2.cons(1).cons(2).cons(3)
#        s4 = s3.tail()
#        assert s4 == SE(roots_int, 1, 100, 1, 2)
#        assert s1 == SE(roots_int, 1)
#        s5 = s1.cons(42).cons(0)
#        assert s5 == SE(roots_int, 1, 42, 0)
#        assert s5.tail() == SE(roots_int, 1, 42)

    def test_SplitEnd_len(self) -> None:
        s1: SE[int|None] = SE(None)
        s2: SE[int|None] = SE(None, 42)
        s2001: SE[int|None] = SE(None, *range(1,2001))

        assert len(s1) == 1
        if s2001:
            assert len(s2001) == 2001
        else:
            assert False
        if s1:
            assert True
        s3 = s1.copy()
        assert len(s1) == 1
        assert s1.pop() == None
        assert len(s1) == 0
        assert len(s3) == 1
        assert s3.pop() == None
        assert len(s3) == 0
        s4: SE[int|None]|None = s3 if s3 else None
        assert s4 is None
        assert s2001.pop() == 2000
        assert s2001.pop() == 1999
        assert len(s1) == 0
        assert len(s2) == 2
        assert len(s2001) == 1999
        assert s2001.pop() == 1998
        assert len(s2001) == 1998
        assert s2001.peak() == 1997

#   def test_tailcons(self) -> None:
#       s1: SE[str] = SE(roots_str, "fum")
#       s1 = s1.cons("fo").cons("fi").cons("fe")
#       assert type(s1) == SE
#       s2 = s1.tail()
#       if s2 is None:
#           assert False
#       s3 = s2.cons("fe")
#       assert s3 == s1
#       while s1:
#           s1 = s1.tail()
#       assert s1.head() == "fum"
#   #   assert s1.tail().cons('foo') is SE(roots_str, "fum").cons('foo') # TODO: Drop mutating methods and make this true???
#       assert s1.tail() == SE(roots_str, "fum")

    def test_stackIter(self) -> None:
        giantSplitEnd: SE[str] = SE(*[' Fum', ' Fo', ' Fi', 'Fe'])
        giantTalk = giantSplitEnd.pop()
        assert giantTalk == "Fe"
        for giantWord in giantSplitEnd:
            giantTalk += giantWord
        assert len(giantSplitEnd) == 3
        assert giantTalk == 'Fe Fi Fo Fum'

        gSE = giantSplitEnd.copy()
        for ff in gSE:
            assert ff[0] in {' ', 'F'}

    def test_equality(self) -> None:
        s1 = SE(*range(3))
        s2 = s1.copy()
        s2.push(42)
        assert s1 is not s2
        assert s1 != s2
        assert s2.pop() == 42
        assert s1 == s2
        assert s2 is not s1
        assert s2.peak() == 2

        s3 = SE(*range(1, 10001))
        s4 = s3.copy()
        assert s3 is not s4
        assert s3 == s4

        s3.push(s4.pop())
        assert s3.pop() == 10000
        assert s3.pop() == 10000
        assert s3 == s4
        assert s3 is not s4

        s5 = SE(1,2,3,4)
        s6 = SE(1,2,3,42)
        assert s5 != s6
        for ii in range(10):
            s5.push(ii)
            s6.push(ii)
        assert s5 != s6

        ducks: tuple[str, ...] = ("Huey", "Dewey")
        s7 = SE((), ducks)
        s8 = SE((), ducks)
        s9 = s8.copy()
        s9.push(("Huey", "Dewey", "Louie"))
        assert s7 == s8
        assert s7 != s9
        assert s7.peak() == s8.peak()
        assert s7.peak() != s9.peak()
        ducks = ducks + ("Louie",)
        s7.push(ducks)
        assert s7 != s8
        assert s7 == s9
        stouges = ('Moe', 'Larry', 'Curlie')
        s7.push(stouges)
        assert s7 != s9
        s9.push(('Moe', 'Larry', 'Curlie'))
        assert s7 == s9
        assert s7 is not s9
        assert s7.peak() == s9.peak()

    def test_storeNones(self) -> None:
        s0: SE[int|None] = SE(100)
        s0.push(None)
        s0.push(42)
        s0.push(None)
        s0.push(42)
        s0.push(None)
        assert len(s0) == 6
        while s0:
            assert s0
            s0.pop()
        assert not s0

        s1: SE[int|None] = SE(None)
        s1.push(24)
        s2 = s1.copy()
        s2.push(42)
        s1.push(42)
        assert s1 == s2
        assert len(s1) == len(s2) == 3
        s3 = s2.copy()
        s3.push(None)
        assert s3.peak() is None
        assert s3
        assert len(s3) == 4
        assert s3.pop() == None
        assert s3.pop() == 42
        assert s3.pop() == 24
        assert s3.pop() is None
        assert len(s3) == 0
        s3.push(None)
        s3.push(42)
        s4 = SE(None, 42)
        assert s3 == s4

    def test_reversing(self) -> None:
        s1 = SE('a', 'b', 'c', 'd')
        s2: SE[str] = SE('d', 'c', 'b', 'a')
        assert s1 != s2
        assert s2 == SE(*iter(s1))
        s0: SE[str] = SE('z')
        assert s0 == SE(*iter(s0))
        s3: SE[int] = SE(*concat(iter(range(1, 100)), iter(range(98, 0, -1))))
        s4 = SE(*s3)
        assert s3 == s4
        assert s3 is not s4

    def test_reversed(self) -> None:
        lf = [1.0, 2.0, 3.0, 4.0]
        lr = [4.0, 3.0, 2.0, 1.0]
        s1: SE[float] = SE(*lr)
        l_s1 = list(s1)
        l_r_s1 = list(reversed(s1))
        assert lf == l_s1
        assert lr == l_r_s1
        s2 = SE(*lf)
        for x in s2:
            assert x == lf.pop()
        assert len(lf) == 0       # test iteration gets all values
        assert len(s2) == 4       # s2 not consumed
