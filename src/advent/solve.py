import click

from advent.day01 import Day01
from advent.day02 import Day02
from advent.day03 import Day03
from advent.day04 import Day04
from advent.solution import load_input


@click.command()
@click.argument("day", type=int, required=True)
def main(day: int) -> None:
    match day:
        case 1:
            problem = Day01(load_input("data/day01.txt"))
        case 2:
            problem = Day02(load_input("data/day02.txt"))
        case 3:
            problem = Day03(load_input("data/day03.txt"))
        case 4:
            problem = Day04(load_input("data/day04.txt"))
    print(problem.solve_part1())
    print(problem.solve_part2())


if __name__ == "__main__":
    main()
