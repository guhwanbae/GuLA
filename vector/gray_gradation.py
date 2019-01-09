#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

(width, height) = (160, 30)
max_intensity = 255
step = max_intensity / width

# Linearly increased array.
gradation_line = np.arange(0, max_intensity, step).reshape(width, 1)
# Stack lines to make plane.
gradation_image = np.tile(gradation_line, (1, height))

plt.figure('Gradation')
plt.title('Gradation')
plt.xlabel('width')
plt.ylabel('height')
plt.imshow(gradation_image)
plt.show()
