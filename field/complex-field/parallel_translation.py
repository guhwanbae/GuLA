#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt

# Set of complex points.
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j,
     2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

# 'z' is the complex point.
reals = [z.real for z in S]
imags = [z.imag for z in S]

plt.title('Complex points')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([0, 6])
plt.ylim([0, 6])
plt.plot(reals, imags, 'b.')
plt.show()


# In[3]:


# Parallel translation.
# Traslate all points by 1+j2.
translated_points = {comp + (1+2j) for comp in S}

reals = [z.real for z in translated_points]
imags = [z.imag for z in translated_points]

plt.title('Translated complex points by 1+j2')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([0, 6])
plt.ylim([0, 6])
plt.plot(reals, imags, 'r.')
plt.show()


# In[5]:


def getRealImag(complex_points):
    reals = [z.real for z in complex_points]
    imags = [z.imag for z in complex_points]
    return (reals, imags)

# Move left eye point to origin.
left_eye_origin = [z - (3+4j) for z in translated_points]

(reals, imags) = getRealImag(left_eye_origin)

plt.title('Left eye origin')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.grid(True)
plt.plot(reals, imags, 'm.')  # m means magenta.
plt.show()


# In[ ]:




