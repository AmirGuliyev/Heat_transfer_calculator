import HeatCalculation as Hsimport DimParimport Correlations as Corimport matplotlib.pyplot as pltimport numpy as npdata = {'length': 1,'A':1, 'd': .1, 't': 60,        'g': 9.81, 'v': 10, 'cp': 1000,'um': 2, 'f_lift': .1, 'm_dot':1, 'dp':5000,        't_sur': 300, 't_sat': 350, 't_f': 390,        'alpha': 1e-4,'beta': 1e-4, 'tau': .02, 'rho':1.225, 'xi': 1,'nu': 1e-6, 'mu': 1e-3, 'sigma': .072,        'd_rho': 0.02, 'h_fg': 2260, 'k': 1e3,        'flow_geom': "external", 'int_flow_geom': "circular", 'flow_type': 'laminar','plate_temp': 'isothermal',        'delta_t':1, 'delta_v':1, 'delta_c':1,        'kf': .064,'ks':200, 'h':10,'hm': .02, 'd_ab': .0001}dim_gro_instance = DimPar.DimGro(data)dim_par_data = {'re': dim_gro_instance.re(numeric=True),              'pr': dim_gro_instance.pr(numeric=True),              'sc': dim_gro_instance.sc(numeric=True),              'le': dim_gro_instance.le(numeric=True),              'nu': dim_gro_instance.nu(numeric=True),              'pe': dim_gro_instance.pe(numeric=True),              'st': dim_gro_instance.st(numeric=True),              'stm': dim_gro_instance.stm(numeric=True),              'bi': dim_gro_instance.bi(),              'bim': dim_gro_instance.bim(),              'bo': dim_gro_instance.bo(),              'cf': dim_gro_instance.cf(),              'cp': dim_gro_instance.cp(),              'cl': dim_gro_instance.cl(),              'ec': dim_gro_instance.ec(),              'fo': dim_gro_instance.fo(),              'la': dim_gro_instance.la(),              'fr': dim_gro_instance.fr(),              'eu': dim_gro_instance.eu(),              'fom': dim_gro_instance.fom(),              'f': dim_gro_instance.f(),              'grl': dim_gro_instance.grl(),              'coj': dim_gro_instance.coj(),              'coj_m': dim_gro_instance.coj_m(),              'ja': dim_gro_instance.ja(),              'wh': dim_gro_instance.sh(),              'we': dim_gro_instance.we(),              'ra': dim_gro_instance.ra(),              'ca': dim_gro_instance.ca()}heat_calc = Hs.Heat(data,dim_par_data)print(heat_calc.total_heat_transfer_rate())#Is amogus here???