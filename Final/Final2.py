# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:10:51 2016

@author: Gailpig
"""
from pylab import *
theta1=[0.3]
theta2=[0.3]
theta3=[0.3]
t=[0.0]
w1=[0.0]
w2=[0.0]
w3=[0.0]
dt=0.001
end_t=10
g=9.8
l=1.0
q=[1.0,5.0,10.0]


for i in range(int(end_t/dt)):
	w1_temp=w1[i]-g/l*theta1[i]*dt-q[0]*w1[i]*dt
	w2_temp=w2[i]-g/l*theta2[i]*dt-q[1]*w2[i]*dt
	w3_temp=w3[i]-g/l*theta3[i]*dt-q[2]*w3[i]*dt
	theta1_temp=theta1[i]+w1_temp*dt
	theta2_temp=theta2[i]+w2_temp*dt
	theta3_temp=theta3[i]+w3_temp*dt
	t_temp=t[i]+dt
	w1.append(w1_temp)
	theta1.append(theta1_temp)
	w2.append(w2_temp)
	theta2.append(theta2_temp)
	w3.append(w3_temp)
	theta3.append(theta3_temp)
	t.append(t_temp)


plot(t,theta1,label='q=1.0',color='r')
plot(t,theta2,label='q=5.0',color='k')
plot(t,theta3,label='q=10.0',color='g')
plt.xlabel('time/s')
plt.ylabel('theta')
legend()
show()
