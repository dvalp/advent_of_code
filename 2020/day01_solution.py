from itertools import combinations
from typing import Iterable

import numpy as np


def find_product(expense_items: Iterable, num_inputs: int) -> np.ndarray:
    """
    Naive approach does well enough in efficiency. Simply tries to calculate
    all combinations for any number of inputs. It's flexible, but does not
    scale well.

    :param expense_items: Iterable of integers to use as inputs
    :param num_inputs: Number of inputs to use for calculations
    :return: numpy array containing the product of the selected inputs
    """
    target_sum = 2020

    for cmb in combinations(expense_items, num_inputs):
        if sum(cmb) == target_sum:
            return np.prod(cmb)
    else:
        raise ValueError(f"Cannot find two elements in the list that sum to {target_sum}")


def find_prod(expense_items: Iterable) -> np.ndarray:
    """
    Not as flexible, but less than 1/100 of the time to calculate the result
    when compared with the other method.

    :param expense_items: Iterable of integers to use as inputs
    :return: numpy array containing the product of the selected inputs
    """
    target_sum = 2020

    s_expenses = set(expense_items)
    for cmb in combinations(s_expenses, 2):
        if (other := target_sum - sum(cmb)) in s_expenses:
            return np.prod([*cmb, other])
    else:
        raise ValueError(f"Cannot find two elements in the list that sum to {target_sum}")


if __name__ == '__main__':
    expenses = set(np.loadtxt("input_day01.txt", dtype=int))

    print(find_prod(expenses))
