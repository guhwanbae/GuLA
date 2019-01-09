#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import matplotlib.pyplot as plt

# Make points to express segment line.
def makeSegment(src, dst, n):
    vec = dst - src
    segment_line = np.array([src + vec * scale_factor for scale_factor in np.arange(0, 1, 1/n)])
    return segment_line

src = np.array([.5, 1])
dst = np.array([3.5, 3])
n = 15

segment_line = makeSegment(src, dst, n)

x = segment_line[:,0]
y = segment_line[:,1]

plt.figure('Segment')
plt.title('Segment line from (0.5, 1) to (3.5, 3)')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.grid()
plt.plot(x,y, 'b.')
plt.show()


# In[22]:


# Make a segment line by using convex combination of two vectors.
def makeSegmentConvex(src, dst, n):
    alpha = np.arange(0, 1, 1/n)
    beta = 1-alpha
    segment_line = np.array([a*src + b*dst for (a,b) in zip(alpha, beta)])
    return segment_line

segment_line = makeSegmentConvex(src, dst, n)

x = segment_line[:,0]
y = segment_line[:,1]

plt.figure('Segment - convex combination')
plt.title('Segment line by using convex combination')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.grid()
plt.plot(x,y, 'm.')
plt.show()

