
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

LiF = np.loadtxt("./../S7271v3_LiF_principal_isentrope.dat",skiprows=1)
LiF_pressure = LiF[:,2]
LiF_up = LiF[:,5]
f = interpolate.interp1d(LiF_up,LiF_pressure)

#desired set of units for all of the plots below
units = "default"

#output directory
output_directory = "./"

#plot the velocities
plt.figure()
directories = ["./../Simulation_outputs/Brown_shot51/","./../Simulation_outputs/Brown_shot53/","./../Simulation_outputs/Brown_shot60/","./../Simulation_outputs/Brown_shot6407/"]
start_indices = [7300,7000,6600,6600]
stop_indices = [14000,14000,15200,14500]
time_shifts = [-100.0,-50,0.0,-460.0]
linestyles = ["solid"]*len(directories)
legend_labels = ["Shot 1","Shot 2","Shot 3","Shot 4"]
num_skiprows = 2
for i,directory in enumerate(directories):
    time = np.loadtxt(directory + "p.target_back.dat",skiprows=num_skiprows)[start_indices[i]:stop_indices[i],0]*us_to_ns + time_shifts[i]
    pressure = np.loadtxt(directory + "p.target_back.dat",skiprows=num_skiprows)[start_indices[i]:stop_indices[i],1]/GPa_to_Mbar
    plt.plot(time,pressure,color=plot_colors[i+1][0],linestyle=linestyles[i],label=legend_labels[i])
plt.legend(legend_labels,prop={"size":16},frameon=False,loc="best")
#add experimental data
directory = "./../Simulation_outputs/EXPERIMENT_gallium/"
files = [directory+"shot51.Ga.xdot.dat",directory+"shot53.Ga.xdot.dat",directory+"shot60.Ga.xdot.dat",directory+"shot6407.Ga.xdot.dat"]
stop_indices = [480,410,2000,1000,1000]
linestyles = ["dashed"]*len(files)
ax = plt.gca()
error_bar_scaling = 0.02
for i,file in enumerate(files):
    time = np.loadtxt(file,skiprows=num_skiprows)[:stop_indices[i],0]*us_to_ns + time_shifts[i]
    xdot = np.loadtxt(file,skiprows=num_skiprows)[:stop_indices[i],1]
    filter(xdot)
    pressure = f(xdot)
    plt.plot(time,pressure,color=plot_colors[i+1][0],linestyle=linestyles[i])
    ax.fill_between(time,pressure - error_bar_scaling*pressure,pressure + error_bar_scaling*pressure, alpha=0.2)
    ax.plot(time,pressure - error_bar_scaling*pressure, color=plot_colors[i+1][0], alpha=0.5)
    ax.plot(time,pressure + error_bar_scaling*pressure, color=plot_colors[i+1][0], alpha=0.5)
#add arrows and annotations
ax.annotate("",xytext=(0.39,0.24),xy=(0.31,0.49),xycoords='axes fraction',arrowprops=dict(arrowstyle="->"))
ax.annotate("",xytext=(0.41,0.23),xy=(0.38,0.5),xycoords='axes fraction',arrowprops=dict(arrowstyle="->"))
plt.annotate('loop',xy=(0.36,0.2),xycoords='axes fraction',color="black",fontsize=24)
ax.annotate("",xytext=(0.55,0.24),xy=(0.64,0.41),xycoords='axes fraction',arrowprops=dict(arrowstyle="->"))
ax.annotate("",xytext=(0.63,0.23),xy=(0.7,0.42),xycoords='axes fraction',arrowprops=dict(arrowstyle="->"))
plt.annotate('no loop',xy=(0.5,0.2),xycoords='axes fraction',color="black",fontsize=24)
plt.xlim(300,620.0)
plt.ylim(0.0,35)
plt.xlabel("Time (ns)",fontsize=24)
plt.ylabel("Pressure (GPa)",fontsize=24)
scale_width = 1.0
scale_height = 1.0
plt.gcf().set_size_inches(width*scale_width,height*scale_height)
file = output_directory + "plot_pressure.pdf"
plt.savefig(file)