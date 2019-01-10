#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import matplotlib.pyplot as plt

n = 100

x = np.linspace(0, 1, n)
noise = np.random.rand(n)

plt.figure('Random noise')
plt.title('Random noise')
plt.plot(x, noise)
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel('time')
plt.ylabel('power')
plt.show()


# In[29]:


def gaussianFilter(arr):
    kernel = np.array([7, 26, 41, 26, 7]) / 273
    print('Gaussian kernel(shape = %s)' % kernel.shape, kernel)
    
    denoise = np.convolve(arr, kernel, mode='same')
    return denoise

denoise = gaussianFilter(noise)

plt.title('Denoise signal')
plt.plot(x, denoise)
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.show()


# In[31]:


plt.subplot(2, 1, 1)
plt.title('Random noise')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.plot(x, noise)

plt.subplot(2, 1, 2)
plt.title('Denoise signal')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.plot(x, denoise)

plt.show()


# In[ ]:





# In[ ]:




