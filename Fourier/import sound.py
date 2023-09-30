import wave, struct
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np  

sample_rate, audio_data = wavfile.read("resulthello.wav")
dft_result=np.fft.fft(audio_data)

frequencies= np.fft.fftfreq(len(dft_result), 1 / sample_rate)
plt.figure(figsize=(10,6))
plt.plot(frequencies[:len(frequencies)//2],np.abs(dft_result[:len(dft_result)//2]))
plt.xlabel('freq in Hz')
plt.ylabel('magnitutde')
plt.xlim(0, sample_rate//2)
plt.show()
