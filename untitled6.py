# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 23:54:52 2016

@author: dell1
"""

from pylab import *
from math import *
x=[3.]
t=[0.]
w=[0.]
dt=0.01
endt=10
g=9.8
l=1
for i in range(int(endt/dt)):
	w_temp=w[i]-g/l*x[i]*dt-x[i]*dt+0.2*sin(2.0*t[i])
	x_temp=x[i]+w_temp*dt
	t_temp=t[i]+dt
	w.append(w_temp)
	x.append(x_temp)
	t.append(t_temp)

plot(t,x)
show()

