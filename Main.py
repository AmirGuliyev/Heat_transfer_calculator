import CalCop as Cc
import DimPar
import numpy as np
import Means as Mm
import Dist
import Correlations as Cor

data = {'h':10, 'length': 1, 'd': .1, 'ks':200, 'hm': .02, 'dab': .0001, 'g': 9.81, 'v': 10, 'cp': 1000,
        't_sur': 300, 't_sat': 350, 'tf': 290, 'alpha': 1e-4, 't': 60, 'tau': .02, 'dp':5000, 'rho':1.225,
        'd_rho': 0.02, 'um': 2, 'xi': 1, 'beta': 1e-4, 'hfg': 2260, 'kf': .064, 'nu': 1e-6, 'mu': 1e-3, 'sigma': .072,
        'f_lift': .1, 'k': 1e3, 'flow_geom': "external", 'int_flow_geom': "circular", 'flowtype': 'laminar','platetemp': 'isothermal', 'm_dot':1, 'deltat':1,
        'delta_v':1, 'delta_c':1}

dim_gro_instance = DimPar.DimGro(data)

dimpardata = {'re': dim_gro_instance.re(numeric=True),'pr': dim_gro_instance.pr(numeric=True),'sc': dim_gro_instance.sc(numeric=True),
              'bi': dim_gro_instance.bi(),'bim': dim_gro_instance.bim(),'bo': dim_gro_instance.bo(),
              'cf': dim_gro_instance.cf(),'cp': dim_gro_instance.cp(),'cl': dim_gro_instance.cl(),
              'ec': dim_gro_instance.ec(),'fo': dim_gro_instance.fo(),'la': dim_gro_instance.la(),
              'fr': dim_gro_instance.fr(),'eu': dim_gro_instance.eu(),'fom': dim_gro_instance.fom(),
              'f': dim_gro_instance.f(),'grl': dim_gro_instance.grl(),'st': dim_gro_instance.st(numeric=True),
              'stm': dim_gro_instance.stm(numeric=True),'coj': dim_gro_instance.coj(),'cojm': dim_gro_instance.cojm(),
              'ja': dim_gro_instance.ja(),'le': dim_gro_instance.le(numeric=True),'nu': dim_gro_instance.nu(numeric=True),
              'pe': dim_gro_instance.pe(numeric=True),'wh': dim_gro_instance.sh(),'we': dim_gro_instance.we(),
              'ra': dim_gro_instance.ra(),'ca': dim_gro_instance.ca()}

inst = Cor.ExternalCorrelations(data, dimpardata)

print(inst.deltav())