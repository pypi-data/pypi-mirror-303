from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from typing import Literal, Tuple, Union


class NestedCounter:
    """For nested counting
    """

    def __init__(self, iterable: Union[Iterable[Tuple], None] = None):
        """NestedCounter

        Returns
        -------
        _type_
            _description_

        Exampes
        -------
        >>> nc = NestedCounter()
        >>> nc.update(('a', 'b', 'x'))
        >>> nc.update(('a', 'b', 'x'))
        >>> nc.update(('a', 'c', 'y'))
        >>> nc
        defaultdict(<class '__main__.NestedCounter'>, {'a': defaultdict(<class '__main__.NestedCounter'>, {'b': defaultdict(<class '__main__.NestedCounter'>, {'x': 2}), 'c': defaultdict(<class '__main__.NestedCounter'>, {'y': 1})})})
        >>> nc = NestedCounter((('a', 'b'), ('a', 'c')))
        >>> nc
        defaultdict(<class '__main__.NestedCounter'>, {'a': defaultdict(<class '__main__.NestedCounter'>, {'b': 1, 'c': 1})})
        """
        self.counter = defaultdict(NestedCounter)
        if iterable is not None:
            for item in iterable:
                self._increment_by_path(item, 1)

    def update(self, items: Union[NestedCounter, Iterable]) -> None:
        """_summary_

        Parameters
        ----------
        items : Union[NestedCounter, Iterable]
            _description_

        Examples
        --------
        >>> nc = NestedCounter()
        >>> nc.update(('a', 'b', 'x'))
        >>> nc.update(('a', 'b', 'x'))
        >>> nc2 = NestedCounter()
        >>> nc2.update(('a', 'b', 'x'))
        >>> nc.update(nc2)
        >>> print(nc)
        defaultdict(<class '__main__.NestedCounter'>, {'a': defaultdict(<class '__main__.NestedCounter'>, {'b': defaultdict(<class '__main__.NestedCounter'>, {'x': 3})})})
        """
        if isinstance(items, NestedCounter):
            # Case: homogeneous source
            for path, count in items:
                self._increment_by_path(path, count)
        elif isinstance(items, Iterable):
            # Case: an iterable of keys
            self._increment_by_path(items, count=1)

    def remove(self, *keys):
        """Navigate to the second last key to allow deletion of the last one
        Examples
        --------

        >>> nc = NestedCounter()
        >>> nc.update(('a', 'b', 'x'))
        >>> nc.remove('a', 'b', 'x')
        >>> print(nc)
        defaultdict(<class '__main__.NestedCounter'>, {'a': defaultdict(<class '__main__.NestedCounter'>, {'b': defaultdict(<class '__main__.NestedCounter'>, {})})})
        """
        # Start at top-level (self)
        current = self

        # Navigate to the immediate parent of the final key
        *leading_keys, last_key = keys
        for key in leading_keys:
            current = current.counter[key]

        # Delete the final key
        del current.counter[last_key]

    def _increment_by_path(self, path: Tuple[str, ...], count: int) -> None:
        """Helper function to increment by a given path and count

        Parameters
        ----------
        path : _type_
            _description_
        count : _type_
            _description_
        """
        current = self
        *keys, last_key = path
        for key in keys:
            current = current.counter[key]
        if last_key not in current.counter:
            current.counter[last_key] = 0
        current.counter[last_key] += count

    def fronts(self):
        yield from self.counter.keys()

    def __iter__(self):
        """Make this class an Iterable

        Yields
        ------
        Iterator[Tuple[Tuple[str, ...], int]]
            (key_path, count) pairs
        """
        for key, sub_counter in self.counter.items():
            if isinstance(sub_counter, NestedCounter):
                # For nested structures, append the current key to the path
                for sub_key_path, sub_count in sub_counter:
                    yield (key,) + sub_key_path, sub_count
            else:
                # Yield leaf key and its count
                yield (key,), sub_counter

    def __repr__(self):
        return repr(self.counter)

    def remove_empty_nodes(self):
        """
        Recursively remove empty nodes from the nested counter.

        Examples
        --------
        >>> nc = NestedCounter()
        >>> nc.update(('a', 'b', 'x'))
        >>> nc.update(('a', 'b', 'y'))
        >>> nc.remove('a', 'b', 'x')
        >>> nc.remove_empty_nodes()
        >>> print(nc)
        defaultdict(<class '__main__.NestedCounter'>, {'a': defaultdict(<class '__main__.NestedCounter'>, {'b': defaultdict(<class '__main__.NestedCounter'>, {'y': 1})})})
        """
        def clean_empty(counter):
            # Iterate over the current level keys
            keys_to_delete = []
            for key, sub_counter in list(counter.items()):
                if isinstance(sub_counter, NestedCounter):
                    # Recursively clean sub-counters
                    clean_empty(sub_counter.counter)
                    # If the sub-counter is now empty, mark it for deletion
                    if not sub_counter.counter:
                        keys_to_delete.append(key)
                elif not sub_counter:  # Handle leaf-level empty values
                    keys_to_delete.append(key)
            for key in keys_to_delete:
                del counter[key]

        clean_empty(self.counter)

    def __getitem__(self, key: str) -> Union['NestedCounter', int]:
        """Dict-like item access

        Parameters
        ----------
        key : _type_
            _description_

        Examples
        --------
        >>> nc = NestedCounter()
        >>> nc.update(('a', 'b', 'x'))
        >>> nc.update(('a', 'b', 'y'))
        >>> nc['a']['b']
        defaultdict(<class '__main__.NestedCounter'>, {'x': 1, 'y': 1})
        """
        return self.counter[key]

    def __setitem__(self, key, value):
        if isinstance(value, int):
            self.counter[key] = value
        else:
            raise ValueError(
                "NestedCounter only supports integer values at the leaves.")

    def rlen(self, take_one: bool = True) -> int:
        """
        Recursively count #LeafNodes (end nodes storing counts).

        Examples
        --------
        >>> nc = NestedCounter()
        >>> nc.update(('a', 'b', 'c'))
        >>> nc.update(('a', 'b', 'c'))
        >>> nc.update(('a', 'b', 'd'))
        >>> nc.rlen()
        2
        >>> nc.rlen(take_one=False)
        3
        """
        total_leaves = 0
        for _, value in self.counter.items():
            if isinstance(value, NestedCounter):
                total_leaves += value.rlen(take_one=take_one)
            else:
                total_leaves += 1 if take_one else value
        return total_leaves


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    nc = NestedCounter()
    nc.update(('a', 'b', 'c'))
    nc.update(('a', 'b', 'c'))
    nc.update(('a', 'p', 'q'))
    for i in nc.fronts():
        print(i)
    for i in nc['a'].fronts():
        print(i)
