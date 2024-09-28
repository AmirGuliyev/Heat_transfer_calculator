import numpy as np
from typing import Dict, Union
from values.flow_conditions import *
__all__ = ["ExternalCorrelations"]

class ExternalCorrelations(FlowtypeAndTemperature):
    def __init__(self, data: Dict[str, Union[float, str]], dim_par_data: Dict[str, float]) -> None:
        super().__init__(data, dim_par_data)

    def _format_sci(self, num):
        return np.array2string(num, formatter={'float_kind': lambda x: f"{x:.2e}"})

    def t_foam(self):
        result = (self.data['t_fluid'] + self.data['t_sur']) / 2
        return self._format_sci(result)

    def delta_v(self):
        if self.isothermal() and self.data['flow_type'] == "laminar":
            result = 5 * self.data['length'] / np.sqrt(self.dim_par_data['re'])
            return self._format_sci(result)
        elif self.isothermal() and self.data['flow_type'] == "turbulent":
            result = .37 * self.data['length'] * np.pow(self.dim_par_data['re'], -1/5)
            return self._format_sci(result)

    def loc_cf(self):
        if self.isothermal() and self.data['flow_type'] == "laminar":
            result = .664 / np.sqrt(self.dim_par_data['re'])
            return self._format_sci(result)
        elif self.isothermal() and self.data['flow_type'] == "turbulent":
            result = .0592 * np.pow(self.dim_par_data['re'], -1/5)
            return self._format_sci(result)

    def loc_nu(self):
        if self.dim_par_data['pr'] >= .6 and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3)
            return self._format_sci(result)
        elif self.dim_par_data['pr'] < .05 and 100 <= self.dim_par_data['pe'] and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .565 * self.dim_par_data['pe'] ** .5
            return self._format_sci(result)
        elif 100 <= self.dim_par_data['pe'] and self.dim_par_data['pr'] and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .3387 * .5 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pe'] ** (1/3) / (1 + (.0468 / self.dim_par_data['pe']) ** 2/3) ** .25
            return self._format_sci(result)
        elif .6 <= self.dim_par_data['pr'] <= 60 and self.isothermal() and self.data['flow_type'] == "turbulent":
            result = .0296 * self.dim_par_data['re'] ** 4/5 * self.dim_par_data['pr'] ** 1/3
            return self._format_sci(result)
        elif self.unheated() and self.data['flow_type'] == "laminar":
            result = .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3) / ((1 - (self.data['xi'] / self.data['length']) ** 3/4) ** 1/3)
            return self._format_sci(result)
        elif self.unheated() and self.data['flow_type'] == "turbulent":
            result = .0296 * self.dim_par_data['re'] ** 4/5 * self.dim_par_data['pr'] ** 1/3 / ((1 - (self.data['xi'] / self.data['length']) ** 9/10) ** 1/9)
            return self._format_sci(result)

    def loc_sh(self):
        if .6 <= self.dim_par_data['sc'] and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['sc'] ** (1/3)
            return self._format_sci(result)
        elif .6 <= self.dim_par_data['sc'] <= 3000 and self.isothermal() and self.data['flow_type'] == "turbulent":
            result = .0296 * self.dim_par_data['re'] ** 4 / 5 * self.dim_par_data['sc'] ** 1 / 3
            return self._format_sci(result)

    def av_cf(self):
        if self.isothermal() and self.data['flow_type'] == "laminar":
            result = 1.328 / np.sqrt(self.dim_par_data['re'])
            return self._format_sci(result)
        elif self.dim_par_data['re'] <= 1e8 and self.isothermal() and self.data['flow_type'] == "mixed":
            result = .074 * np.pow(self.dim_par_data['re'], -1/5) - 2 * 871 / self.dim_par_data['re']
            return self._format_sci(result)
        elif self.dim_par_data['re'] <= 1e8 and self.isothermal() and self.data['flow_type'] == "turbulent":
            result = .074 * np.pow(self.dim_par_data['re'], -1/5) - 2 / self.dim_par_data['re']
            return self._format_sci(result)

    def av_nu(self):
        if 100 <= self.dim_par_data['pe'] and self.dim_par_data['pr'] and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .3387 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pe'] ** (1/3) / (1 + (.0468 / self.dim_par_data['pe']) ** 2/3) ** .25
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['pr'] and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .664 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3)
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.isothermal() and self.data['flow_type'] == "turbulent":
            result = (.037 * self.dim_par_data['re'] ** 4/5) * self.dim_par_data['pr'] ** 1/3
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.isothermal() and self.data['flow_type'] == "mixed":
            result = (.037 * self.dim_par_data['re'] ** 4/5 - 871) * self.dim_par_data['pr'] ** 1/3
            return self._format_sci(result)

    def av_sh(self):
        if .6 <= self.dim_par_data['sc'] and self.isothermal() and self.data['flow_type'] == "laminar":
            result = .664 * self.dim_par_data['re'] ** .5 * self.dim_par_data['sc'] ** (1/3)
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['sc'] <= 60 and self.isothermal() and self.data['flow_type'] == "turbulent":
            result = (.037 * self.dim_par_data['re'] ** 4 / 5) * self.dim_par_data['sc'] ** 1 / 3
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['sc'] <= 60 and 5e5 <= self.dim_par_data['re'] <= 1e8 and self.isothermal() and self.data['flow_type'] == "mixed":
            result = (.037 * self.dim_par_data['re'] ** 4 / 5 - 871) * self.dim_par_data['sc'] ** 1 / 3
            return self._format_sci(result)
