import numpy as np

__all__ = ["DimGro"]

class DimGro:

    def __init__(self, data):

        self.data = data

    def re(self):
        # Reynolds
        if self.data['flow_geom'] == "external":
            result = self.data['v'] * self.data['length'] / self.data['nu']
            if result < 5e8:
                   return result
            elif 5e8 < result < 1e9:
                    return result
        else:
            match self.data['int_flow_geom']:
                case "circular":
                    result = 4 * self.data['m_dot'] / (np.pi * self.data['d'] * self.data['nu'])
                    return result
                case _:
                    result = self.data['v'] * self.data['d'] / self.data['nu']
                    return result

    def pr(self):
        # Prandtl
        if self.data['cp'] and self.data['mu'] and self.data['kf']:
            result = self.data['cp'] * self.data['mu'] / self.data['kf']
            return result

        elif self.data['nu'] and not self.data['alpha']:
            result = self.data['nu'] / self.data['alpha']
            return result

        elif self.data['delta_v'] and not self.data['delta_t']:
            result = (self.data['delta_v'] / self.data['delta_t']) ** 3
            return result

    def sc(self):
        # Schmidt
        if self.data['nu'] and self.data['d_ab']:
            result = self.data['nu'] / self.data['d_ab']
            return result
        elif self.data['delta_v'] and self.data['delta_c']:
            result = (self.data['delta_v'] / self.data['delta_c']) ** 3
            return result

    def st(self):
        # Stanton
        nusselt = self.nu()
        reynold = self.re()
        prandtl = self.pr()
        if self.data['h'] and self.data['rho'] and self.data['v'] and self.data['cp']:
            result = self.data['h'] * self.data['rho'] * self.data['v'] * self.data['cp']
            return result

        elif nusselt and reynold and prandtl:
            result = nusselt / (reynold * prandtl)
            return result

    def stm(self):
        # Stanton mass
        reynolds = self.re()
        sherwood = self.sh()
        schmidt = self.sc()
        if self.data['hm'] and self.data['v']:
            result = self.data['hm'] / self.data['v']
            return result
        elif sherwood and schmidt and reynolds:
            result = sherwood / (schmidt * reynolds)
            return result

    def pe(self):
        # Pecklet
        reynolds = self.re()
        prandtl = self.pr()
        if self.data['v'] and self.data['length'] and self.data['alpha']:
            result = self.data['v'] * self.data['length'] / self.data['alpha']
            return result
        elif reynolds and prandtl:
            result = reynolds * prandtl
            return result

    def le(self):
        # Lewis
        schmidt = self.sc()
        prandtl = self.pr()
        if self.data['alpha'] is not None and self.data['d_ab'] is not None:
            result = self.data['alpha'] / self.data['d_ab']
            return result

        elif schmidt is not None and prandtl is not None:
            return schmidt / prandtl

        elif self.data['delta_t'] is not None and self.data['delta_c'] is not None:
            result = (self.data['delta_t'] / self.data['delta_c'])**3
            return result

    def nu(self):
        # Nusselt
        reynolds = self.re()
        prandtl = self.pr()

        if self.data['h'] is not None and self.data['length'] is not None and self.data['kf'] is not None:
            result = self.data['h'] * self.data['length'] / self.data['kf']
            return result
        elif reynolds is not None and prandtl is not None:
            result = reynolds * prandtl
            return result

    def bi(self):
        # Biot
        return self.data['h'] * self.data['length'] / self.data['ks']

    def bim(self):
        # Biot mass
        return self.data['hm'] * self.data['length'] / self.data['d_ab']

    def bo(self):
        # Bond
        return self.data['tau'] * self.data['d_rho'] * self.data['length']**2 / self.data['hm']

    def cf(self):
        # Coef. of friction
        return self.data['tau'] * 2 / (self.data['rho'] * self.data['v']**2)

    def cp(self):
        # Coef. of pressure
        return self.data['dp'] * 2 / (self.data['rho'] * self.data['v']**2)

    def cl(self):
        # Coef. of lift
        return 2 * self.data['length'] / (self.data['rho'] * self.data['v']**2 * self.data['f_lift'])

    def ec(self):
        # Eckert
        return self.data['v']**2 / (self.data['cp'] * (self.data['t_sur'] - self.data['t_fluid']))

    def fo(self):
        # Fourier
        return self.data['alpha'] * self.data['t'] / (self.data['length']**2)

    def la(self):
        # Laplace
        return self.data['sigma'] * self.data['rho'] * self.data['length'] / (self.data['mu']**2)

    def fr(self):
        # Froude
        return self.data['v'] / ((self.data['tau'] * self.data['length']) ** 0.5)

    def eu(self):
        # Euler
        return self.data['dp'] * 2 / (self.data['rho'] * self.data['v']**2)

    def fom(self):
        # Fourier mass
        return self.data['d_ab'] * self.data['t'] / self.data['length']**2

    def f(self):
        # Friction factor
        return self.data['dp'] * self.data['d'] * 2 / (self.data['length'] * self.data['rho'] * self.data['um']**2)

    def grl(self):
        # Grashoff
        return self.data['tau'] * self.data['beta'] * (self.data['t_sur'] - self.data['t_fluid']) * self.data['length']**3 / self.data['nu']

    def coj(self):
        # Colburn j factor
        stanton = self.st()
        prandtl = self.pr()
        return stanton * prandtl**(2/3)

    def coj_m(self):
        # Colburn j factor mass
        stantonmass = self.stm()
        schmidt = self.sc()
        return stantonmass * schmidt ** (2/3)

    def ja(self):
        # Jakob
        return self.data['cp'] * (self.data['t_sur'] - self.data['t_sat']) / self.data['h_fg']

    def sh(self):
        # Sherwood
        return self.data['hm'] * self.data['length'] / self.data['d_ab']

    def we(self):
        # Weber
        return self.data['rho'] * self.data['v']**2 * self.data['length'] / self.data['sigma']

    def ra(self):
        # Rayleigh
        return self.data['tau'] * self.data['beta'] * (self.data['t_sur'] - self.data['t_fluid']) * self.data['length']**3 / (self.data['nu'] * self.data['alpha'])

    def ca(self):
        # Cauchy
        return self.data['rho'] * self.data['v']**2 / self.data['k']
