# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:59:10 2020

@author: anurag
"""

# import required libraries
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

#1.  Read the image -----------------------------------------

# parameter for image to scan/process
args_image = r'Document Scanner\bill.png'
# read the image
image = cv2.imread(args_image)
orig = image.copy()
# show the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0) # press 0 to close all cv2 windows
cv2.destroyAllWindows() 

#Change the dimensions of the image
# get dimensions of image
dimensions = image.shape
 
# height, width, number of channels in image
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)



#resize the image
scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',image.shape)
 
cv2.imshow("Resized image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

orig = image.copy()  #very important line in terms of 

##experiment
## convert to RGB
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
## convert to grayscale
#gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
## create a binary thresholded image
#_, binary = cv2.threshold(gray, 200, 127, cv2.THRESH_BINARY_INV)
## show it
#plt.imshow(binary, cmap="gray")
#plt.show()
#
## find the contours from the thresholded image
#contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
## draw all contours
#image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
## show the image with the drawn contours
#
#cv2.imshow("Contour Outline", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#2. Identify the edges -------------------------------------

# convert image to gray scale. This will remove any color noise
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur the image to remove high frequency noise 
# it helps in finding/detecting contour in gray image
grayImageBlur = cv2.blur(grayImage,(3,3))
# then we performed canny edge detection
edgedImage = cv2.Canny(grayImageBlur, 100, 300, 3)
# show the gray and edge-detected image
#cv2.imshow("gray", grayImage)
#cv2.imshow("grayBlur", grayImageBlur)
cv2.imshow("Edge Detected Image", edgedImage)
cv2.waitKey(0) # press 0 to close all cv2 windows
cv2.destroyAllWindows()

#3. Detect the document edges in the image --------------------------
# find the contours in the edged image, sort area wise 
# keeping only the largest ones 
allContours = cv2.findContours(edgedImage.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
allContours = imutils.grab_contours(allContours)
# descending sort contours area and keep top 1
allContours = sorted(allContours, key=cv2.contourArea, reverse=True)[:1]
# approximate the contour
perimeter = cv2.arcLength(allContours[0], True) 
ROIdimensions = cv2.approxPolyDP(allContours[0], 0.02*perimeter, True)
# show the contour on image
cv2.drawContours(image, [ROIdimensions], -1, (0,255,0), 2)
cv2.imshow("Contour Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(ROIdimensions.shape)
#
#print(ROIdimensions)

#4. Identify and extract document boundary/edges
# reshape coordinates array
ROIdimensions = ROIdimensions.reshape(4,2)
# list to hold ROI coordinates
rect = np.zeros((4,2), dtype='float32')
# top left corner will have the smallest sum, 
# bottom right corner will have the largest sum
s = np.sum(ROIdimensions, axis=1)
rect[0] = ROIdimensions[np.argmin(s)]
rect[2] = ROIdimensions[np.argmax(s)]
# top-right will have smallest difference
# botton left will have largest difference
diff = np.diff(ROIdimensions, axis=1)
rect[1] = ROIdimensions[np.argmin(diff)]
rect[3] = ROIdimensions[np.argmax(diff)]
# top-left, top-right, bottom-right, bottom-left
(tl, tr, br, bl) = rect
# compute width of ROI
widthA = np.sqrt((tl[0]-tr[0])**2 + (tl[1]-tr[1])**2 )
widthB = np.sqrt((bl[0]-br[0])**2 + (bl[1]-br[1])**2 )
maxWidth = max(int(widthA), int(widthB))
# compute height of ROI
heightA = np.sqrt((tl[0]-bl[0])**2 + (tl[1]-bl[1])**2 )
heightB = np.sqrt((tr[0]-br[0])**2 + (tr[1]-br[1])**2 )
maxHeight = max(int(heightA), int(heightB))

#5. Apply perspective transform---------------------
# Set of destinations points for "birds eye view"
# dimension of the new image
dst = np.array([
    [0,0],
    [maxWidth-1, 0],
    [maxWidth-1, maxHeight-1],
    [0, maxHeight-1]], dtype="float32")
# compute the perspective transform matrix and then apply it
transformMatrix = cv2.getPerspectiveTransform(rect, dst)
# transform ROI
scan = cv2.warpPerspective(orig, transformMatrix, (maxWidth, maxHeight))
# lets see the wraped document
cv2.imshow("Scaned",scan)
cv2.waitKey(0)
cv2.destroyAllWindows()

#6. Final Steps------------
# convert to gray
scanGray = cv2.cvtColor(scan, cv2.COLOR_BGR2GRAY)
# display final gray image
cv2.imshow("scanGray", scanGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ------------------------------
# convert to black/white with high contrast for documents
from skimage.filters import threshold_local
# increase contrast incase its document
T = threshold_local(scanGray, 9, offset=8, method="gaussian")
scanBW = (scanGray > T).astype("uint8") * 255
# display final high-contrast image
cv2.imshow("scanBW", scanBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

