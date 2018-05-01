###
### This script generates intensity distribution from circles automatically detected.
###

import numpy,sys
import matplotlib,matplotlib.pyplot 
import skimage,skimage.io,skimage.feature,skimage.transform

from skimage.draw import circle_perimeter

from skimage.filters import roberts, sobel, scharr, prewitt

import matplotlib.pyplot as plt

# 0. user defined variables
inputImageFile='day.2.tif'

# 1. read image
print('reading image...')
ima=skimage.io.imread(inputImageFile)
image=numpy.array(ima)

print(len(image),len(image[0]),len(image[0]))
#print(image,numpy.max(image),numpy.min(image))

sys.exit()

# 2. detect edges
print('detecting edges...')
edges=sobel(image)
#print(sum(edges))

# 3. detect radii
print('detecting radii...')
houghRadii=numpy.arange(20, 35, 2)
houghResults=skimage.transform.hough_circle(edges,houghRadii)



# 4. select the most prominent 5 circles
print('selecting circles...')
accums, cx, cy, radii = skimage.transform.hough_circle_peaks(houghResults, houghRadii,total_num_peaks=3)
print(accums,len(accums))

# Draw them
print('drawing circles...')
fig, ax = matplotlib.pyplot.subplots(ncols=1, nrows=1, figsize=(10, 4))
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius)

    print('before',center_y,image[circy, circx])
    image[circy, circx] = (220, 20, 20)
    print('after',image[circy, circx])
    
sys.exit()
    
# x. plotting figure
ax.imshow(image,cmap=plt.cm.gray)
#ax.imshow(edges, cmap=plt.cm.gray)
plt.savefig('result.pdf')


### consider hyst = filters.apply_hysteresis_threshold(edges, low, high)
