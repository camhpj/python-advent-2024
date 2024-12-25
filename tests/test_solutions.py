from advent.day01 import Day01
from advent.day02 import Day02
from advent.day03 import Day03
from advent.day04 import Day04
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
    prob = Day03(load_input("tests/data/day03_1.txt"))
    assert prob.solve_part1() == 161
    prob = Day03(load_input("tests/data/day03_2.txt"))
    assert prob.solve_part2() == 48


def test_Day04() -> None:
    prob = Day04(load_input("tests/data/day04.txt"))
    assert prob.solve_part1() == 18
    # assert prob.solve_part2()
