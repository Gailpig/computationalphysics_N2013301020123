# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:03:39 2016

@author:Gailpig
"""

from pylab import *
theta=[0.3]
t=[0.0]
w=[0.0]
dt=0.001
end_t=30
g=9.8
l=1.0
q=1.0
F=0.2


for i in range(int(end_t/dt)):
	w_temp=w[i]-g/l*theta[i]*dt-q*w[i]*dt+0.2*sin(2*t[i])*dt
	theta_temp=theta[i]+w_temp*dt
	t_temp=t[i]+dt
	w.append(w_temp)
	theta.append(theta_temp)
	t.append(t_temp)



plot(t,theta,label='w_D=2.0,F=0.2,q=1.0',color='r')
plt.xlabel('time/s')
plt.ylabel('theta')
legend()
show()
