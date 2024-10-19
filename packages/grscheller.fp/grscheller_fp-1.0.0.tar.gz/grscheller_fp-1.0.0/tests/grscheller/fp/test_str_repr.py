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

from typing import Optional
from grscheller.fp.nothingness import _NoValue, noValue
from grscheller.fp.err_handling import MB, XOR

def addLt42(x: int, y: int) -> int|_NoValue:
    sum = x + y
    if sum < 42:
        return sum
    return noValue

class Test_str:
    def test_MB_str(self) -> None:
        n1: MB[int] = MB()
        o1 = MB(42)
        assert str(n1) == 'MB()'
        assert str(o1) == 'MB(42)'
        mb1 = MB(addLt42(3, 7))
        mb2 = MB(addLt42(15, 30))
        assert str(mb1) == 'MB(10)'
        assert str(mb2) == 'MB()'
        nt1: MB[int] = MB()
        nt2: MB[int] = MB(noValue)
        nt3: MB[int] = MB()
        s1 = MB(1)
        assert str(nt1) == str(nt2) == str(nt3) == str(mb2) =='MB()'
        assert str(s1) == 'MB(1)'

    def test_XOR_str(self) -> None:
        assert str(XOR(10, '')) == '< 10 | >'
        assert str(XOR(addLt42(10, -4), 'foofoo')) == '< 6 | >'
        assert str(XOR(addLt42(10, 40), '')) == "< |  >"
        assert str(XOR(noValue, 'Foofoo rules')) == "< | Foofoo rules >"
        assert str(XOR(42, '')) == "< 42 | >"
        assert str(XOR('13', 0)) == "< 13 | >"

    def test_noValue_str(self) -> None:
        assert str(noValue) == 'noValue'

class Test_repr:
    def test_mb_repr(self) -> None:
        mb1: MB[object] = MB()
        mb2: MB[object] = MB()
        mb3: MB[object] = MB(noValue)
        assert mb1 == mb2 == mb3 == MB()
        assert repr(mb2) == 'MB()'
        mb4 = eval(repr(mb3))
        assert mb4 == mb3

        def lt5orNothing1(x: int) -> int|_NoValue:
            if x < 5:
                return x
            else:
                return noValue

        def lt5orNothing2(x: int) -> MB[int]:
            if x < 5:
                return MB(x)
            else:
                return MB()

        mb5 = MB(lt5orNothing1(2))
        mb6 = lt5orNothing2(2)
        mb7 = lt5orNothing2(3)
        mb8 = MB(lt5orNothing1(7))
        mb9 = lt5orNothing2(8)

        assert mb5 == mb6
        assert mb6 != mb7
        assert mb8 == mb9

        assert repr(mb5) == repr(mb6) ==  'MB(2)'
        assert repr(mb7) ==  'MB(3)'
        assert repr(mb8) == repr(mb9) ==  'MB()'

        foofoo = MB(MB('foo'))
        foofoo2 = eval(repr(foofoo))
        assert foofoo2 == foofoo
        assert repr(foofoo) == "MB(MB('foo'))"

    def test_xor_repr(self) -> None:
        e1: XOR[int, str] = XOR(right='Nobody home!')
        e2: XOR[int, str] = XOR(right='Somebody not home!')
        e3: XOR[int, str] = XOR(right='')
        assert e1 != e2
        e5 = eval(repr(e2))
        assert e2 != XOR(right='Nobody home!')
        assert e2 == XOR(right='Somebody not home!')
        assert e5 == e2
        assert e5 != e3
        assert e5 is not e2
        assert e5 is not e3

        def lt5_or_nothing(x: int) -> int|_NoValue:
            if x < 5:
                return x
            else:
                return noValue

        def lt5_or_none_XOR(x: int) -> XOR[int, str]:
            if x < 5:
                return XOR(x, 'None!')
            else:
                return XOR(noValue, f'was to be {x}')

        e1 = XOR(lt5_or_nothing(2), 'potential right value does not matter')
        e2 = lt5_or_none_XOR(2)
        e3 = lt5_or_none_XOR(3)
        e7: XOR[int, str] = XOR(lt5_or_nothing(7), 'was to be 7')
        e8 = XOR(8, 'no go for 8').flatMap(lt5_or_none_XOR)

        assert e1 == e2
        assert e2 != e3
        assert e7 != e8
        assert e7 == eval(repr(e7))

        assert repr(e1) ==  "XOR(2, 'potential right value does not matter')"
        assert repr(e2) ==  "XOR(2, 'None!')"
        assert repr(e3) ==  "XOR(3, 'None!')"
        assert repr(e7) == "XOR(right='was to be 7')"
        assert repr(e8) ==  "XOR(right='was to be 8')"
