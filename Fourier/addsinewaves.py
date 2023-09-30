import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the sine waves
sampling_rate = 1000  # Sampling rate in Hz
duration = 1.0  # Duration of the signal in seconds
frequency1 = 5.0  # Frequency of the first sine wave in Hz
frequency2 = 20.0  # Frequency of the second sine wave in Hz

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the two sine waves
sine_wave1 = np.sin(2 * np.pi * frequency1 * t)
sine_wave2 = np.sin(2 * np.pi * frequency2 * t)

# Add the two sine waves to create a composite signal
composite_signal = sine_wave1 + sine_wave2

# Perform FFT on the composite signal
fft_result = np.fft.fft(composite_signal)
frequencies = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)

# Create a plot to visualize the signals and the FFT result
plt.figure(figsize=(12, 6))

# Plot the composite signal
plt.subplot(3, 1, 1)
plt.plot(t, composite_signal)
plt.title('Composite Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot the individual sine waves
plt.subplot(3, 1, 2)
plt.plot(t, sine_wave1, label='Sine Wave 1')
plt.plot(t, sine_wave2, label='Sine Wave 2')
plt.title('Individual Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Plot the magnitude spectrum (FFT result)
plt.subplot(3, 1, 3)
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_result[:len(fft_result)//2]))
plt.title('Magnitude Spectrum (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
