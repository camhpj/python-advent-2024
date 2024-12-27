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
            while map_[i, j] != "#":
                prev = i, j
                map_[i, j] = "X"
                match point:
                    case "N":
                        x, y = i - 1, j
                    case "E":
                        x, y = i, j + 1
                    case "S":
                        x, y = i + 1, j
                    case "W":
                        x, y = i, j - 1
                    case _:
                        raise ValueError()
                i, j = x, y
                if (i // map_.shape[0] != 0) or (j // map_.shape[1] != 0):
                    return np.where(map_ == "X")[0].shape[0]
            i, j = prev  # move back one

    def solve_part2(self) -> int:
        return 0
