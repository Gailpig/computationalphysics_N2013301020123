# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:52:10 2016

@author: Gailpig
"""

from pylab import *
import numpy as np
theta1=[0.2]
theta2=[0.2]
theta3=[0.2]
t=[0.0]
w1=[0.0]
w2=[0.0]
w3=[0.0]
dt=0.04
end_t=60
g=9.8
l=9.8
q=0.5
w_D=float(2.0/3)
F=[0.,0.5,1.2]


for i in range(int(end_t/dt)):
	w1_temp=w1[i]-g/l*sin(theta1[i])*dt-q*w1[i]*dt+F[0]*sin(w_D*t[i])*dt
	theta1_temp=theta1[i]+w1_temp*dt
	w2_temp=w2[i]-g/l*sin(theta2[i])*dt-q*w2[i]*dt+F[1]*sin(w_D*t[i])*dt
	theta2_temp=theta2[i]+w2_temp*dt
	w3_temp=w3[i]-g/l*sin(theta3[i])*dt-q*w3[i]*dt+F[2]*sin(w_D*t[i])*dt
	theta3_temp=theta3[i]+w3_temp*dt
     	t_temp=t[i]+dt
     	if theta1_temp<-np.pi: 
         theta1_temp=theta1_temp+2*np.pi 
     	if theta1_temp>np.pi: 
         theta1_temp=theta1_temp-2*np.pi 
     	if theta2_temp<-np.pi: 
         theta2_temp=theta2_temp+2*np.pi 
     	if theta2_temp>np.pi: 
         theta2_temp=theta2_temp-2*np.pi
     	if theta3_temp<-np.pi: 
         theta3_temp=theta3_temp+2*np.pi 
     	if theta3_temp>np.pi: 
         theta3_temp=theta3_temp-2*np.pi 
	w1.append(w1_temp)
	theta1.append(theta1_temp)
	w2.append(w2_temp)
	theta2.append(theta2_temp)
	w3.append(w3_temp)
	theta3.append(theta3_temp)
	t.append(t_temp)



plot(t,theta1,label='w_D=2/3,F=0,q=0.5',color='r')
plot(t,theta2,label='w_D=2/3,F=0.5,q=0.5',color='b')
plot(t,theta3,label='w_D=2/3,F=1.2,q=0.5',color='k')
plt.xlabel('time/s')
plt.ylabel('theta')
plt.ylim(-4,7)
legend()
show()
