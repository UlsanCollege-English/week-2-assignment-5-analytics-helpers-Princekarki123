from typing import List, Optional


def chunk(values: List[int], size: int) -> List[List[int]]:
    """Split `values` into chunks of length `size`.

    Last chunk may be shorter. If `size <= 0`, raise ValueError.
    """
    if size <= 0:
        raise ValueError("chunk size must be positive")

    return [values[i:i+size] for i in range(0, len(values), size)]


def running_total(start: int, changes: List[int]) -> List[int]:
    """Return running totals starting from `start`, after each change."""
    result = []
    total = start
    for change in changes:
        total += change
        result.append(total)
    return result


def index_of_first_at_least(values: List[int], threshold: int) -> Optional[int]:
    """Return index of the first element >= threshold, else None."""
    for i, v in enumerate(values):
        if v >= threshold:
            return i
    return None
