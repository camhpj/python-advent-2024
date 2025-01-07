import re
from itertools import cycle

import numpy as np

from advent.solution import Solution


class Day06(Solution):
    def preprocess(self) -> np.ndarray:
        return np.array([[*i] for i in self.input.split("\n")])

    def solve_map(self, map_: np.ndarray) -> tuple[np.ndarray, list[tuple[int, int]]]:
        moves = []
        i, j = np.ravel(np.where(map_ == "^"))
        for point in cycle(["N", "E", "S", "W"]):
            while map_[i, j] != "#":
                prev = i, j
                map_[i, j] = "X"
                moves.append((i, j, point))
                match point:
                    case "N":
                        i, j = i - 1, j
                    case "E":
                        i, j = i, j + 1
                    case "S":
                        i, j = i + 1, j
                    case "W":
                        i, j = i, j - 1
                    case _:
                        raise ValueError()
                if (i // map_.shape[0] != 0) or (j // map_.shape[1] != 0):
                    return (map_, moves)
            i, j = prev  # move back one

    def solve_part1(self) -> int:
        map_, _ = self.solve_map(self.preprocess())
        return np.where(map_ == "X")[0].shape[0]

    def solve_part2(self) -> int:
        map_, moves = self.solve_map(self.preprocess())
        count = 0
        for idx, (x, y, _) in enumerate(moves[2:]):
            i, j, point = moves[idx + 1]
            if (x, y) == (i, j):
                continue
            match point:
                case "N":
                    path = map_[i, j+1:]
                case "E":
                    path = map_[i+1:, j]
                case "S":
                    path = np.flip(map_[i, :j])
                case "W":
                    path = np.flip(map_[:i, j])
                case _:
                    raise ValueError()
            if re.match(r"^X+#\.*$", "".join(path)):
                # print(x, y)
                count += 1
        return count
