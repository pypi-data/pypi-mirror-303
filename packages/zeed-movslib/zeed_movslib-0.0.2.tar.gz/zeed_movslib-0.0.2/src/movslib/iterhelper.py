from itertools import chain
from typing import TYPE_CHECKING
from typing import TypeVar

if TYPE_CHECKING:
    from collections.abc import Iterable

T = TypeVar('T')


def zip_with_next(
    it: 'Iterable[T]', last: T | None
) -> 'Iterable[tuple[T, T | None]]':
    c = chain(it, (last,))
    next(c)
    return zip(it, c, strict=True)
