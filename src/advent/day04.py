import numpy as np

from advent.solution import Solution
from typing import Callable

class Day04(Solution):
    def preprocess(self) -> np.ndarray:
        return np.array([np.array(list(i)) for i in self.input.split("\n")])

    def solve_char_part1(self, t: np.ndarray, i: int, j: int) -> int:
        def check_equality(
            x: np.ndarray,
            y: np.ndarray = np.array(["X", "M", "A", "S"]),
            inverse: bool = False,
        ) -> bool:
            if inverse:
                y = np.flip(y)
            if all(x == y):
                return True
            return False

        if t[i, j] != "X":
            return 0
        z = t.shape[1] - 4

        count = 0
        if (j <= z) and check_equality(t[i, j : j + 4]):  # E
            count += 1
        if (j >= 3) and check_equality(t[i, j - 3 : j + 1], inverse=True):  # W
            count += 1
        if (i <= z) and check_equality(t[i : i + 4, j]):  # S
            count += 1
        if (i >= 3) and check_equality(t[i - 3 : i + 1, j], inverse=True):  # N
            count += 1
        if (i >= 3) and (j <= z) and check_equality(np.array([t[i, j], t[i - 1, j + 1], t[i - 2, j + 2], t[i - 3, j + 3]]).flatten()):  # NE
            count += 1
        if (i >= 3) and (j >= 3) and check_equality(np.array([t[i, j], t[i - 1, j - 1], t[i - 2, j - 2], t[i - 3, j - 3]]).flatten()):  # NW
            count += 1
        if (i <= z) and (j <= z) and check_equality(np.array([t[i, j], t[i + 1, j + 1], t[i + 2, j + 2], t[i + 3, j + 3]]).flatten()):  # SE
            count += 1
        if (i <= z) and (j >= 3) and check_equality(np.array([t[i, j], t[i + 1, j - 1], t[i + 2, j - 2], t[i + 3, j - 3]]).flatten()):  # SW
            count += 1
        return count

    def solve_char_part2(self, t: np.ndarray, i: int, j: int) -> int:
        def check_equality(
            x1: np.ndarray,
            x2: np.ndarray,
            y: np.ndarray = np.array(["M", "A", "S"]),
            inverse: bool = False,
        ) -> bool:
            if inverse:
                y = np.flip(y)
            if all(x1 == y) and all(x2 == y):
                return True
            return False

        if t[i, j] != "A":
            return 0
        z = t.shape[1] - 4

        count = 0
        return count

    def solve(self, func: Callable) -> int:
        count = 0
        t = self.preprocess()
        for i, line in enumerate(t):
            for j, _ in enumerate(line):
                count += func(t, i, j)
        return count

    def solve_part1(self) -> int:
        return self.solve(self.solve_char_part1)

    def solve_part2(self) -> int:
        return self.solve(self.solve_char_part2)
