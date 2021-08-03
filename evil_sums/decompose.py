from itertools import chain, combinations
from typing import Iterable, Optional


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def get_constituents(options: Iterable[int], target: int) -> Optional[set[int]]:
    for subset in powerset(options):
        if sum(subset) == target:
            return subset
