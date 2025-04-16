
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
directories = ["./../Simulation_outputs/Brown_shot60/","./../Simulation_outputs/Brown_shot61/","./../Simulation_outputs/Brown_shot63/",
               "./../Simulation_outputs/Brown_shot6407/","./../Simulation_outputs/Brown_shot6423/"]
start_indices = [7300,7000,6600,6600,0]
stop_indices = [15000,18000,18000,15000,17000]
time_shifts = [-100.0,-80.0,-60.0,-450.0,-380.0]
linestyles = ["solid"]*len(directories)
colors = [plot_colors[3][0],plot_colors[10][0],plot_colors[13][0],plot_colors[4][0],"orange"]
legend_labels = [r"Shot 3 (165 $\mu$m)",r"Shot 3b (250 $\mu$m)",r"Shot 3c (260 $\mu$m)",r"Shot 4 (52 $\mu$m)",r"Shot 4b (100 $\mu$m)"]
linewidths = [1]*len(directories)
num_skiprows = 2
for i,directory in enumerate(directories):
    time = np.loadtxt(directory + "p.target_back.dat",skiprows=num_skiprows)[start_indices[i]:stop_indices[i],0]*us_to_ns + time_shifts[i]
    pressure = np.loadtxt(directory + "p.target_back.dat",skiprows=num_skiprows)[start_indices[i]:stop_indices[i],1]/GPa_to_Mbar
    plt.plot(time,pressure,color=colors[i],linestyle=linestyles[i],label=legend_labels[i],linewidth=linewidths[i])
plt.legend(legend_labels,prop={"size":16},frameon=False,loc="best")
#add experimental data
directory = "./../Simulation_outputs/EXPERIMENT_gallium/"
files = [directory+"shot60.Ga.xdot.dat",directory+"shot61.Ga.xdot.dat",directory+"shot63.Ga.xdot.dat",directory+"shot6407.Ga.xdot.dat",directory+"shot6423.Ga.xdot.dat"]
stop_indices = [400,500,5500,750,2000]
linestyles = ["dashed"]*len(files)
ax = plt.gca()
error_bar_scaling = 0.02
for i,file in enumerate(files):
    time = np.loadtxt(file,skiprows=num_skiprows)[:stop_indices[i],0]*us_to_ns + time_shifts[i]
    xdot = np.loadtxt(file,skiprows=num_skiprows)[:stop_indices[i],1]
    filter(xdot)
    pressure = f(xdot)
    plt.plot(time,pressure,color=colors[i],linestyle=linestyles[i])
    ax.fill_between(time,pressure - error_bar_scaling*pressure,pressure + error_bar_scaling*pressure, alpha=0.2)
    ax.plot(time,pressure - error_bar_scaling*pressure, color=colors[i], alpha=0.5)
    ax.plot(time,pressure + error_bar_scaling*pressure, color=colors[i], alpha=0.5)
plt.xlim(300,690.0)
plt.ylim(0.0,35)
plt.xlabel("Time (ns)",fontsize=24)
plt.ylabel("Pressure (GPa)",fontsize=24)
scale_width = 1.0
scale_height = 1.0
plt.gcf().set_size_inches(width*scale_width,height*scale_height)
file = output_directory + "plot_pressure_later_shots.pdf"
plt.savefig(file)