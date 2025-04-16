
import numpy as np
import sys
import pandas as pd
from matplotlib import pyplot as plt

sys.path.append("./../")
from utility_constants import GPa_to_Mbar, plot_colors

# use LaTeX fonts for figures and set font size of tick labels
plt.rc('text', usetex=True)
plt.rc('font', family='serif', weight='bold')
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20

#color scheme and plot markers to use for the different phases in the phase diagrams
def color_scheme(phase_label):
    if phase_label == "I":
        plot_color = plot_colors[2][0]  #red
    elif phase_labels[i] == "II":
        plot_color = plot_colors[3][0]  #green
    elif phase_labels[i] == "III":
        plot_color = plot_colors[4][0]  #orange
    elif phase_labels[i] == "fluid":
        plot_color = plot_colors[1][0]  #blue
    return plot_color
plot_marker = "s"

#base dimensions of the figures in inches
width = 8.5
height = 7

#desired set of units for all of the plots below
units = "default"

#output directory
output_directory = "./"

plt.figure()
#superimpose the loading paths onto the phase diagram
directories = ["./../Simulation_outputs/Brown_shot53/","./../Simulation_outputs/Brown_shot53_equil/","./../Simulation_outputs/Brown_shot53_liqonly/"]
stop_indices = [12200,12200,12200]
linestyles = ["solid","dashed","dotted"]
legend_labels = ["Nonequilibrium (Samsa CNT-based kinetics)","Equilibrium (No kinetic delay)","Liquid only (Infinitely slow kinetics)"]
num_skiprows = 2
for i,directory in enumerate(directories):
    T = np.loadtxt(directory + "Tliq.target_bin.dat",skiprows=num_skiprows)[:stop_indices[i],1]
    P = np.loadtxt(directory + "p.target_bin.dat",skiprows=num_skiprows)[:stop_indices[i],1]/GPa_to_Mbar
    plt.plot(P,T,color="white",linestyle=linestyles[i],label=legend_labels[i])
plt.xlim(0.0,30.0)
plt.ylim(250.0,1000.0)
plt.xlabel("Pressure (GPa)",fontsize=24)
plt.ylabel("Temperature (K)",fontsize=24)

#plot the phase diagram at relatively low temperatures and pressures (includes phases I, II, III, and fluid)
file = "phase_diagram_L311_Ga_I_II_III_fluid_T_max=1p0000e+03_K_P_max=3p0000e+01_GPa.dat"
df = pd.read_fwf(file)
temperature = df["T (K)"]
pressure = df["P (GPa)"]
phase_labels = df["Phase"]
num_T = len(temperature)
for i in np.arange(num_T):
    plt.plot(pressure[i],temperature[i],plot_marker,color=color_scheme(phase_labels[i]))
scale_width = 1.0
scale_height = 1.0
plt.gcf().set_size_inches(width*scale_width,height*scale_height)
file = output_directory + file.replace('.dat','') + ".pdf"

#superimpose the loading paths onto the phase diagram
directories = ["./../Simulation_outputs/Brown_shot53/","./../Simulation_outputs/Brown_shot53_equil/","./../Simulation_outputs/Brown_shot53_liqonly/"]
stop_indices = [12200,12200,12200]
linestyles = ["solid","dashed","dotted"]
legend_labels = ["Nonequilibrium (Samsa CNT-based kinetics)","Equilibrium (No kinetic delay)","No solidification (Infinitely slow kinetics)"]
num_skiprows = 2
for i,directory in enumerate(directories):
    T = np.loadtxt(directory + "Tliq.target_bin.dat",skiprows=num_skiprows)[:stop_indices[i],1]
    P = np.loadtxt(directory + "p.target_bin.dat",skiprows=num_skiprows)[:stop_indices[i],1]/GPa_to_Mbar
    plt.plot(P,T,color="white",linestyle=linestyles[i],label=legend_labels[i])
plt.legend(legend_labels,prop={"size":18},frameon=False,loc="upper left")
ax = plt.gca()
ax.annotate("",xytext=(0.73,0.46),xy=(0.78,0.36),xycoords='axes fraction',arrowprops=dict(arrowstyle="->"))
plt.annotate(r'$P_\mathrm{trans}$', xy=(0.68,0.48), xycoords='axes fraction',color="black",fontsize=24)
ax.annotate("",xytext=(0.14,0.27),xy=(0.19,0.17),xycoords='axes fraction',arrowprops=dict(arrowstyle="->"))
plt.annotate(r'$P_\mathrm{melt}$', xy=(0.09,0.29), xycoords='axes fraction',color="black",fontsize=24)
plt.annotate('Liquid',xy=(0.3,0.65),xycoords='axes fraction',color="black",fontsize=24)
plt.annotate('Ga-III',xy=(0.7,0.22),xycoords='axes fraction',color="black",fontsize=24)
plt.savefig(file)