import numpy as np

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from matplotlib.animation import FuncAnimation

def f(z,u):
    return np.array([z[1],-omega*omega/(1+u)*np.sin(z[0]) - gamma*z[1]])

def update_RK4(z,u):
    k1 = f(z,u)
    y = z + dt*k1/2
    k2 = f(y,u)
    y = z + dt*k2/2
    k3 = f(y,u)
    y = z + dt*k3
    k4 = f(y,u)
    return z + dt*(k1+2*k2+2*k3+k4)/6


omega = 2*np.pi  # natural frequency
gamma = 0.01  # friction coefficient
eps = 0.1   # control amplitude

tf  = 20.0 # total time
n   = 1000 # number of time steps
dt = tf/n   
t = np.linspace(0,tf,n)

x_0 = np.array([0,1])
y_0 = np.array([np.pi,-0.0001])

x = np.zeros([n,2])
y = np.zeros([n,2])

x[0,:] = x_0[:]
y[0,:] = y_0[:]


u = eps*np.cos(2*omega*t)
u[:int(n/4)] = 0

for i in range(n-1):
    x[i+1,:] = update_RK4(x[i,:],u[i])
    y[i+1,:] = update_RK4(y[i,:],0)






fig = plt.figure(figsize=(14,8))
ax1 = plt.subplot(1,2,1)
ax1.set_xlim(-10, 10) 
ax1.set_ylim((-10, 5)) 
ax1.plot([-1, 1],[0, 0], color='black', lw=6)
line_pandelum, = ax1.plot([], [], lw=4, color='C0')
line_mass, = ax1.plot([], [], ls='None', ms = 15, marker = 'o', color='C1')
ax1.set_xticks([],'')
ax1.set_yticks([],'')

ax2 = plt.subplot(2,2,4)
ax2.set_xlim(0, tf) 
ax2.set_ylim(-1.2*eps, 1.2*eps) 
line_u1, = ax2.plot([], [], lw=2, color='C0',label=r'$u$')
plt.grid()
plt.ylabel(r'$u$', fontsize = 15, rotation =0)
plt.xlabel(r'$t$', fontsize = 15)
plt.legend(fontsize=18)

ax3 = plt.subplot(2,2,2)
ax3.set_xlim(-2, 2) 
ax3.set_ylim(-8, 8) 
line_xy, = ax3.plot([], [], lw=2, color='C1',label=r'$(x_1,x_2)$')
ax3.set_xlabel(r'$x_1$', fontsize = 15)
ax3.set_ylabel(r'$x_2$', fontsize = 15, rotation =0)
plt.grid()
plt.legend(fontsize=18)
#plt.legend(fontsize=10)

def init():
    line_pandelum.set_data([], [])
    line_mass.set_data([], [])
    line_u1.set_data([],[])
    line_xy.set_data([],[])
    return line_pandelum, line_mass, line_u1, line_xy,

def animate(i):  
    xx =  7*np.sin(x[i,0])*(1+u[i])
    yy = -7*np.cos(x[i,0])*(1+u[i])
    line_pandelum.set_data([0,xx], [0,yy])
    line_mass.set_data([xx],[yy])
    line_u1.set_data(t[:i],u[:i])
    line_xy.set_data(x[:i,0],x[:i,1])
    return line_pandelum, line_mass, line_u1, line_xy,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=n, interval=25, blit=True)
plt.show()





