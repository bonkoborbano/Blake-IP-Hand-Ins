import numpy as np
import cv2 as cv
import copy

# Read the image
JesseKandaSsense = cv.imread('JesseKandaSsense.jpg', cv.IMREAD_COLOR)
# Resize image to 128x128
JesseKandaSsense = cv.resize(JesseKandaSsense, (128,128))
# Display an image
cv.imshow('JesseKandaSsense', JesseKandaSsense)


"""THRESHOLDING"""
JesseKandaSsenseGrey = cv.cvtColor(JesseKandaSsense, cv.COLOR_BGR2GRAY)
cv.imshow('JesseKandaSsenseGrey', JesseKandaSsenseGrey)
imageThreshold = copy.copy(JesseKandaSsenseGrey)

threshold = 150

for y in range(JesseKandaSsenseGrey.shape[0]):
  for x in range(JesseKandaSsenseGrey.shape[1]):
    if (JesseKandaSsenseGrey[y,x]<threshold):
      imageThreshold[y,x] = 0
    else:
      imageThreshold[y,x] = 255
cv.imshow('JesseKandaSSenseGreyBinary', imageThreshold)


"""EROSION"""
imErode = copy.copy(imageThreshold)

# Erosion with loops
for y in range(1,imageThreshold.shape[0]-1):
  for x in range(1,imageThreshold.shape[1]-1):
    sum = 0
    for ky in range (3):
      for kx in range (3):
        sum += imageThreshold[y+ky-1, x+kx-1]
    if(sum == 255*9):
      imErode[y,x] = 255
    else:
      imErode[y,x] = 0
cv.imshow('ErosionLoops', imErode)


# Erosion with OpenCV function cv.erode
kernel = np.ones((3,3), np.uint8) #define the kernel - needs to be uint8

imErode_2 = cv.erode(imageThreshold, kernel, iterations=1)
cv.imshow('ErosionCV2', imErode_2)


"""DILATION"""
imDilate = copy.copy(imageThreshold)

kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]])

# Dilation with loops
for y in range(2,imageThreshold.shape[0]-2):
  for x in range(2,imageThreshold.shape[1]-2):
    sum = 0
    for ky in range (5):
      for kx in range (5):
        sum += imageThreshold[y+ky-2, x+kx-2] * kernel[ky,kx]
    if(sum >= 255):
      imDilate[y,x] = 255
    else:
      imDilate[y,x] = 0
cv.imshow('DilationLoops', imDilate)

# Dilation with OpenCV function dilate
kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]],
                  np.uint8)
imDilate_2 = cv.dilate(imageThreshold, kernel, iterations=1)
cv.imshow('DilationCV2', imDilate_2)


cv.waitKey(0)
cv.destroyAllWindows()