"""Wrap around the standard counter
"""


from collections import Counter, defaultdict
from typing import Any, Dict, Iterable, Tuple

import numpy as np


class CoolCounter:
    def __init__(self) -> None:
        self.counts: Counter = Counter()
        self.samplesize: int = 0

    def __call__(self, stream: Iterable) -> Any:
        self.counts = Counter(stream)

    def reset(self):
        self.counts = Counter()
        self.samplesize = 0

    def topn(self, n=10):
        return self.counts.most_common(n=n)

    def chaincount(self, iterables: Iterable[Iterable[str]]):
        for inner in iterables:
            self.counts.update(inner)
            self.samplesize += 1

    def chaincount_unique(self, iterables: Iterable[Iterable[str]]):
        """_summary_

        Parameters
        ----------
        iterables : Iterable[Iterable[str]]
            _description_

        Example
        -------
        >>> cnter = CoolCounter()
        >>> cnter.chaincount_unique(['abc', 'ab', 'aaaaaa'])
        >>> cnter.counts['a']
        3
        """
        for inner in iterables:
            self.counts.update(set(inner))
            self.samplesize += 1

    @classmethod
    def merge(cls, counters: Iterable[Counter]) -> Counter:
        cnt = Counter()
        for counter in counters:
            cnt.update(counter)
        return cnt

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    @property
    def frequencies_as_arrays(self) -> Tuple[np.ndarray, np.ndarray]:
        total = self.total
        counts = self.counts
        keys = np.array(list(counts.keys()))
        freqs = np.array(
            [count / total for count in counts.values()], dtype=float)
        return keys, freqs

    @property
    def frequencies(self) -> Dict[str, float]:
        total = self.total
        freqs = {
            name: count / total for name, count in self.counts.items()
        }
        return freqs


if __name__ == "__main__":
    import doctest
    doctest.testmod()
