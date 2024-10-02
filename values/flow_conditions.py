from typing import Dict, Union

__all__ = ["FlowtypeAndTemperature"]


class FlowtypeAndTemperature:
    def __init__(self, data: Dict[str, Union[str, float]], dim_par_data: Dict[str,float]):
        self.data = data
        self.dim_par_data = dim_par_data

    def flow_type(self):
        if self.dim_par_data['re'] < 5e5:
            return "laminar"
        elif self.dim_par_data['re'] > 1e8:
            return "turbulent"
        else:
            return "mixed"
