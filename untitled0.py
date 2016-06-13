# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:22:00 2016

@author: dell1
"""

print' ##               ###             ###                  ######'
print' ##              ## ##           ## ##                   ##'
print' ##             ##   ##         ##   ##                  ##'
print' ##            ##     ##       ##     ##                 ##'
print' ##           ##       ##     ##       ##                ##'
print' ##          ##         ##   ##         ##        ##     ##'
print' ##         ##           ## ##           ##       ##     ##'
print' #######   ##             ###             ##        ####'


from pylab import  *

v=[] 
t=[] 
g=9.8 
dt=0.1 
v.append(0.) 
t.append(0) 
end_time=10 

for i in range(int(end_time/dt)): 
        u=v[i]+g*dt 
        v.append(u) 
        t.append(dt*(i+1))
 
 
 
 
plot(t, v) 
show() 



