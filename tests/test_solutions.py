from advent.day1 import Day1
from advent.solution import load_puzzle


def test_Day1() -> None:
    prob = Day1(load_puzzle("tests/data/day01.txt"))
    assert prob.solve_part1() == 11
    assert prob.solve_part2() == 31
