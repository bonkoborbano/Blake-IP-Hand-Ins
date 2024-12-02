import numpy as np
import cv2 as cv
import copy

# Read the image
JesseKandaSsense = cv.imread('JesseKandaSsense.jpg', cv.IMREAD_COLOR)
# Resize image to 128x128
JesseKandaSsense = cv.resize(JesseKandaSsense, (128,128))
# Display an image
cv.imshow('JesseKandaSsense', JesseKandaSsense)


#5x5 MEAN BLUR
# KERNEL DEFINITION
kernel_1 = np.array ([[1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1]])
# CONVOLUTION WITH LOOPS
mean5x5 = copy.copy(JesseKandaSsense).astype(float)
for y in range(2, JesseKandaSsense.shape[0]-2):
  for x in range(2, JesseKandaSsense.shape[1]-2):
    for c in range(JesseKandaSsense.shape[2]):
      sum = 0
      for ky in range(5):
        for kx in range(5):
          sum += JesseKandaSsense[y+ky-2, x+kx-2, c]*kernel_1[ky,kx]
      mean5x5[y,x,c] = sum/25.0
cv.imshow('Mean5x5', mean5x5)


#LEFT SOBEL
# KERNEL DEFINITION
kernel_2 = np.array ([[1,0,-1],
                    [2,0,-2],
                    [1,0,-1]])
# CONVOLUTION WITH LOOPS
JesseKandaSsenseGray = cv.cvtColor(JesseKandaSsense, cv.COLOR_BGR2GRAY)
leftSobel = copy.copy(JesseKandaSsenseGray).astype(int)
for y in range(1, JesseKandaSsenseGray.shape[0]-1):
  for x in range(1, JesseKandaSsenseGray.shape[1]-1):
      sum = 0
      for ky in range(3):
        for kx in range(3):
          sum += JesseKandaSsenseGray[y+ky-1, x+kx-1]*kernel_2[ky,kx]
      leftSobel[y, x] = sum/9
leftSobel = cv.convertScaleAbs(leftSobel)
cv.imshow('Left Sobel', leftSobel)


#RIGHT SOBEL
# KERNEL DEFINITION
kernel_3 = np.array ([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])

# CONVOLUTION WITH LOOPS
rightSobel = copy.copy(JesseKandaSsenseGray).astype(int)
for y in range(1, JesseKandaSsenseGray.shape[0]-1):
  for x in range(1, JesseKandaSsenseGray.shape[1]-1):
      sum = 0
      for ky in range(3):
        for kx in range(3):
          sum += JesseKandaSsenseGray[y+ky-1, x+kx-1]*kernel_3[ky,kx]
      rightSobel[y, x] = sum/9
rightSobel = cv.convertScaleAbs(rightSobel)
cv.imshow('Right Sobel', rightSobel)


#MAXIMUM FILTER
max_filter = copy.copy(JesseKandaSsense).astype(int)
for y in range(1,max_filter.shape[0]-1):
  for x in range(1,max_filter.shape[1]-1):
    for c in range(max_filter.shape[2]):
      array = [0]*9
      for ky in range(3):
        for kx in range(3):
          array[ky*3+kx] = JesseKandaSsense[y+ky-1,x+kx-1,c]
      array.sort()
      max_filter[y,x,c] = array[8]
max_filter = cv.convertScaleAbs(max_filter)
cv.imshow('Max Filter', max_filter)


#MY OWN KERNEL
kernel_4 = np.array ([[10,0,1],
                      [5,2,2],
                        [14,0,-19]])

# CONVOLUTION WITH LOOPS
blakesKernel = copy.copy(JesseKandaSsense).astype(float)
for y in range(1, JesseKandaSsense.shape[0]-1):
  for x in range(1, JesseKandaSsense.shape[1]-1):
    for c in range(JesseKandaSsense.shape[2]):
      sum = 0
      for ky in range(3):
        for kx in range(3):
          sum += JesseKandaSsense[y+ky-1, x+kx-1, c]*kernel_4[ky,kx]
      blakesKernel[y,x,c] = sum
cv.imshow('Blakes Kernel', blakesKernel)


cv.waitKey(0)
cv.destroyAllWindows()