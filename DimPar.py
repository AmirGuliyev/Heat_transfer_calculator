"""     self.data.['h'] = h             # Heat transfer coefficient, W / m^2 * K
        self.data['length'] = length    # Characteristic length, m
        self.data['A'] = Area           # Area, m^2
        self.data['ks'] = ks            # Solid heat conduction coefficient,
        self.data['hm'] = hm            # Mass transfer coefficient,
        self.data['d_ab'] = d_ab        # Binary diffusion coefficient,
        self.data['d'] = d              # Diameter, m
        self.data['tau'] = g            # Gravitational acceleration constant, m^2 / s
        self.data['v'] = v              # Velocity, m / s
        self.data['k'] = k              # Bulk modulus,
        self.data['cp'] = cp            # Const pressure specific heat capacity, J / K
        self.data['t_sur'] = t_sur      # Surface temperature, K
        self.data['t_sat'] = t_sat      # Saturation temperature, K
        self.data['t_fluid'] = t_fluid  # Fluid temperature, K
        self.data['alpha'] = alpha      # Thermal diffusivity
        self.data['t'] = t              # Time, s
        self.data['m_dot'] = m_dot      # Mass flux, kg / s
        self.data['tau'] = tau          # Surface shear stress
        self.data['dp'] = dp            # Pressure Drop,
        self.data['rho'] = rho          # Density
        self.data['d_rho'] = d_rho      # Vapor-liquid density difference
        self.data['um'] = um            # Internal flow velocity
        self.data['beta'] = beta        # Volumetric thermal expansion coefficient
        self.data.f_lift = f_lift                   # Lift force
        self.data['h_fg'] = h_fg                    # Latent energy during liquid-vapor phase change
        self.data['kf'] = kf                        # Fluid heat conduction coefficient
        self.data['nu'] = nu                        # Kinematic viscosity
        self.data['mu'] = mu                        # Dynamic viscosity
        self.data['sigma'] = sigma                  # Surface tension
        self.data['flow_type'] = flow_type          # flow_type
        self.data['int_flow_geom'] = int_flow_geom  # Internal flow geometry
        self.data['delta_v'] = delta_v              # Velocity boundary layer
        self.data['delta_t'] = delta_t              # Thermal boundary layer
        self.data['delta_c'] = delta_c              # Concentration boundary layer"""

import numpy as np


