
import numpy as np
import sys
import pandas as pd
from matplotlib import pyplot as plt
from scipy import interpolate

sys.path.append("./../")
from utility_constants import us_to_ns, GPa_to_Mbar, plot_colors

def filter(array):
    for i in np.arange(len(array)):
        if array[i] < 0:
            array[i] = 0

# use LaTeX fonts for figures and set font size of tick labels
plt.rc('text', usetex=True)
plt.rc('font', family='serif', weight='bold')
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20

#base dimensions of the figures in inches
width = 8.5
height = 7

#desired set of units for all of the plots below
units = "default"

#output directory
output_directory = "./"

LiF = np.loadtxt("./../S7271v3_LiF_principal_isentrope.dat",skiprows=1)
LiF_pressure = LiF[:,2]
LiF_up = LiF[:,5]
f = interpolate.interp1d(LiF_up,LiF_pressure)

#plot the velocities
plt.figure()
directories = ["./../Simulation_outputs/Brown_shot60/","./../Simulation_outputs/Brown_shot60_200um/",
               "./../Simulation_outputs/Brown_shot60_250um/","./../Simulation_outputs/Brown_shot60_300um/","./../Simulation_outputs/Brown_shot60_350um/"]
start_indices = [0,0,0,0,0]
stop_indices = [15000,18000,14000,18000,18000]
time_shifts = [-100.0,-80.0,-60.0,-40.0,-20.0]
linestyles = ["solid","dashed","dotted","dashdot","solid"]
legend_labels = [r"Shot 3 (165 $\mu$m)",r"200 $\mu$m",r"250 $\mu$m",r"300 $\mu$m",r"350 $\mu$m"]
num_skiprows = 2
for i,directory in enumerate(directories):
    time = np.loadtxt(directory + "p.target_back.dat",skiprows=num_skiprows)[start_indices[i]:stop_indices[i],0]*us_to_ns + time_shifts[i]
    pressure = np.loadtxt(directory + "p.target_back.dat",skiprows=num_skiprows)[start_indices[i]:stop_indices[i],1]/GPa_to_Mbar
    if (directory == "./../Simulation_outputs/Brown_shot60_350um/"):
        plt.plot(time,pressure,color=plot_colors[3][0],linestyle=linestyles[i],label=legend_labels[i],linewidth=3)
    else:
        plt.plot(time,pressure,color=plot_colors[3][0],linestyle=linestyles[i],label=legend_labels[i])
plt.legend(legend_labels,prop={"size":16},frameon=False,loc="best")
plt.xlim(300,620.0)
plt.ylim(0.0,25)
plt.xlabel("Time (ns)",fontsize=24)
plt.ylabel("Pressure (GPa)",fontsize=24)
scale_width = 1.0
scale_height = 1.0
plt.gcf().set_size_inches(width*scale_width,height*scale_height)
file = output_directory + "plot_shot60_pressure.pdf"
plt.savefig(file)
