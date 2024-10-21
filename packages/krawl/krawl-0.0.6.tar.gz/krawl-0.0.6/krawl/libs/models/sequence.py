from __future__ import annotations

from typing import List, Union


class SequenceBase:

    def __init__(self, items: Union[str, List]) -> None:
        """Sequence the item in it

        An item can also be a Sequence


        Example
        -------
        >>> seq = SequenceBase(["hello", SequenceBase("world of war"), "end here!"])
        >>> for x in seq:
        >>>     print(x)
        >>> print(seq)
        >>> for ch in seq.chars():
        >>>     print(ch)
        """
        self.items: List[Union[str, SequenceBase]]
        if isinstance(items, str):
            self.items = [items]
        else:
            self.items = items

    def __iter__(self):
        yield from self.items

    def chars(self):
        for item in self.items:
            if isinstance(item, str):
                yield from item
            else:
                yield from item.chars()

    def add(self, item):
        self.items.append(item)

    def __str__(self) -> str:
        return '*'.join(x if isinstance(x, str) else str(x) for x in self.items)
