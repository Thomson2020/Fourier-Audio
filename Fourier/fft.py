import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from pydub import AudioSegment

audio_file = "hello.wav"
sample_rate, audio_data = wavfile.read(audio_file)

# Perform Fourier Transform
fft_result = np.fft.fft(audio_data)
fft_freqs = np.fft.fftfreq(len(audio_data), 1 / sample_rate)

plt.figure(figsize=(12, 6))
plt.plot(fft_freqs, np.abs(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Fourier Transform of Audio")
plt.show()

edited_audio_data = np.fft.ifft(fft_result)
output_audio_file = "hello_res.mp3"
edited_audio_data = np.int16(edited_audio_data.real)  # Convert back to integer type
wavfile.write(output_audio_file, sample_rate, edited_audio_data)

# Convert the WAV file to MP3
edited_audio = AudioSegment.from_wav(output_audio_file)
edited_audio.export(output_audio_file, format="mp3")
