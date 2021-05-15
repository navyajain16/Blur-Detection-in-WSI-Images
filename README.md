# Blur-Detection-in-WSI-Images
This is a repository for Blur detection in sky/cloud images.

This project was tested on python 3.8 and Windows 10 environment.

In this paper we have proposed a method to detect blur in sky/ cloud images by use of a marker which is a stable object that does not change its position with time. 
This marker can be cropped out from the image and then used for detection.

This can be done in following steps:

(1) Add or select an external static marker in the field of view of capturedimages.

(2) Crop the area containing the static marker from the captured image.

(3) Detect if the external staticmarker is blurred or non-blurred using a blur-detection metric.

We have used 2 metrics : Laplacian and Fast Fourier Transform (FFT) method.

## Scripts

- ***Laplacian.py:*** This file contains the code for laplacian operator used.

- ***fft.py:*** This file contains the code for FFT operator used.

- ***req.txt:*** This file contains list of all the libraries required for this project.


