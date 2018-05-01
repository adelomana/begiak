import numpy as np
import matplotlib.pyplot as plt
import sys

from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte


# Load picture and detect edges

image = img_as_ubyte(data.coins()[160:230, 70:270])
print(image,np.max(image),np.min(image))

print('detecting edges...')
edges = canny(image, sigma=3, low_threshold=10, high_threshold=50)
print(sum(edges))

# Detect two radii
print('detecting radii...')
hough_radii = np.arange(20, 35, 2)
hough_res = hough_circle(edges, hough_radii)
#print(hough_res)


# Select the most prominent 5 circles
print('selecting circles...')
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,
                                           total_num_peaks=3)

print(accums,len(accums))

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
image = color.gray2rgb(image)
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius)

    print('before',image[circy, circx])
    image[circy, circx] = (220, 20, 20)
    print('after',image[circy, circx])

ax.imshow(image, cmap=plt.cm.gray)
plt.savefig('test.pdf')
