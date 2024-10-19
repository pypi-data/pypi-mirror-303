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

"""
### Nodes for Graphs

Node classes used with graph-like data structures. API designed to be used by
other data structures which contain these data structures.

"""
from __future__ import annotations
from typing import Callable, cast, Iterator, Optional
from grscheller.fp.err_handling import MB

__all__ = ['SL_Node', 'DL_Node', 'Tree_Node']

class SL_Node[D]():
    """
    Data node for rearward Pointing (tip-to-root) singularly linked graphs.

    * for mutable and immutable linear data structures
    * designed so multiple instances can safely share the same data
    * this type of node always contain data and optionally a previous Node
    * nodes point towards a unique "root node" with no predecessor
      * in a Boolean context return false only if only at a root
      * multiple root nodes can exist
      * empty data structures can be "re-rooted"
    * two nodes compare as equal if
      * both their previous Nodes are the same
      * their data compares as equal
    * more than one node can point to the same node forming bush like graphs

    """
    __slots__ = '_data', '_prev'

    def __init__(self, data: D, prev: MB[SL_Node[D]]) -> None:
        self._data = data
        self._prev = prev

    def __iter__(self) -> Iterator[D]:
        node = self
        while node:
            yield node._data
            node = node._prev.get()
        yield node._data

    def __bool__(self) -> bool:
        return self._prev != MB()

    def data_eq(self, other: SL_Node[D]) -> bool:
        if self._data is other._data:
            return True
        elif self._data == other._data:
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False

        if self._prev is not other._prev:
            return False
        else:
            return self.data_eq(other)

    def get_data(self) -> D:
        return self._data

    def fold[T](self,  f: Callable[[T, D], T], init: Optional[T] = None) -> T:
        """Reduce data across linked nodes

        * with a function and an optional starting value
        * reduces in natural LIFO order
          * from self to the root

        """
        if init is None:
            acc: T = cast(T, self._data)
            node = self._prev.get()
        else:
            acc = init
            node = self

        while node:
            acc = f(acc, node._data)
            node = node._prev.get()
        acc = f(acc, node._data)
        return acc

    def pop2(self) -> tuple[D, MB[SL_Node[D]]]:
        """Return the *head* and, if it exists, the top node of the *tail*."""
        return self._data, self._prev

    def push_data(self, data: D) -> SL_Node[D]:
        """Push data onto the stack and return a new node containing the data"""
        return SL_Node(data, MB(self))

class DL_Node[D]():
    """
    #### Doubly Linked Node

    Doubly linked nodes for graph-like data structures.

    * this type of node always contain data, even if that data is None
      * in a Boolean context return true if both left and right nodes exist
    * not __iter__ method provided, too application specific
    * doubly link lists possible
    * circular graphs are possible
    * simple recursive binary trees possible

    """
    __slots__ = '_left', '_data', '_right'

    def __init__(self, left: MB[DL_Node[D]], data: D, right: MB[DL_Node[D]]):
        self._left = left
        self._data = data
        self._right = right

    def __bool__(self) -> bool:
        if self._left == MB() or self._right == MB():
            return False
        return True

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False

        if self._left is not other._left:
            return False
        if self._right is not other._right:
            return False
        if self._data is other._data:
            return True
        elif self._data == other._data:
            return True

        return False

    def has_left(self) -> bool:
        return self._left != MB()

    def has_right(self) -> bool:
        return self._right != MB()

class Tree_Node[D, M]():
    """Binary Tree Node with metadata.

    Nodes useful for binary trees

    * this type of node always contain data, even if that data is None
    * in a Boolean context return true if not at the top of the tree
    * potential uses of metadata can be for re-balancing or repeat counts
    """
    __slots__ = '_data', '_left', '_right', '_up'

    def __init__(self, data: D,
                 up: MB[Tree_Node[D,M]],
                 left: MB[Tree_Node[D,M]],
                 right: MB[Tree_Node[D,M]],
                 meta: tuple[M, ...] = ()):
        self._data = data
        self._up = up
        self._left = left
        self._right = right

    def __bool__(self) -> bool:
        if self._up == MB():
            return False
        else:
            return True

    def is_top(self) -> bool:
        return self._up == MB()
