from functools import lru_cache
from itertools import chain


def _canon(seq):
    """
    Return a sequence in its "canonical" form, i.e. if and only if seq1 and
    seq2 are equivalent under rotation and/or reflection, then

        _canon(seq1) == _canon(seq2)

    e.g.

        (0, 0, 1, 1) and (0, 1, 1, 0) are equivalent.
        (0, 0, 1, 1) and (0, 1, 0, 1) are not equivalent.
        (0, 1, 2, 3) and (3, 2, 1, 0) are equivalent.
        (0, 1, 2, 3) and (0, 3, 1, 2) are not equivalent.
    """
    # We just build all 8 options and let Python choose whichever floats to the top.
    rev = tuple(reversed(seq))
    return sorted(
        chain(
            ((*seq[i:], *seq[:i]) for i in range(4)),
            ((*rev[i:], *rev[:i]) for i in range(4)),
        )
    )[0]


@lru_cache(maxsize=None)
def _diffy(seq):
    if not any(seq):
        return 1
    return 1 + _diffy(
        _canon(tuple(abs(x - y) for x, y in zip(seq, [*seq[1:], seq[0]])))
    )


def diffy(seq):
    """Return the number of squares created by the diffy process."""
    # Fun fact: This process is guaranteed to terminate only with squares
    if len(seq) != 4:
        raise ValueError(
            "Sequences representing diffy squares must have exactly 4 elements"
        )
    return _diffy(_canon(tuple(seq)))
