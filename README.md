# Detecting Blurred Ground-based Sky/Cloud Images
With the spirit of reproducible research, this repository contains all the codes required to produce the results in the manuscript:

> M. Jain, N. Jain, Y. H. Lee, S. Winkler, and S. Dev, Detecting Blurred Ground-based Sky/Cloud Images, *under review*.

### Executive summary
In this paper we have proposed a method to detect blurred sky/ cloud images using an external stationary marker. This marker is a stable object that does not change its position with time, and can be seen in the field of view of the camera. We use a cropped version of the entire image containing the marker to classify the image as blurred or non-blurred. 

Our proposed approach is as follows:
1. Add or select an external static marker in the field of view of captured images.
2. Crop the area containing the static marker from the captured image.
3. Detect if the external staticmarker is blurred or non-blurred using a blur-detection metric.

We have used 2 metrics : Laplacian and Fast Fourier Transform (FFT) method.

### Environment 
This project was tested on `python 3.8` using a `Windows 10` environment.

### Scripts
+ `Laplacian.py`: This file contains the code for laplacian operator used.
+ `fft.py`: This file contains the code for FFT operator used.
+ `req.txt`: This file contains list of all the libraries required for this project.
