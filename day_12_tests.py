from unittest import TestCase
import day_12


class Tests(TestCase):
    def test_small_set(self):
        self.assertEqual(day_12.count_paths(
            """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
        ), 10)

    def test_small_set_2(self):
            self.assertEqual(day_12.count_paths(
                """start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end"""
            , True), 36)

    def test_medium(self):
        self.assertEqual(day_12.count_paths(
            """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
        ), 19)

    def test_large(self):
        self.assertEqual(day_12.count_paths(
            """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
        ), 226)

    def test_day_1(self):
        day_12.count_paths(
            """um-end
pk-um
FE-il
ay-FE
pk-start
end-jt
um-FE
RO-il
xc-ay
il-end
start-EZ
pk-FE
xc-start
jt-FE
EZ-um
pk-xc
xc-EZ
pk-ay
il-ay
jt-EZ
jt-om
pk-EZ"""
        , True)


