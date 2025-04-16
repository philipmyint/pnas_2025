
import numpy as np
import sys
import pandas as pd
from matplotlib import pyplot as plt

sys.path.append("./../")
from utility_constants import us_to_ns, plot_colors

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

#plot the velocities
plt.figure()
directories = ["./../Simulation_outputs/Brown_shot51/","./../Simulation_outputs/Brown_shot53/","./../Simulation_outputs/Brown_shot60/","./../Simulation_outputs/Brown_shot6407/"]
stop_indices = [15000,15000,18000,18000]
time_shifts = [-130.0,-70.0,0.0,-450.0]
time_shifts = [-100.0,-50,0.0,-460.0]
linestyles = ["solid"]*len(directories)
legend_labels = ["Shot 1","Shot 2","Shot 3","Shot 4"]
num_skiprows = 2
for i,directory in enumerate(directories):
    time = np.loadtxt(directory + "pf_phi.target_bin.dat",skiprows=num_skiprows)[:stop_indices[i],0]*us_to_ns + time_shifts[i]
    phi = np.loadtxt(directory + "pf_phi.target_bin.dat",skiprows=num_skiprows)[:stop_indices[i],1]
    plt.plot(time,phi,color=plot_colors[i+1][0],linestyle=linestyles[i],label=legend_labels[i])
plt.legend(legend_labels,prop={"size":16},frameon=False,loc="best")
plt.xlim(300,680.0)
plt.ylim(0.0,1.0)
plt.xlabel("Time (ns)",fontsize=24)
plt.ylabel("Ga-III phase fraction",fontsize=24)
scale_width = 1.0
scale_height = 1.0
plt.gcf().set_size_inches(width*scale_width,height*scale_height)
file = output_directory + "plot_phase_fractions.pdf"
plt.savefig(file)