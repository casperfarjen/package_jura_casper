#rv_curve_Casper package

### JURA IV python example, May 09, 2023

This package allows you to create a radial velocity plot of a star orbited by a planet.

#### Usage instructions

#import libraries
import numpy as np
import matplotlib.pyplot as plt
#import our rv_curve_class
from rv_curve_Casper.rv_curve_module import rv_curve_class

#Create the instance
rv = rv_curve_class(t0=0., p=30., e=0.5, w=np.pi/3, k=10., t_init=0., t_end=25.)

#Create the plot
rv.plot()