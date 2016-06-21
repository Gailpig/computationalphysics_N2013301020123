# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 20:07:38 2016

@author: Gailpig
"""

from pylab import *
theta1=[3.0]
theta2=[3.0]
t=[0.]
w1=[0.]
w2=[0.]
dt=0.001
end_t=20
g=9.8
l=9.8



for i in range(int(end_t/dt)):
	w1_temp=w1[i]-g/l*theta1[i]*dt
	w2_temp=w2[i]-g/l*sin(theta2[i])*dt
	theta1_temp=theta1[i]+w1_temp*dt
	theta2_temp=theta2[i]+w2_temp*dt
	t_temp=t[i]+dt
	w1.append(w1_temp)
	theta1.append(theta1_temp)
	w2.append(w2_temp)
	theta2.append(theta2_temp)
	t.append(t_temp)


plot(t,theta1,label='linear',color='r')
plt.xlabel('time/s')
plot(t,theta2,label='nonlinear',color='g')
plt.ylabel('theta')
legend()
show()
plt.savefig("1.png")


