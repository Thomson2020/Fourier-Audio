import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('wall4.jpg', cv2.IMREAD_GRAYSCALE)

# Perform FFT
fft_result = np.fft.fft2(image)
fft_result_shifted = np.fft.fftshift(fft_result)

# Calculate the magnitude spectrum (logarithmic scale for visualization)
magnitude_spectrum = 20 * np.log(np.abs(fft_result_shifted))

# Display the original image and magnitude spectrum
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()
