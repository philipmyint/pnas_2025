
#this file specifies some useful physical constants, conversion factors, and plotting options 

#gas constant in kJ/mol/K
R = 8.314462618e-3

#Avogadro's number
NA = 6.02214076e+23

#Boltzmann constant in J/K
kB = R/NA*1000.0

#Dirac constant in J s
hbar = 1.054571817e-34

#length conversion factor(s)
km_to_m = 1.0e3
cm_to_nm = 1.0e7
cm_to_m = 1.0e-2
cm_to_bohr = 188972598.85789
cm_to_angstrom = 1.0e8

#pressure conversion factor(s) 
GPa_to_Mbar = 1.0e-2
GPa_to_bar = 1.0e4
GPa_to_Pa = 1.0e9
GPa_to_erg_per_cm3 = 1.0e10
GPa_to_kbar = 1.0e1
GPa_to_atm = GPa_to_bar/1.01325
GPa_to_torr = GPa_to_bar*760.0

#energy conversion factor(s)
kJ_to_erg = 1.0e10
kJ_to_J = 1.0e3
kJ_to_mJ = 1.0e6
kJ_to_Ha = 2.2937104486906e20
kJ_to_eV = 6.2415064799632e21
kJ_per_mol_to_K_per_particle = kJ_to_J/NA/kB
J_to_mJ = kJ_to_J

#volume conversion factor(s)
cm3_per_mol_to_angstrom3_per_particle = (cm_to_angstrom**3.0)/NA

#mass conversion factor(s)
kg_to_g = 1.0e3

#time conversion factor(s)
s_to_ns = 1.0e9
us_to_ns = 1.0e3
us_to_s = 1.0e-6
s_to_atomic_time = kJ_to_J/(kJ_to_Ha*hbar)

#velocity conversion factor(s)
km_per_s_to_cm_per_us = km_to_m/cm_to_m*us_to_s
km_per_s_to_m_per_s = km_to_m

#temperature conversion factor(s)
K_to_eV = 1.160451812e-4
K_to_keV = 1.160451812e-7
K_to_MeV = 1.160451812e-10

#if the mole fraction of a particular component is below this minimum, we assume that it is not present
#in the mixture (in order to prevent numerical divergences when we evaluate the logarithm of its mole fraction)
z_min = 1.0e-10

#RGB values for different colors
plot_colors = [((0.0,0.0,0.0),"black"),((31.0/255.0,119.0/255.0,180.0/255.0),"blue"),\
    ((214.0/255.0,39.0/255.0,40.0/255.0),"red"),((44.0/255.0,160.0/255.0,44.0/255.0),"green"),\
    ((255.0/255.0,127.0/255.0,14.0/255.0),"orange"),((238.0/255.0,0.0/255.0,238.0/255.0),"magenta"),\
    ((140.0/255.0,86.0/255.0,75.0/255.0),"brown"),((23.0/255.0,190.0/255.0,207.0/255.0),"cyan"),\
    ((255.0/255.0,215.0/255.0,0.0/255.0),"gold"),((148.0/255.0,103.0/255.0,189.0/255.0),"violet"),\
    ((128.0/255.0,128.0/255.0,0.0/255.0),"olive"),((220.0/255.0,20.0/255.0,60.0/255.0),"crimson"),\
    ((255.0/255.0,174.0/255.0,185.0/255.0),"pink"),((189.0/255.0,252.0/255.0,201.0/255.0),"mint"),\
    ((192.0/255.0,192.0/255.0,192.0/255.0),"silver")]

#tuples for different line styles in plots
linestyle_tuple = [
    ('solid',                 (0, ())),
    ('dashed',                (0, (5, 5))),
    ('dashdot',               (0, (3, 5, 1, 5))),
    ('dotted',                (0, (1, 1))),
    ('loosely dotted',        (0, (1, 10))),
    ('densely dotted',        (0, (1, 1))),
    ('loosely dashed',        (0, (5, 10))),
    ('densely dashed',        (0, (5, 1))),
    ('loosely dashdotted',    (0, (3, 10, 1, 10))),
    ('densely dashdotted',    (0, (3, 1, 1, 1))),
    ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
    ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
    ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]