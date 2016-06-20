# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:53:03 2016

@author: dell1
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

sigma=10
b=8.0/3.0
dt=0.001


class Lorenz:
	def __init__(self,x,y,z,r):
		self.x=[x]
		self.y=[y]
		self.z=[z]
		self.r=r
		self.t=[0.]

	def update(self):
		current_x=self.x[-1]
		current_y=self.y[-1]
		current_z=self.z[-1]
		a_x=sigma*(current_y-current_x)
		a_y=-current_x*current_z+self.r*current_x-current_y
		a_z=current_x*current_y-b*current_z
		self.next_x=current_x+a_x*dt
		self.next_y=current_y+a_y*dt
		self.next_z=current_z+a_z*dt
		self.next_t=self.t[-1]+dt

	def fire(self):
		while (self.t[-1]<=50):
			self.update()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.t.append(self.next_t)
			
		plt.plot(self.x,self.z)

A=Lorenz(1,0,0,25)
A.fire()
plt.legend(loc='best')
plt.xlim(-20,20)
plt.xlabel('x')
plt.ylabel('z')
plt.show()

