# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:48:31 2021

@author: navya
"""

import matplotlib.pyplot as plt
import numpy as np
from imutils import paths
def detect_blur_fft(image, size=40, thresh=-15, vis=False):
    (h, w) = image.shape
    (cX, cY) = (int(w / 2.0), int(h / 2.0))
    fft = np.fft.fft2(image)
    fftShift = np.fft.fftshift(fft)
    if vis:
        magnitude = 20 * np.log(np.abs(fftShift))
        (fig, ax) = plt.subplots(1, 2, )
        ax[0].imshow(image, cmap="gray")
        ax[0].set_title("Input")
        ax[0].set_xticks([])
        ax[0].set_yticks([])
        ax[1].imshow(magnitude, cmap="gray")
        ax[1].set_title("Magnitude Spectrum")
        ax[1].set_xticks([])
        ax[1].set_yticks([])
        plt.show()
        fftShift[cY - size:cY + size, cX - size:cX + size] = 0
        fftShift = np.fft.ifftshift(fftShift)
        recon = np.fft.ifft2(fftShift)
        magnitude = 20 * np.log(np.abs(recon))
        mean = np.mean(magnitude)
        return (mean, mean <= thresh)
    
import cv2
images = "CLEARR"
Threshold = 13
for imagePath in paths.list_images(images):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = (mean, blurry) = detect_blur_fft(gray, size=40,thresh=-4, vis=1 > 0)
    image = np.dstack([gray] * 3)
    color = (0, 0, 255) if blurry else (0, 255, 0)
    text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
    text = text.format(mean)
#cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,color, 2)
    print("[INFO] {}".format(text))