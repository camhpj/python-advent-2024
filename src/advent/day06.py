from itertools import cycle

import numpy as np

from advent.solution import Solution


class Day06(Solution):
    def preprocess(self) -> np.ndarray:
        return np.array([[*i] for i in self.input.split("\n")])

    def solve_part1(self) -> int:
        map_ = self.preprocess()
        i, j = np.ravel(np.where(map_ == "^"))
        for point in cycle(["N", "E", "S", "W"]):
            d = 1
            prev = i, j
            while True:
                match point:
                    case "N":
                        x, y = i - d, j
                    case "E":
                        x, y = i, j + d
                    case "S":
                        x, y = i + d, j
                    case "W":
                        x, y = i, j - d
                    case _:
                        raise ValueError()
                d += 1
                try:
                    if map_[x, y] == "#":
                        i, j = prev
                        break
                    else:
                        map_[prev] = "X"
                        map_[x, y] = "^"
                        prev = x, y
                except IndexError:
                    return np.where(map_ == "X")[0].shape[0] + 1

    def solve_part2(self) -> int:
        return 0
