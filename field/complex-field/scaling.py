#!/usr/bin/env python
# coding: utf-8

# In[28]:


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
plt.xlim([0, 6])
plt.ylim([0, 6])
plt.plot(reals, imags, 'b.')
plt.show()


# In[30]:


def scaling(points, factor):
    return [z * factor for z in points]

scaled_points = scaling(S, 0.5)
(reals, imags) = getRealImag(scaled_points)

plt.title('Scaled points')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([0, 6])
plt.ylim([0, 6])
plt.plot(reals, imags, 'c.')  # 'c' means cyan.
plt.show()

