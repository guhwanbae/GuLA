#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import skimage.transform

face_a = plt.imread('../resource/face.png')
face_b = plt.imread('../resource/lena_gray.png')

# Match size of two image equally.
face_b = skimage.transform.resize(face_b, face_a.shape, mode='constant')

def convexCombination(image_a, image_b, alpha):
    beta = 1 - alpha
    blend = image_a * alpha + image_b * beta
    return blend

def crossFade(image_a, image_b, n):
    frames = []
    for alpha in np.arange(0, 1, 1/n):
        blended_image = plt.imshow(convexCombination(face_a, face_b, alpha))
        frames.append([blended_image])
    return frames

fig = plt.figure('Cross-fade')

# Get 30 frames to animate.
frames = crossFade(face_a, face_b, 30)

ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True)
plt.title('Cross-fade')
plt.show()
