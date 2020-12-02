import numpy as np
from typing import Iterable


def detect_increasing(nums: Iterable) -> bool:
    return all(np.diff(nums) >= 0)


def detect_duplicates(digits: Iterable) -> bool:
    # return any(np.diff(digits) == 0)
    # New test is to ensure that at least one group only appears once
    return 2 in np.unique(digits, return_counts=True)[1]


def valid_password():
    candidates = np.array([np.array(list(str(number))) for number in np.arange(256310, 732737)], dtype=int)
    valid = [all([detect_increasing(code), detect_duplicates(code)]) for code in candidates]
    return len(candidates[valid])
