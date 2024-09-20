from logging import exception

import numpy as np
from CalCop import Integrator as Inte
import Means as Me

"""class Distributions(Inte, Me):
    def __init__(self, x):
        super().__init__()
        self.x = x
"""


def prime_num(numrange: list) -> list:
    j = 2
    while j <= len(numrange):
        for index, value in enumerate(numrange):
            if value % j == 0 and value != j:
                numrange[index] = 0
        j += 1
    numrange = [i for i in numrange if i != 0]
    return numrange