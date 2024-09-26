from calculations.correlations import ExternalCorrelations

__all__ = ["Heat"]

class Heat(ExternalCorrelations):
    def __init__(self, data, dim_par_data):
        super().__init__(data, dim_par_data)

    def av_heat_trans_coef(self):

        return ExternalCorrelations.av_nu(self) * self.data['kf'] / self.data['length']

    def total_heat_transfer_flux(self):

        return self.av_heat_trans_coef() * (self.data['t_f'] - self.data['t_sur'])

    def total_heat_transfer_rate(self):

        return self.total_heat_transfer_flux() * self.data['A']
