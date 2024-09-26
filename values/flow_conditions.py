from typing import Dict, Union
from .dimensionless_parameters import *

__all__ = ["FlowtypeAndTemperature"]

class FlowtypeAndTemperature:
    def __init__(self, data: Dict[str, Union[str, float]]):
        self.data = data
        self.re = DimGro.re(data)

    def check_flow_plate(self, flow_type: str, plate_temp: str):
        return self.data['flow_type'] == flow_type and self.data['plate_temp'] == plate_temp

    def isothermal(self):
        if self.re < 5e5:
            return self.check_flow_plate("laminar","isothermal")
        elif self.re > 1e8:
            return self.check_flow_plate("turbulent","isothermal")
        else:
            return self.check_flow_plate("mixed","isothermal")

    def lam_unheated(self):
        if self.re > 1e8:
            return self.check_flow_plate("laminar","unheated")
        else:
            return self.check_flow_plate("turbulent","unheated")
