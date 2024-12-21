from advent.day01 import Day01
from advent.day02 import Day02
from advent.solution import load_input


def test_Day1() -> None:
    prob = Day01(load_input("tests/data/day01.txt"))
    assert prob.solve_part1() == 11
    assert prob.solve_part2() == 31


def test_Day2() -> None:
    prob = Day02(load_input("tests/data/day01.txt"))
    assert prob.solve_part1() == 0
    # assert prob.solve_part2()