class DimGro:

    def __init__(self, data):

        self.data = data

    def re(self, numeric=False):

        # Reynolds

        if self.data['flow_geom'] == "external":

            result = self.data['v'] * self.data['length'] / self.data['nu']

            if result < 5e8:

                if numeric:

                    return result

                return f"For external flow Re number is {result}. Flow is laminar"

            elif 5e8 < result < 1e9:

                if numeric:

                    return result

                return f"For external flow Re number is {result}. Flow is mixed"

        else:

            match self.data['int_flow_geom']:

                case "circular":

                    result = 4 * self.data['m_dot'] / (np.pi * self.data['d'] * self.data['nu'])

                    if numeric:

                        return result

                    return (f"For internal flow of circular geometry Re number is "
                            f"{result}")
                case _:

                    result = self.data['v'] * self.data['d'] / self.data['nu']

                    if numeric:

                        return result

                    return f"For internal flow Re number is {result}"

    def pr(self, numeric=False):

        # Prandtl

        if self.data['cp'] is not None and self.data['mu'] is not None and self.data['kf'] is not None:
            result = self.data['cp'] * self.data['mu'] / self.data['kf']

            if numeric:

                return result

            return (f"Through specific heat, dynamic viscosity and fluid thermal conductivity "
                    f"Pr number is {result}")

        elif self.data['nu'] is not None and self.data['alpha'] is None:

            result = self.data['nu'] / self.data['alpha']

            if numeric:

                return result

            return (f"Through kinematic viscosity and thermal diffusivity "
                    f"Pr number is {result}")

        elif self.data['delta_v'] is not None and self.data['delta_t'] is None:

            result = (self.data['delta_v'] / self.data['delta_t']) ** 3

            if numeric:

                return result

            return (f"Through velocity boundary layer and thermal boundary layer "
                    f"Pr number is {result}")

    def sc(self, numeric = False):

        # Schmidt

        if self.data['nu'] is not None and self.data['d_ab'] is not None:

            result = self.data['nu'] / self.data['d_ab']

            if numeric:

                return result

            return (f"Through kinematic viscosity and binary diffusion coefficient "
                    f"Sc number is {result}")

        elif self.data['delta_v'] is not None and self.data['delta_c'] is None:

            result = (self.data['delta_v'] / self.data['delta_c']) ** 3

            if numeric:

                return result

            return (f"Through velocity boundary layer and thermal boundary layer "
                    f"Sc number is {result}")

    def st(self, numeric=False):

        # Stanton

        nusselt = self.nu()

        reynold = self.re()

        prandtl = self.pr()

        if self.data['h'] is not None and self.data['rho'] is not None and self.data['v'] is not None and self.data['cp'] is not None:

            result = self.data['h'] * self.data['rho'] * self.data['v'] * self.data['cp']

            if numeric:

                return result

            return (f"Through heat transfer coefficient, fluid density, fluid velocity and constant pressure "
                    f"specific heat capacity St number is {self.data['h'] / (self.data['rho'] * self.data['v'] * self.data['cp'])})")

        elif nusselt is not None and reynold is not None and prandtl is not None:

            result = nusselt / (reynold * prandtl)

            if numeric:

                return result

            return f"Through Nu, Re and Pr dimensionless parameters St number is {nusselt / (reynold * prandtl)}"

    def stm(self, numeric=False):

        # Stanton mass

        reynolds = self.re()

        sherwood = self.sh()

        schmidt = self.sc()

        if self.data['hm'] is not None and self.data['v'] is not None:

            result = self.data['hm'] / self.data['v']

            if numeric:

                return result

            return result

        elif sherwood is not None and schmidt is not None and reynolds is not None:

            result = sherwood / (schmidt * reynolds)

            if numeric:

                return result

            return f"Through Sh, Re and Sc dimensionless parameters Stanton(mass) number is {sherwood / (reynolds * schmidt)}"

    def pe(self, numeric = False):

        # Pecklet

        reynolds = self.re()

        prandtl = self.pr()

        if self.data['v'] is not None and self.data['length'] is not None and self.data['alpha'] is not None:

            result = self.data['v'] * self.data['length'] / self.data['alpha']

            if numeric:

                return result

            return f"Through velocity, length and thermal diffusivity Pe number is {self.data['v'] * self.data['length'] / self.data['alpha']}"

        elif reynolds is not None and prandtl is not None:

            result = reynolds * prandtl

            if numeric:

                return result

            return f"Through Re and Pr dimensionless parameters, Pe number is {reynolds * prandtl}"

    def le(self, numeric = False):

        # Lewis

        schmidt = self.sc()

        prandtl = self.pr()

        if self.data['alpha'] is not None and self.data['d_ab'] is not None:

            result = self.data['alpha'] / self.data['d_ab']

            if numeric:

                return result

            return f"Through thermal diffusivity and binary diffusion coefficient Le number is {self.data['alpha'] / self.data['d_ab']}"

        elif schmidt is not None and prandtl is not None:

            if numeric:

                return schmidt / prandtl

            return f"Through Sc and Pr dimensionless parameters Le number is {schmidt / prandtl}"

        elif self.data['delta_t'] is not None and self.data['delta_c'] is not None:

            result = (self.data['delta_t'] / self.data['delta_c'])**3

            if numeric:

                return result

            return (f"Through thermal boundary layer and concentration boundary layer "
                    
                    f"Pr number is {(self.data['delta_t'] / self.data['delta_c'])**3}")

    def nu(self, numeric=False):

        # Nusselt

        reynolds = self.re()

        prandtl = self.pr()

        if self.data['h'] is not None and self.data['length'] is not None and self.data['kf'] is not None:

            result = self.data['h'] * self.data['length'] / self.data['kf']

            if numeric:

                return result

            return (f"Through heat convection coefficient, length and fluid's thermal conduction "
                    f"Nu number is {self.data['h'] * self.data['length'] / self.data['kf']}")

        elif reynolds is not None and prandtl is not None:

            result = reynolds * prandtl

            if numeric:

                return result

            return f"Through Re and Pr dimensionless parameters, Nu number is {result}"

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
        stanton = self.st(numeric=True)
        prandtl = self.pr(numeric=True)
        return stanton * prandtl**(2/3)

    def coj_m(self):
        # Colburn j factor mass
        stantonmass = self.stm(numeric=True)
        schmidt = self.sc(numeric=True)
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
