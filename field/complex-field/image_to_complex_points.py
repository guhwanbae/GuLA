import numpy as np
import matplotlib.pyplot as plt

def getRealImag(complex_points):
    reals = [z.real for z in complex_points]
    imags = [z.imag for z in complex_points]
    return (reals, imags)

def rgb2gray(source_image):
    weighted_sum_factor = [.299, .587, .114]
    return np.dot(source_image[:,:,:3], weighted_sum_factor)

def gray2complex(gray_image):
    scale_factor = 1/255
    threshold = 120*scale_factor
    [width, height] = gray_image.shape
    return np.array([complex(x,y) for x in range(width) for y in range(height) if gray_image[x,y] < threshold])

gray_source = plt.imread('../../resource/face.png')

complex_points = gray2complex(gray_source)

(reals, imags) = getRealImag(complex_points)

# Oops! Image is rotated by 90 degrees.
plt.title('Image expressed by complex. (Wrong allignment)')
plt.xlabel('Real')
plt.ylabel('Imagerany')
plt.plot(reals, imags, '.')
plt.show()

# To get correct allignment image, rotate by -90 debgrees.
complex_points = complex_points * -1j

(reals, imags) = getRealImag(complex_points)

plt.title('Image expressed by complex. (Good allignment)')
plt.plot(reals, imags, '.')
plt.show()
