import numpy as np
from values.flow_conditions import *
from values.dimensionless_parameters import *
from typing import Dict, Union


__all__ = ["ExternalCorrelations"]

class ExternalCorrelations(FlowtypeAndTemperature):
    def __init__(self, data, dim_par_data) -> None:
        super().__init__(data, dim_par_data)

    def t_foam(self):
        return (self.data['t_fluid'] + self.data['t_sur']) / 2

    def delta_v(self):
        if self.isothermal() and self.data['flow_type'] == "laminar":
            return 5 * self.data['length'] / np.sqrt(self.dim_par_data['re'])

        elif self.isothermal() and self.data['flow_type'] == "turbulent":
            return .37 * self.data['length'] * np.pow(self.dim_par_data['re'], -1/5)

    def loc_cf(self):
        if self.isothermal() and self.data['flow_type'] == "laminar":
            return .664 / np.sqrt(self.dim_par_data['re'])

        elif self.isothermal() and self.data['flow_type'] == "turbulent":
            return .0592 * np.pow(self.dim_par_data['re'], -1/5)

    def loc_nu(self):
        if self.dim_par_data['pr'] >= .6 and self.isothermal() and self.data['flow_type'] == "laminar":
            return .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3)

        elif self.dim_par_data['pr'] < .05 and 100 <= self.dim_par_data['pe'] and self.isothermal() and self.data['flow_type'] == "laminar":
            return .565 * self.dim_par_data['pe'] ** .5

        elif 100 <= self.dim_par_data['pe'] and self.dim_par_data['pr'] and self.isothermal() and self.data['flow_type'] == "laminar":
            return .3387 * .5 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pe'] ** (1/3) / (1 + (.0468 / self.dim_par_data['pe']) ** 2/3) ** .25

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.isothermal() and self.data['flow_type'] == "turbulent":
            return .0296 * self.dim_par_data['re'] ** 4/5 * self.dim_par_data['pr'] ** 1/3

        elif self.unheated() and self.data['flow_type'] == "laminar":
            return .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3) / ((1 - (self.data['xi'] / self.data['length']) ** 3/4) ** 1/3)

        elif self.unheated() and self.data['flow_type'] == "turbulent":
            return .0296 * self.dim_par_data['re'] ** 4/5 * self.dim_par_data['pr'] ** 1/3 / ((1 - (self.data['xi'] / self.data['length']) ** 9/10) ** 1/9)

    def loc_sh(self):
        if .6 <= self.dim_par_data['sc'] and self.isothermal() and self.data['flow_type'] == "laminar":
            return .332 * self.dim_par_data['re'] ** .5 * self.dim_par_data['sc'] ** (1/3)

        elif .6 <= self.dim_par_data['sc'] <= 3000 and self.isothermal() and self.data['flow_type'] == "turbulent":
            return .0296 * self.dim_par_data['re'] ** 4 / 5 * self.dim_par_data['sc'] ** 1 / 3

    def av_cf(self):
        if self.isothermal() and self.data['flow_type'] == "laminar":
            return 1.328 / np.sqrt(self.dim_par_data['re'])

        elif self.dim_par_data['re'] <= 1e8 and self.isothermal() and self.data['flow_type'] == "mixed":
            return .074 * np.pow(self.dim_par_data['re'], -1/5) - 2 * 871 / self.dim_par_data['re']

        elif self.dim_par_data['re'] <= 1e8 and self.isothermal() and self.data['flow_type'] == "turbulent":
            return .074 * np.pow(self.dim_par_data['re'], -1/5) - 2 / self.dim_par_data['re']

    def av_nu(self):
        if 100 <= self.dim_par_data['pe']  and self.dim_par_data['pr'] and self.isothermal() and self.data['flow_type'] == "laminar":
            return .3387 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pe'] ** (1/3) / (1 + (.0468 / self.dim_par_data['pe']) ** 2/3) ** .25

        elif .6 <= self.dim_par_data['pr'] and self.isothermal() and self.data['flow_type'] == "laminar":
            return .664 * self.dim_par_data['re'] ** .5 * self.dim_par_data['pr'] ** (1/3)

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.isothermal() and self.data['flow_type'] == "turbulent":
            # CRITICAL REYNOLDS NUMBER IS 5e5
            return (.037 * self.dim_par_data['re'] ** 4/5) * self.dim_par_data['pr'] ** 1/3

        elif .6 <= self.dim_par_data['pr'] <= 60 and self.isothermal() and self.data['flow_type'] == "mixed":
            # CRITICAL REYNOLDS NUMBER IS 5e5
            return (.037 * self.dim_par_data['re'] ** 4/5 - 871) * self.dim_par_data['pr'] ** 1/3

    def av_sh(self):
        if .6 <= self.dim_par_data['sc'] and self.isothermal() and self.data['flow_type'] == "laminar":
            return .664 * self.dim_par_data['re'] ** .5 * self.dim_par_data['sc'] ** (1/3)

        elif .6 <= self.dim_par_data['sc'] <= 60 and self.isothermal() and self.data['flow_type'] == "turbulent":
            # CRITICAL REYNOLDS NUMBER IS 5e5
            return (.037 * self.dim_par_data['re'] ** 4 / 5) * self.dim_par_data['sc'] ** 1 / 3

        elif .6 <= self.dim_par_data['sc'] <= 60  and 5e5 <= self.dim_par_data['re'] <= 1e8 and self.isothermal() and self.data['flow_type'] == "mixed":
            # CRITICAL REYNOLDS NUMBER IS 5e5
            return (.037 * self.dim_par_data['re'] ** 4 / 5 - 871) * self.dim_par_data['sc'] ** 1 / 3

