from abc import abstractmethod, ABC
from typing import Any


class Solution(ABC):
    def __init__(self, input: str) -> None:
        self.input = input

    @abstractmethod
    def solve_part1(self) -> Any:
        return

    @abstractmethod
    def solve_part2(self) -> Any:
        return


def load_puzzle(path: str) -> str:
    with open(path, "r") as f:
        data = f.read()
    return data
