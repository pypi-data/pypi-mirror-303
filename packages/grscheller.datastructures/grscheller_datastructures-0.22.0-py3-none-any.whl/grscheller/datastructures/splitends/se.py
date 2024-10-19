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

"""### Stack type Data Structures

##### SplitEnd Stack types:

* **SE:** Singularly linked stack with shareable data nodes

"""

from __future__ import annotations

from typing import Callable, cast, Iterator, Never, Optional
from ..nodes import SL_Node
from grscheller.fp.err_handling import MB

__all__ = [ 'SE' ]

class SE[D]():
    """#### Class SE - SplitEnd

    LIFO stacks which can safely share immutable data between themselves.

    * each SplitEnd is a very simple stateful (mutable) LIFO stack
      * top of the stack is the "top"
    * data can be pushed and popped to the stack
    * different mutable split ends can safely share the same "tail"
    * each SplitEnd sees itself as a singularly linked list
    * bush-like datastructures can be formed using multiple SplitEnds
    * len() returns the number of elements on the SplitEnd stack
    * in boolean context, return true if split end is not empty

    """
    __slots__ = '_count', '_tip'

    def __init__(self, *ds: D) -> None:
        self._tip: MB[SL_Node[D]] = MB()
        self._count: int = 0
        self.push(*ds)

    def __iter__(self) -> Iterator[D]:
        if self._tip == MB():
            empty: tuple[D, ...] = ()
            return iter(empty)
        return iter(self._tip.get())

    def __reversed__(self) -> Iterator[D]:
        return reversed(list(self))

    def __bool__(self) -> bool:
        # Returns true if not a root node
        return bool(self._tip)

    def __len__(self) -> int:
        return self._count

    def __repr__(self) -> str:
        return 'SE(' + ', '.join(map(repr, reversed(self))) + ')'

    def __str__(self) -> str:
        return ('>< ' + ' -> '.join(map(str, self)) + ' ||')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False

        if self._count != other._count:
            return False
        if self._count == 0:
            return True

        left = self._tip.get()
        right = other._tip.get()
        for _ in range(self._count):
            if left is right:
                return True
            if not left.data_eq(right):
                return False
            if left:
                left = left._prev.get()
                right = right._prev.get()

        return True

    def push(self, *ds: D) -> None:
        """Push data onto the top of the SplitEnd."""
        for d in ds:
            node = SL_Node(d, self._tip)
            self._tip, self._count = MB(node), self._count+1

    def pop(self, default: Optional[D] = None) -> D|Never:
        """Pop data off of the top of the SplitEnd.

        * raises ValueError if
          * popping from an empty SplitEnd
          * and no default value was given

        """
        if self._count == 0:
            if default is None:
                raise ValueError('SE: Popping from an empty SplitEnd')
            else:
                return default

        data, self._tip, self._count = self._tip.get().pop2() + (self._count-1,)
        return data

    def peak(self, default: Optional[D] = None) -> D:
        """Return the data at the top of the SplitEnd.

        * does not consume the data
        * raises ValueError if peaking at an empty SplitEnd

        """
        if self._count == 0:
            if default is None:
                raise ValueError('SE: Popping from an empty SplitEnd')
            else:
                return default

        return self._tip.get().get_data()

    def copy(self) -> SE[D]:
        """Return a copy of the SplitEnd.

        * O(1) space & time complexity.
        * returns a new instance

        """
        se: SE[D] = SE()
        se._tip, se._count = self._tip, self._count
        return se

    def fold[T](self, f:Callable[[T, D], T], init: Optional[T] = None) -> T|Never:
        """Reduce with a function.

        * folds in natural LIFO Order

        """
        if self._tip != MB():
            return self._tip.get().fold(f, init)
        elif init is not None:
            return init
        else:
            msg = 'SE: Folding empty SplitEnd but no initial value supplied'
            raise ValueError(msg)
