#!/usr/bin/env python
# coding: utf-8

# In[17]:


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


# In[18]:


# Complex point rotation can be expressed by phasor operation.
def rotate(complex_points, rad):
    phase = complex(np.cos(rad), np.sin(rad))
    print('phase =', phase)
    return [z * phase for z in complex_points]

# Rotate a figure 180 degrees.
rotated_180 = rotate(S, np.pi)

(reals, imags) = getRealImag(rotated_180)

plt.title('Rotate a figure 180 degrees')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.plot(reals, imags, 'm.')
plt.show()


# In[19]:


# Rotate a figure -90 degrees.
# Counter clock rotation.
rotated_counter_90 = rotate(S, -np.pi/2)

(reals, imags) = getRealImag(rotated_counter_90)

plt.title('Rotate a figure -90 degrees')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.plot(reals, imags, 'c.')
plt.show()


# In[21]:


# Rotate a figure 45 degrees.
rotated_45 = rotate(S, np.pi/4)

(reals, imags) = getRealImag(rotated_45)

plt.title('Rotate a figure 45 degrees')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.plot(reals, imags, 'r.')
plt.show()


# In[ ]:




