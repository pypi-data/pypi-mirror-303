
from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from typing import Literal, Tuple, Union


class BatchMaker:
    """Create batches
    """

    @classmethod
    def get_batches(
        cls,
        docs: Iterable[Iterable[str]],
        batchsize: int
    ) -> Iterable[Iterable[str]]:
        """Get batches from a docstream

        Parameters
        ----------
        docs : Iterable[Iterable[str]]
            The `Doc Stream`
        batchsize : int

        Example
        -------
        >>> docs = ['abce def geghieo', 'C D E F']
        >>> batches = BatchMaker.get_batches(docs, batchsize=3)
        >>> bchs = list(batches)
        >>> bchs[0]
        ['a', 'b', 'c']
        >>> bchs[-1]
        ['E', ' ', 'F']

        Yields
        ------
        Iterator[Iterable[Iterable[str]]]
            The $BATCH STREAAM$
        """
        for doc in docs:
            tokenlist = list(doc)
            docsize = len(tokenlist)
            for i in range(docsize-batchsize+1):
                yield tokenlist[i:i+batchsize]

    @classmethod
    def get_cobatches(
        cls,
        docs: Iterable[Iterable[str]],
        batchsize: int,
        offset: int
    ) -> Iterable[Tuple[Iterable[str], Iterable[str]]]:
        """Get a list of (anchorbatch, workingbatch)

        Parameters
        ----------
        docs : Iterable[Iterable[str]]
        batchsize : int
        offset : int
            Normally a multiple of the batchsize

        Example
        -------
        >>> docs = ['abcdefgeghieo', 'Hello world!']
        >>> batches = BatchMaker.get_cobatches(docs, batchsize=3, offset=3)
        >>> bchs = list(batches)
        >>> bchs[0]
        (['a', 'b', 'c'], ['d', 'e', 'f'])

        Yields
        ------
        Iterable[Tuple[Iterable[str],Iterable[str]]]
            ((<anchorbatch>, <workingbatch>))
        """
        for doc in docs:
            tokenlist = list(doc)
            docsize = len(tokenlist)
            fullspan = batchsize + offset + batchsize
            for i in range(docsize-fullspan+1):
                yield (
                    # Anchor batch
                    tokenlist[i:i+batchsize],
                    # Working batch
                    tokenlist[i+offset:i+offset+batchsize]
                )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
