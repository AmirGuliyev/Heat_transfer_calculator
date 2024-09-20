import numpy as np
import itertools
from CalCop import Integrator


def armean(*numbers) -> float:
    return sum(numbers) / len(numbers)


def geomean(numbers: list) -> float:
    return np.prod(numbers) ** (1 / len(numbers))


def harmomean(numbers: list) -> float:
    combo = list(itertools.combinations(numbers, 2))
    combo = [int(np.prod(x)) for x in combo]
    return len(numbers) * np.prod(numbers) / sum(combo)


def funcmean(x1: float, x2: float) -> float:
    integrator = Integrator(tar_func=lambda x: x**2)
    return integrator.integral(x1, x2) / (x2 - x1)


def rms_disc(numbers: list) -> float:
    numbers = np.array(numbers) ** 2
    return np.sqrt(sum(numbers) / len(numbers))


def cub_mean(numbers: list) -> float:
    numbers = np.array(numbers) ** 3
    return (sum(numbers) / len(numbers)) ** (1 / 3)


def rms_cont(x1: float, x2: float) -> float:
    integrator = Integrator(tar_func=lambda x: x**2)
    return np.sqrt(integrator.integral(x1, x2) / (x2 - x1))



