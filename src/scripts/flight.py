import numpy as np
import matplotlib.pyplot as plt
from pint import UnitRegistry
ureg = UnitRegistry()

#%% Constants

g = -9.81
RHO = 1.23
AREA = 0.0568
CLO = 0.1
CLA = 1.4
CDO = 0.08
CDA = 2.72
ALPHA0 = -4
m  = 0.175

#%% initial conditions

a0 = 0 / 180 * np.pi
v0 = 14.0

y0  = 1.0
vx0 = np.cos(a0) * v0
vy0 = np.sin(a0) * v0
alpha = 15.0
deltaT = 0.01


x = 0.0
y = y0
vx = vx0
vy = vy0

cl = CLO + CLA*alpha*np.pi/180
cd = CDO + CDA*np.power((alpha - ALPHA0)*np.pi/180, 2)

k = 0
t = 0
p = [(t,x,y,vx,vy)]


while (y > 0):
    deltavy = (RHO*np.power(vx,2)*AREA*cl/2/m+g)*deltaT
    deltavx = -RHO*np.power(vx,2)*AREA*cd*deltaT

    t  = t + deltaT
    vx = vx + deltavx
    vy = vy + deltavy
    x = x + vx * deltaT
    y = y + vy * deltaT

    p.append((t,x,y,vx,vy))
    k += 1

p = np.array(p)

plt.figure()
plt.plot(p[:,1], p[:,2])
plt.axis('equal')
plt.grid()


