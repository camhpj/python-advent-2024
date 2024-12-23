from advent.day01 import Day01
from advent.day02 import Day02
from advent.day03 import Day03
from advent.solution import load_input


def test_Day01() -> None:
    prob = Day01(load_input("tests/data/day01.txt"))
    assert prob.solve_part1() == 11
    assert prob.solve_part2() == 31


def test_Day02() -> None:
    prob = Day02(load_input("tests/data/day02.txt"))
    assert prob.solve_part1() == 2
    assert prob.solve_part2() == 4


def test_Day03() -> None:
    prob = Day03("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    assert prob.solve_part1() == 161
    prob = Day03("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    assert prob.solve_part2() == 48
