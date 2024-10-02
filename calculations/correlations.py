import numpy as np
from typing import Dict, Union
from values.flow_conditions import *
__all__ = ["ExternalCorrelations"]

class ExternalCorrelations(FlowtypeAndTemperature):
    def __init__(self, data: Dict[str, Union[float, str]], dim_par_data: Dict[str, float]) -> None:
        super().__init__(data, dim_par_data)

    def _format_sci(self, num):
        return np.round(num,5)

    def t_foam(self):
        result = (self.data['t_fluid'] + self.data['t_sur']) / 2
        return self._format_sci(result)


    def delta_v(self):
        if self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = 5 * self.data['length'] / np.sqrt(self.dim_par_data['re'])
            return self._format_sci(result)
        elif self.flow_type() == "turbulent" or "mixed" and self.data['plate_temp'] == "isothermal":
            result = .37 * self.data['length'] * np.power(self.dim_par_data['re'], -1/5)
            return self._format_sci(result)

    def delta_t(self):
        if self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = self.delta_v() * np.power(self.dim_par_data['pr'],(-1/3))
            return self._format_sci(result)
        elif self.flow_type() == "turbulent" and self.data['plate_temp'] == "isothermal":
            return self.delta_v()

    def loc_cf(self):
        if self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = .664 / np.sqrt(self.dim_par_data['re'])
            return self._format_sci(result)
        elif self.flow_type() == "turbulent" and self.data['plate_temp'] == "isothermal":
            result = .0592 * np.power(self.dim_par_data['re'], -1/5)
            return self._format_sci(result)

    def tau_shear(self):
            result = self.loc_cf() * self.data['rho'] * self.data['v'] ** 2 / 2
            return self._format_sci(result)

    def drag_force(self):
            result = self.tau_shear() / self.data['A']
            return self._format_sci(result)

    def loc_nu(self):
        if self.dim_par_data['pr'] >= .6 and self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3)
            return self._format_sci(result)
        elif self.dim_par_data['pr'] < .05 and 100 <= self.dim_par_data['pe'] and self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = .565 * self.dim_par_data['pe'] ** .5
            return self._format_sci(result)
        elif 100 <= self.dim_par_data['pe'] and self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = (.3387 * self.dim_par_data['re'] ** .5 *
                      self.dim_par_data['pe'] ** (1/3) / (1 + (.0468 / self.dim_par_data['pe']) ** 2/3) ** .25)
            return self._format_sci(result)
        elif .6 <= self.dim_par_data['pr'] <= 60 and self.flow_type() == "turbulent" and self.data['plate_temp'] == "isothermal":
            result = .0296 * self.dim_par_data['re'] ** 4/5 * self.dim_par_data['pr'] ** 1/3
            return self._format_sci(result)
        elif self.flow_type() == "laminar" and self.data['plate_temp'] == "unheated":
            result = (.332 * self.dim_par_data['re'] ** .5 *
                      self.dim_par_data['pr'] ** (1/3) / ((1 - (self.data['xi'] / self.data['length']) ** 3/4) ** 1/3))
            return self._format_sci(result)
        elif self.flow_type() == "turbulent" and self.data['plate_temp'] == "unheated":
            result = (.0296 * self.dim_par_data['re'] ** 4/5 *
                      self.dim_par_data['pr'] ** 1/3 / ((1 - (self.data['xi'] / self.data['length']) ** 9/10) ** 1/9))
            return self._format_sci(result)

    def loc_sh(self):
        if .6 <= self.dim_par_data['sc'] and self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['sc'] ** (1/3)
            return self._format_sci(result)
        elif .6 <= self.dim_par_data['sc'] <= 3000 and self.flow_type() == "turbulent" and self.data['plate_temp'] == "isothermal":
            result = .0296 * self.dim_par_data['re'] ** 4 / 5 * self.dim_par_data['sc'] ** 1 / 3
            return self._format_sci(result)

    def av_cf(self):
        if self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = 1.328 / np.sqrt(self.dim_par_data['re'])
            return self._format_sci(result)
        elif self.flow_type() == "turbulent"  and self.data['plate_temp'] == "isothermal":
            result = .074 * np.power(self.dim_par_data['re'], -1/5) - 2 / self.dim_par_data['re']
            return self._format_sci(result)
        elif self.flow_type() == "mixed" and self.data['plate_temp'] == "isothermal":
            result = .074 * np.power(self.dim_par_data['re'], -1/5) - 2 * 871 / self.dim_par_data['re']
            return self._format_sci(result)


    def av_nu(self):
        if 100 <= self.dim_par_data['pe'] and self.flow_type() == "laminar" and self.data[ 'plate_temp'] == "isothermal":
            result = self.loc_nu() * 2
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['pr'] and self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = .664 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3)
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.flow_type() == "turbulent" and self.data['plate_temp'] == "isothermal":
            result = (.037 * self.dim_par_data['re'] ** 4/5) * self.dim_par_data['pr'] ** 1/3
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.flow_type() == "mixed" and self.data['plate_temp'] == "isothermal":
            result = (.037 * self.dim_par_data['re'] ** 4/5 - 871) * self.dim_par_data['pr'] ** 1/3
            return self._format_sci(result)

    def av_sh(self):
        if .6 <= self.dim_par_data['sc'] and self.flow_type() == "laminar" and self.data['plate_temp'] == "isothermal":
            result = .664 * self.dim_par_data['re'] ** .5 * self.dim_par_data['sc'] ** (1/3)
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['sc'] <= 60 and self.flow_type() == "turbulent" and self.data['plate_temp'] == "isothermal":
            result = (.037 * self.dim_par_data['re'] ** 4 / 5) * self.dim_par_data['sc'] ** 1 / 3
            return self._format_sci(result)

        elif .6 <= self.dim_par_data['sc'] <= 60 and self.flow_type() == "mixed" and self.data['plate_temp'] == "isothermal":
            result = (.037 * self.dim_par_data['re'] ** 4 / 5 - 871) * self.dim_par_data['sc'] ** 1 / 3
            return self._format_sci(result)
