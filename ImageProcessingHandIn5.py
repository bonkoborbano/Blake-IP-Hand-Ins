import cv2 as cv
import numpy as np
import copy

# Read the image
blobImage = cv.imread('BLOBimage.png', cv.IMREAD_GRAYSCALE)

# Display an image
cv.imshow('BlobImage', blobImage)

# Grassfire algorithm
imLabel = copy.copy(blobImage)
def grassFires(y,x,label,im):
  Ylist = []
  Xlist = []
  Ylist.append(y)
  Xlist.append(x)
  im[y,x] = label

  while(len(Ylist)>0):
    y = Ylist.pop(0)
    x = Xlist.pop(0)

    if (y>0 and im[y-1,x] == 255):
      im[y-1,x] = label
      Ylist.append(y-1)
      Xlist.append(x)

    if (y<im.shape[0]-1 and im[y+1,x] == 255):
      im[y+1,x] = label
      Ylist.append(y+1)
      Xlist.append(x)

    if (x>0 and im[y,x-1] == 255):
      im[y,x-1] = label
      Ylist.append(y)
      Xlist.append(x-1)

    if (x<im.shape[1]-1 and im[y,x+1] == 255):
      im[y,x+1] = label
      Ylist.append(y)
      Xlist.append(x+1)

label =  1

for yy2 in range(imLabel.shape[0]):
  for xx2 in range(imLabel.shape[1]):
    if (imLabel[yy2,xx2] == 255):
      grassFires(yy2,xx2,label,imLabel)
      label += 1

# Calculate the area of the blobs
area = copy.copy(imLabel)

areaArray = [0]*label
for x in range (area.shape[0]):
  for y in range (area.shape[1]):
   for i in range (1,label):
#   for i in range (label): if you want to calculate also the area of the black pixel
      if (area[x,y] == i):
        areaArray[i] +=1
print('Area of the blobs:')
print(areaArray)

# Detect the contours on the binary image using CHAIN_APPROX_NONE
contours, hierarchy = cv.findContours(image=blobImage, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

# Draw contours on the original image
image_copy = blobImage.copy()
image_copy = cv.cvtColor(image_copy, cv.COLOR_GRAY2BGR)

# Find the largest contour by area
largest_contour = max(contours, key=cv.contourArea)

cv.drawContours(image=image_copy, contours=[largest_contour], contourIdx=-1, color=(0, 0, 255), thickness=2, lineType=cv.LINE_AA)

# See the results
cv.imshow('biggest contour', image_copy)

cv.waitKey(0)
cv.destroyAllWindows()