import cv2

# Read and display an image
LenaImageBGR = cv2.imread('lena_colored.jpg', cv2.IMREAD_COLOR)
cv2.imshow('LenaBGR', LenaImageBGR)

# Convert image to GRAY and display it
LenaImageGRAY = cv2.cvtColor(LenaImageBGR, cv2.COLOR_BGR2GRAY)
cv2.imshow('LenaGRAY', LenaImageGRAY)

# Split the image into 3 channels and display the red channel
b,g,r=cv2.split(LenaImageBGR)
cv2.imshow('Red', r)

# Merge the 3 channels, swap the channels and display the image
merged = cv2.merge((g,r,b),LenaImageBGR)
cv2.imshow('Merged', merged)

cv2.waitKey(0)
cv2.destroyAllWindows()