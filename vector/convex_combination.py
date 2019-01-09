#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import skimage.transform

face_a = plt.imread('../resource/face.png')
face_b = plt.imread('../resource/lena_gray.png')

# Match size of two image equally.
face_b = skimage.transform.resize(face_b, face_a.shape, mode='constant')

print('Shape of face A =', face_a.shape)
print('Shape of face B =', face_b.shape)


# In[2]:

plt.figure('Face A')
plt.title('Face A')
plt.imshow(face_a)
plt.show()

# In[3]:


plt.figure('Face B')
plt.title('Face B')
plt.imshow(face_b)
plt.show()


# In[20]:


def convexCombination(image_a, image_b, alpha):
    beta = 1 - alpha
    blend = image_a * alpha + image_b * beta
    return blend

blend = convexCombination(face_a, face_b, 0.5)

plt.figure('Blended face')
plt.title('Blended face')
plt.imshow(blend)
plt.show()
