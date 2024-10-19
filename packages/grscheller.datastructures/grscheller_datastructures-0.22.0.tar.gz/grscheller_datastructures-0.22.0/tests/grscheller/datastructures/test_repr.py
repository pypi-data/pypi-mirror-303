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
from grscheller.datastructures.queues import DoubleQueue
from grscheller.datastructures.queues import FIFOQueue
from grscheller.datastructures.queues import LIFOQueue
from grscheller.datastructures.tuples import FTuple
from grscheller.fp.err_handling import MB, XOR

class Test_repr:
    def test_DoubleQueue(self) -> None:
        dq0: DoubleQueue[object] = DoubleQueue()
        assert repr(dq0) == 'DoubleQueue()'
        dq1 = eval(repr(dq0))
        assert dq1 == dq0
        assert dq1 is not dq0

        dq0.pushR(1)
        dq0.pushL('foo')
        assert repr(dq0) == "DoubleQueue('foo', 1)"
        dq1 = eval(repr(dq0))
        assert dq1 == dq0
        assert dq1 is not dq0

        assert dq0.popL().get('bar') == 'foo'
        dq0.pushR(2)
        dq0.pushR(3)
        dq0.pushR(4)
        dq0.pushR(5)
        assert dq0.popL() == MB(1)
        dq0.pushL(42)
        dq0.popR()
        assert repr(dq0) == 'DoubleQueue(42, 2, 3, 4)'
        dq1 = eval(repr(dq0))
        assert dq1 == dq0
        assert dq1 is not dq0

    def test_FIFOQueue(self) -> None:
        sq1: FIFOQueue[object] = FIFOQueue()
        assert repr(sq1) == 'FIFOQueue()'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        sq1.push(1)
        sq1.push('foo')
        assert repr(sq1) == "FIFOQueue(1, 'foo')"
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        assert sq1.pop() == MB(1)
        sq1.push(2)
        sq1.push(3)
        sq1.push(4)
        sq1.push(5)
        assert sq1.pop() == MB('foo')
        sq1.push(42)
        sq1.pop()
        assert repr(sq1) == 'FIFOQueue(3, 4, 5, 42)'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

    def test_LIFOQueue(self) -> None:
        sq1: LIFOQueue[object] = LIFOQueue()
        assert repr(sq1) == 'LIFOQueue()'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        sq1.push(1)
        sq1.push('foo')
        assert repr(sq1) == "LIFOQueue(1, 'foo')"
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        assert sq1.pop() == MB('foo')
        sq1.push(2, 3)
        sq1.push(4)
        sq1.push(5)
        assert sq1.pop() == MB(5)
        sq1.push(42)
        assert repr(sq1) == 'LIFOQueue(1, 2, 3, 4, 42)'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

    def test_ftuple(self) -> None:
        ft1:FTuple[object] = FTuple()
        assert repr(ft1) == 'FTuple()'
        ft2 = eval(repr(ft1))
        assert ft2 == ft1
        assert ft2 is not ft1

        ft1 = FTuple(42, 'foo', [10, 22])
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22])"
        ft2 = eval(repr(ft1))
        assert ft2 == ft1
        assert ft2 is not ft1

        list_ref = ft1[2]
        if type(list_ref) == list:
            list_ref.append(42)
        else:
            assert False
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22, 42])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22])"
        popped = ft1[2].pop()                                     # type: ignore
        assert popped == 42
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22])"

        # beware immutable collections of mutable objects
        ft1 = FTuple(42, 'foo', [10, 22])
        ft2 = ft1.copy()
        ft1[2].append(42)                                         # type: ignore
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22, 42])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22, 42])"
        popped = ft2[2].pop()
        assert popped == 42
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22])"

    def test_SplitEnd_procedural_methods(self) -> None:
        s1: SE[object] = SE('foobar')
        assert repr(s1) == "SE('foobar')"
        s2 = eval(repr(s1))
        assert s2 == s1
        assert s2 is not s1

        s1.push(1)
        s1.push('foo')
        assert repr(s1) == "SE('foobar', 1, 'foo')"
        s2 = eval(repr(s1))
        assert s2 == s1
        assert s2 is not s1

        assert s1.pop() == 'foo'
        assert s1.pop() == 1
        assert s1.pop() == 'foobar'
        s1.push(2)
        s1.push(3)
        s1.push(4)
        s1.push(5)
        assert s1.pop() == 5
        s1.push(42)
        assert repr(s1) == 'SE(2, 3, 4, 42)'
        s2 = s1.copy()
        assert s2 == s1
        assert s2 is not s1

#    def test_SplitEnd_functional_methods(self) -> None:
#        se_roots: SplitEndRoots[int] = SplitEndRoots()
#        fs1: SplitEnd = SplitEnd(se_roots, 1, 2, 3)
#    #   assert repr(fs1) == 'SplitEnd()'
#    #   fs2 = eval(repr(fs1))
#        fs2 = fs1.copy()
#        assert fs2 == fs1
#        assert fs2 is not fs1
#
#        fs1 = fs1.cons(42)
#        fs1 = fs1.cons(-1)
#    #   assert repr(fs1) == "SplitEnd(1, 'foo')"
#    #   fs2 = eval(repr(fs1))
#    #   assert fs2 == fs1
#    #   assert fs2 is not fs1
#
#        assert fs1.head() == -1
#        assert fs2.head() == 3
#        fs3 = fs2.tail()
#        if fs3 is None:
#            assert False
#        fs3 = fs3.cons(-3).cons(4).cons(5)
#        assert fs3.head() == 5
#        if (fs4 := fs3.tail()):
#            fs4 = fs4.cons(42)
#        else:
#            assert False
#        assert fs4 == SplitEnd(se_roots, 1, 2, -3, 4, 42)
#    #   assert repr(fs4) == 'SplitEnd(1, 2, -3, 4, 42)'
#    #   fs5 = eval(repr(fs4))
#    #   assert fs5 == fs4
#    #   assert fs5 is not fs4

class Test_repr_mix:
    def test_mix1(self) -> None:
        thing1: XOR[object, str] = \
            XOR(
                FIFOQueue(
                    FTuple(
                        42,
                        MB(42),
                        XOR(right = 'nobody home')
                    ),
                    SE[tuple[int, ...]](
                        (1,),
                        (),
                        (42, 100)
                    ),
                    LIFOQueue(
                        'foo',
                        'bar'
                    )
                ),
                'Potential Right'
            )

        repr_str = "XOR(FIFOQueue(FTuple(42, MB(42), XOR(right='nobody home')), SE((1,), (), (42, 100)), LIFOQueue('foo', 'bar')), 'Potential Right')"
        assert repr(thing1) == repr_str

        thing2 = eval(repr(thing1))
        thing3 = eval(repr_str)
        assert thing2 == thing1 == thing3
        assert thing2 is not thing1

        repr_thing1 = repr(thing1)
        repr_thing2 = repr(thing2)
        repr_thing3 = repr(thing3)
        assert repr_thing2 == repr_thing1 == repr_thing3 == repr_str
