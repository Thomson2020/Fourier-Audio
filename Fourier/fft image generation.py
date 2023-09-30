import numpy as np
import matplotlib.pyplot as plt

# Define the size of the image
width, height = 512, 512

# Generate a random complex image in the frequency domain
# You can modify this to create different patterns
frequency_domain = np.random.rand(width, height) + 1j * np.random.rand(width, height)

# Perform the inverse FFT to obtain the image in the spatial domain
image = np.fft.ifft2(frequency_domain)

# Take the absolute value to get the magnitude (brightness) of the image
image_magnitude = np.abs(image)

# Display the generated image
plt.figure(figsize=(6, 6))
plt.imshow(image_magnitude, cmap='gray')
plt.title('Generated Image using FFT')
plt.axis('off')
plt.show()
