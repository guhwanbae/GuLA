#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Simple linear equation solver.
# ax+b = c
def solve1(a, b, c):
    return (c-b)/a

# 2x+1 = 5
print('2x+1=5, x=', solve1(2,1,5))

# (10+j5)x+5=20
print('(10+j5)x+5 = 20, x=', solve1(10+5j,5,20))


# In[36]:


import matplotlib.pyplot as plt

# Set of complex points.
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j,
     2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

reals = [z.real for z in S]
imags = [z.imag for z in S]

# Plot points by uinsg pyplot.
plt.title('Complex points')
plt.xlabel('Real')
plt.ylabel('Imagenary')
plt.xlim([0, 6])
plt.ylim([0, 6])
plt.plot(reals, imags, '.')
plt.show()


# In[ ]:




