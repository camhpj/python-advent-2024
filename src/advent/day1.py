from advent.solution import Solution


class Day1(Solution):
    def preprocess(self) -> tuple[list[int], list[int]]:
        left, right = zip(*(map(int, line.split("   ")) for line in self.input.split("\n")))
        return (left, right)

    def solve_part1(self) -> int:
        left, right = self.preprocess()
        return sum([abs(i - j) for i, j in zip(sorted(left), sorted(right))])

    def solve_part2(self) -> None:
        left, right = self.preprocess()
        return sum([i * right.count(i) for i in left])
