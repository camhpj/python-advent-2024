import numpy as np

from advent.solution import Solution


class Day02(Solution):
    def preprocess(self) -> list[np.ndarray]:
        return [np.array(list(map(int, line.split(" ")))) for line in self.input.split("\n")]

    def solve_part1(self) -> int:
        lines = self.preprocess()
        safe = 0
        for l in lines:
            if not (all(l[:-1] > l[1:]) or all(l[:-1] < l[1:])):
                continue
            delta = abs(l[:-1] - l[1:])
            if not (all(delta > 0) and all(delta < 4)):
                continue
            safe += 1
        return safe

    def solve_part2(self) -> int:
        lines = self.preprocess()
        safe = 0

        all_lines = []
        for l in lines:
            tmp = []
            for i, _ in enumerate(l):
                tmp.append(np.delete(l, i))
            all_lines.append(tmp)

        for group in all_lines:
            for l in group:
                if not (all(l[:-1] > l[1:]) or all(l[:-1] < l[1:])):
                    continue
                delta = abs(l[:-1] - l[1:])
                if not (all(delta > 0) and all(delta < 4)):
                    continue
                safe += 1
                break
        return safe
