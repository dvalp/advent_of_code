import numpy as np


def estimate_fuel(mass):
    return mass // 3 - 2


def sum_masses():
    with open("input_day01", 'r') as f:
        print(sum(estimate_fuel(int(line)) for line in f))


def estimate_full_fuel(mass):
    subtotal = 0
    while mass > 0:
        mass = estimate_fuel(mass)
        if mass > 0:
            subtotal += mass

    return subtotal


def sum_full_estimates():
    with open("input_day01", 'r') as f:
        return np.array(estimate_full_fuel(int(line)) for line in f).sum()


def fuel_w_numpy():
    masses = np.loadtxt("input_day01", dtype=int)
    return np.vectorize(estimate_full_fuel)(masses).sum()


if __name__ == '__main__':
    # Result == 5180690
    result = fuel_w_numpy()
    assert result == 5180690
