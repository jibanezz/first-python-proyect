 

# Python program to read an write an image
 
import imageio as iio
 
# read an image 
img = iio.imread("kids smile.jpg")

import matplotlib.pyplot as plt

import cv2
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_image)

plt.show()

# remove noise

blur_image = cv2.GaussianBlur(gray_image,(5,5),6)

plt.imshow(blur_image)

plt.show()


#detect edges

edges = cv2.Canny(blur_image,100,200)

plt.imshow(edges)

plt.show()

#dilate edges

import numpy as np

kernel = np.ones((5,5),np.uint8)

dilated_edges = cv2.dilate(edges,kernel,iterations = 1)

plt.imshow(dilated_edges)

plt.show()

