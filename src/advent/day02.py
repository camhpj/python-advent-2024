from advent.solution import Solution


class Day02(Solution):
    def preprocess(self) -> list[list[int]]:
        return [list(map(int, line.split(" "))) for line in self.input.split("\n")]

    def solve_part1(self) -> int:
        return 0

    def solve_part2(self) -> int:
        return 0
