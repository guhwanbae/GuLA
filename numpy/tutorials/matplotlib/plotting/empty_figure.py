#!/usr/bin/env python
# coding: utf-8

# In[12]:

import numpy as np
import matplotlib.pyplot as plt

fig, axs_list = plt.subplots(2, 2)

print('Figure object =', type(fig))
print('Axes object =', type(axs_list))
print('Shape of axes =', axs_list.shape)

left_top = axs_list[0, 0]
print('Axis object =', type(left_top))

left_top.set_xlim([-1,1])
left_top.set_ylim([-1,1])

n = 100
x = np.linspace(0, n, n)

# Draw a segment line.
left_top.plot(x, x, 'r')
plt.show()

# In[ ]:




