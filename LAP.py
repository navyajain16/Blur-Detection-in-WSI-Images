# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:04:14 2021

@author: navya
"""

# import the necessary packages
from imutils import paths
import argparse
import cv2
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

images = "patch"
Threshold = 12

for imagePath in paths.list_images(images):
	# load the image, convert it to grayscale, and compute the
	# focus measure of the image using the Variance of Laplacian
	# method
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)

	if fm > Threshold:
		text = imagePath+" - Not Blurry: "+str(fm)
		print(imagePath+" - Not Blurry: "+str(fm))
 
	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
	if fm < Threshold:
		text = imagePath+" - Blurry: "+str(fm)
		print(imagePath+" - Blurry: "+str(fm))