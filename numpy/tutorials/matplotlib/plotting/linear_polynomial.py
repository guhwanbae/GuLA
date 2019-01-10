#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt

n = 100
length = 1
step = length / n

x = np.arange(0, length, step)

plt.figure('Simple graph')
plt.title('Simple graph')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, x, 'r', label='linear')
plt.plot(x, x**2, 'g', label='quadratic')
plt.plot(x, x**3, 'b', label='cubic')
plt.legend()
plt.show()


# In[ ]:




