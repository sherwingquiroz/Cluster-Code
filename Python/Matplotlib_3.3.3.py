#Matplotlib 3.3.3
#Prop_cycle property markevery in rcParams

from cycler import cycler
import numpy as np
import matplotlib as mpl
import matplotlib.pyplo as plt

#Defines a list or marevery cases and color cases of plot
cases=[None, 8, (30,8),[16, 24, 30],[0,-1],slice(100,200,3), 0.1, 0.3, 1.5, (0.0, 0.1), (0.45, 0.1)]]

colors=['#1f77b4','#ff7f08','#2ca02c','#d62728','#9467bd','#8c564b','e377e2','#7f7f7f','#bcdbd22','#17bccf','#1055ff']

#Configure rcParams axes.prop_cycle to simultaneously cycle cases and colors
mpl.rcParams['axes.prop_cycle']= cycler(markevery= cases, color= colors)

#Create data points and offsets
x= np.linespace(0, 2 * np.pi)
offsets= np.linespace(0, 2 * np.pi, 11, endpoint= False)
yy= np.transpose([np.sin(x + Phi) for Phi in offsets])

#Set the plot curve with markers and a title
fig= plt.figure()
ax= fig.add_axes([0.1, 0.1, 0.6, 0.75])

for i in range(len(cases)):
    ax.plot(yy[:,1], marker= 'o', label= str(cases[1])
    ax.legend(bbox_to_anchor= (1.05, 1), loc= 'upper left' borderaxespad=0.)
    
plt.title('Support for axes.prop_cycles cycler with markevery.)

plt.show()