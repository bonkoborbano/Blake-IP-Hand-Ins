import cv2
import matplotlib.pylab as plt

# Read the image
LenaImageBGR = cv2.imread('lena_colored.jpg', cv2.IMREAD_COLOR)

# Resize image to 256x256
LenaImageBGR_Mini = cv2.resize(LenaImageBGR, (256,256))

#Display an image
cv2.imshow('LenaBGR', LenaImageBGR_Mini)

# Brightness
k = 100
brightLena = cv2.convertScaleAbs(LenaImageBGR_Mini, alpha=1, beta=k)
cv2.imshow('Brightness', brightLena)

# Contrast
k = 2
contrastLena = cv2.convertScaleAbs(LenaImageBGR_Mini, alpha=2, beta=0)
cv2.imshow('Contrast', contrastLena)

# Historgram of blue channel
histo_blue = cv2.calcHist([LenaImageBGR_Mini], [0], None, [256], [0, 256])
blueChannel = plt.plot(histo_blue, color='b')
plt.show()

# Greyscale mapping
LenaImageGRAY = cv2.cvtColor(LenaImageBGR_Mini, cv2.COLOR_BGR2GRAY)
inverseImage = 255 - LenaImageGRAY
cv2.imshow('InverseLenaGRAY', inverseImage)


cv2.waitKey(0)
cv2.destroyAllWindows()