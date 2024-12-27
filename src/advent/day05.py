from collections import defaultdict
from typing import DefaultDict

from advent.solution import Solution


class Day05(Solution):
    def preprocess(self) -> tuple[DefaultDict[int, list[int]], list[list[int]]]:
        part1, part2 = self.input.split("\n\n")
        page_rules = [list(map(int, i.split("|"))) for i in part1.split("\n")]
        page_order = [list(map(int, i.split(","))) for i in part2.split("\n")]
        map_ = defaultdict(list)
        for i, j in page_rules:
            map_[i].append(j)
        return (map_, page_order)

    def update_indices(self, num: int, i: int, idx: dict[int, int]) -> dict[int, int]:
        if i in idx.values():
            for k, v in idx.items():
                if v <= i:
                    idx[k] = v - 1
        idx[num] = i if i != 1e8 else max(idx.values()) + 1
        return idx

    def solve_line(self, line: list[int], map_: DefaultDict[int, list[int]]) -> tuple[dict[int, int], bool]:
        idx = {line[0]: 0}
        for num in line[1:]:
            i = 1e8
            for el in map_[num]:
                if el not in idx.keys():
                    continue
                tmp = idx[el] - 1
                if tmp <= i:
                    i = tmp
            idx = self.update_indices(num, i, idx)
        in_order = line == [j for _, j in sorted(zip(idx.values(), idx.keys()))]
        return (idx, in_order)

    def solve_part1(self) -> int:
        map_, page_order = self.preprocess()
        count = 0
        for line in page_order:
            _, in_order = self.solve_line(line, map_)
            if in_order:
                count += line[len(line) // 2]
        return count

    def solve_part2(self) -> int:
        map_, page_order = self.preprocess()
        count = 0
        for line in page_order:
            idx, in_order = self.solve_line(line, map_)
            if in_order:
                continue
            line_y = [j for _, j in sorted(zip(idx.values(), idx.keys()))]
            count += line_y[len(line_y) // 2]
        return count
