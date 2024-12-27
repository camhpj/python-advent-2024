import click

from advent.day01 import Day01
from advent.day02 import Day02
from advent.day03 import Day03
from advent.day04 import Day04
from advent.day05 import Day05
from advent.day06 import Day06
from advent.solution import load_input


@click.command()
@click.argument("day", type=int, required=True)
def main(day: int) -> None:
    match day:
        case 1:
            prob = Day01(load_input("data/day01.txt"))
        case 2:
            prob = Day02(load_input("data/day02.txt"))
        case 3:
            prob = Day03(load_input("data/day03.txt"))
        case 4:
            prob = Day04(load_input("data/day04.txt"))
        case 5:
            prob = Day05(load_input("data/day05.txt"))
        case 6:
            prob = Day06(load_input("data/day06.txt"))
    print(prob.solve_part1())
    print(prob.solve_part2())


if __name__ == "__main__":
    main()
