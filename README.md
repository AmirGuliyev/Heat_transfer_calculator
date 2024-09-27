# Heat Transfer Calculator

After agonizing attempts to write another 10 variable long Nusselt or Sherwood number correlations and missing 
another multiplication sign which rendered my equation essentially useless, I've decided it was enough.
No other mechanical and energy engineering student should endure the pain of writing out correlations and
dimensionless parameters that were supposed to be written in specialized software. This is essentially my 
first python project which stems both from my burning passion towards the field of heat&mass transfer and my
disdain towards the requirement of this magical field to write prolonged formulas.

### Variables: 
| Variable      | Variables in Code | Description                                                        | 
|---------------|-------------------|--------------------------------------------------------------------| 
| $h$           | h                 | Heat transfer coefficient, W * m<sup>-1</sup> * K                  | 
| $length$      | length            | Characteristic length, m                                           | 
| $Area$        | Area              | Area, m<sup>2</sup>                                               | 
| $k_s$         | ks                | Solid heat conduction coefficient, W * m<sup>-1</sup> * K<sup>-1</sup> | 
| $h_m$         | hm                | Mass transfer coefficient, m * s<sup>-1</sup>                     | 
| $d_{ab}$      | d_ab              | Binary diffusion coefficient, m<sup>2</sup> * s<sup>-1</sup>      | 
| $d_s$         | sd                | Diameter, m                                                        | 
| $g$           | g                 | Gravitational acceleration constant, m * s<sup>-2</sup>           | 
| $v$           | v                 | Velocity, m * s<sup>-1</sup>                                      | 
| $k$           | k                 | Bulk modulus                                                       | 
| $c_p$         | cp                | Constant pressure specific heat capacity, J * K<sup>-1</sup>     | 
| $t_{sur}$     | t_sur             | Surface temperature, K                                             | 
| $t_{sat}$     | t_sat             | Saturation temperature, K                                          | 
| $t_{fluid}$   | t_fluid           | Fluid temperature, K                                               | 
| $\alpha$      | alpha             | Thermal diffusivity, m<sup>2</sup> / s                            | 
| $t$           | t                 | Time, s                                                            | 
| $\dot{m}$     | m_dot             | Mass flux, kg * s<sup>-1</sup>                                   | 
| $\tau$        | tau               | Surface shear stress, Pa                                          | 
| $\Delta p$    | dp                | Pressure drop, Pa                                                  | 
| $\rho$        | rho               | Density, kg * m<sup>-3</sup>                                     | 
| $\Delta \rho$ | d_rho             | Vapor-liquid density difference, kg * m<sup>-3</sup>             | 
| $u_m$         | um                | Internal flow velocity, m * s<sup>-1</sup>                       | 
| $\beta$       | beta              | Volumetric thermal expansion coefficient, K<sup>-1</sup>         | 
| $f_{lift}$    | f_lift            | Lift force, N                                                      | 
| $h_{fg}$      | h_fg              | Latent specific energy during liquid-vapor phase change, J * kg<sup>-1</sup> | 
| $k_f$         | kf                | Fluid heat conduction coefficient, W * m<sup>-1</sup> * K<sup>-1</sup> | 
| $\nu$         | nu                | Kinematic viscosity, m<sup>2</sup> * s<sup>-1</sup>              | 
| $\mu$         | mu                | Dynamic viscosity, kg * m<sup>-1</sup> * s<sup>-1</sup>          | 
| $\sigma$      | sigma             | Surface tension, N * m<sup>-1</sup>                              | 
| $flow_{type}$ | flow_type         | Flow type                                                          | 
| $int_{flow_{geom}}$ | int_flow_geom | Internal flow geometry                                             | 
| $\delta_v$    | delta_v           | Velocity boundary layer, m                                         | 
| $\delta_t$    | delta_t           | Thermal boundary layer, m                                          | 
| $\delta_c$    | delta_c           | Concentration boundary layer, m                                    |