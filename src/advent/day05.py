from collections import defaultdict

from advent.solution import Solution


class Day05(Solution):
    def preprocess(self) -> tuple[list[list[int], list[list[int]]]]:
        part1, part2 = self.input.split("\n\n")
        page_rules = [list(map(int, i.split("|"))) for i in part1.split("\n")]
        page_order = [list(map(int, i.split(","))) for i in part2.split("\n")]
        return (page_rules, page_order)

    def solve_part1(self) -> int:
        page_rules, page_order = self.preprocess()
        map_ = defaultdict(list)
        for i, j in page_rules:
            map_[i].append(j)

        count = 0
        for line in page_order:
            idx = {line[0]: 0}
            for num in line[1:]:
                num_idx = 1e8
                for el in map_[num]:
                    try:
                        tmp = idx[el] - 1
                        if tmp <= num_idx:
                            num_idx = tmp
                    except KeyError:
                        continue
                if num_idx == 1e8:
                    num_idx = max(idx.values()) + 1
                idx[num] = num_idx

            line_y = [j for _, j in sorted(zip(idx.values(), idx.keys()))]
            if line == line_y:
                count += line[len(line) // 2]
        return count

    def solve_part2(self) -> int:
        return 0
