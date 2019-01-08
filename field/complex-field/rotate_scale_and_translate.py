#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Set of complex points.
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j,
     2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

def getRealImag(complex_points):
    reals = [z.real for z in complex_points]
    imags = [z.imag for z in complex_points]
    return (reals, imags)

(reals, imags) = getRealImag(S)

plt.title('Complex points')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.plot(reals, imags, 'b.')
plt.show()


# In[2]:


def rotateAndScale(complex_points, angle_rad, scale_factor):
    phasor = scale_factor * complex(np.cos(angle_rad), np.sin(angle_rad))
    return [z * phasor for z in complex_points]

# Scale in half and rotate by 90 degrees.
rotated_and_scaled = rotateAndScale(S, np.pi/2, 1/2)

(reals, imags) = getRealImag(rotated_and_scaled)

plt.title('Scale in half and rotate by 90 degrees.')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.plot(reals, imags, 'm.')
plt.show()


# In[68]:


def rotateAndTranslate(complex_points, angle_rad, shift_factor):
    # Shift points after rotating.
    phasor = complex(np.cos(angle_rad), np.sin(angle_rad))
    return [(z * phasor) + shift_factor for z in complex_points]

# Rotate by -145 degrees and parallel translate by 1+2j.
rotated_and_translated = rotateAndTranslate(S, -np.pi*5/4, 0)

(reals, imags) = getRealImag(rotated_and_translated)

plt.title('Rotate by -145 degrees and parallel translate by 1+2j.')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.plot(reals, imags, 'c.')
plt.show()
