import click
from advent.day1 import Day1
from advent.solution import load_puzzle


@click.command()
@click.argument("day", type=int, required=True)
def main(day: int) -> None:
    match day:
        case 1:
            problem = Day1(load_puzzle("data/day01.txt"))
    print(problem.solve_part1())
    print(problem.solve_part2())


if __name__ == "__main__":
    main()
