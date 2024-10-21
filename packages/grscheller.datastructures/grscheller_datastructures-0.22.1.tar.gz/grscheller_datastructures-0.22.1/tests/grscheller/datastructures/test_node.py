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
from typing import cast
from grscheller.datastructures.nodes import SL_Node as SL
from grscheller.datastructures.nodes import DL_Node as DL
from grscheller.fp.err_handling import MB

class Test_SL_Node:
    def test_bool(self) -> None:
        n1 = SL(1, MB())
        n2 = SL(2, MB(n1))
        assert not n1
        assert n2

    def test_linking(self) -> None:
        n1 = SL(1, MB())
        n2 = SL(2, MB(n1))
        n3 = SL(3, MB(n2))
        assert n3._data == 3
        assert n3._prev != MB()
        assert n3._prev.get()._data == 2
        assert n2._prev is not None
        assert n2._data == n3._prev.get()._data == 2
        assert n1._data == n2._prev.get()._data == n3._prev.get()._prev.get()._data == 1
        assert n3._prev != MB()
        assert n3._prev.get()._prev.get() != MB()
        assert n3._prev.get()._prev.get()._prev == MB()
        assert n3._prev.get()._prev == n2._prev

# class Test_DL_TREE_Node:
#     def test_bool(self) -> None:
#         nul: MB[DL[str]] = MB()
#         tn0: DL[str] = DL(MB(), 'spam', MB())
#         tn1: DL[str] = DL(MB(), 'spam', MB(tn0))
#         tn2: DL[str] = DL(MB(), 'spam', MB(tn1))
#         tn3: DL[str] = DL(MB(), 'Monty', MB())
#         tn4: DL[str] = DL(MB(), 'Python', MB(tn2))
#         tn5: DL[str] = DL(MB(tn3), 'Monty Python', MB(tn4))
#         assert tn5.has_left()
#         assert tn5.has_right()
#         assert not tn4.has_left()
#         assert tn4.has_right()
#         assert not tn3.has_left()
#         assert not tn3.has_right()
#         assert not tn2.has_left()
#         assert tn2.has_right()
#         assert not tn1.has_left()
#         assert tn1.has_right()
#         assert not tn0.has_left()
#         assert not tn0.has_right()
