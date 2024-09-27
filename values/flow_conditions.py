from typing import Dict, Union
from values.dimensionless_parameters import *

__all__ = ["FlowtypeAndTemperature"]

class FlowtypeAndTemperature:
    def __init__(self, data: Dict[str, Union[str, float]], dim_par_data: Dict[str,float]):
        self.data = data
        self.dim_par_data = dim_par_data

    def check_flow_plate(self, flow_type: str, plate_temp: str):
        return self.data['flow_type'] == flow_type and self.data['plate_temp'] == plate_temp

    def isothermal(self):
        if self.dim_par_data['re'] < 5e5:
            return self.check_flow_plate("laminar","isothermal")
        elif self.dim_par_data['re'] > 1e8:
            return self.check_flow_plate("turbulent","isothermal")
        else:
            return self.check_flow_plate("mixed","isothermal")

    def unheated(self):
        if self.dim_par_data['re'] > 1e8:
            return self.check_flow_plate("laminar","unheated")
        else:
            return self.check_flow_plate("turbulent","unheated")
