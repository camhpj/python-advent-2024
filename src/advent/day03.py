import re

from advent.solution import Solution


class Day03(Solution):
    def solve_part1(self) -> int:
        total = 0
        for match in re.findall(r"mul\((\d+),(\d+)\)", self.input):
            x = int(match[0])
            y = int(match[1])
            total += x * y
        return total

    def solve_part2(self) -> int:
        return 0
