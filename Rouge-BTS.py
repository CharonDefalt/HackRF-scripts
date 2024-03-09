import pyhackrf
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
sample_rate = 2e6  # 2 MHz sample rate
center_freq = 1e9  # 1 GHz center frequency
num_samples = 1024  # Number of samples to capture

# Open HackRF device
hackrf = pyhackrf.HackRF()

# Configure HackRF
hackrf.sample_rate = sample_rate
hackrf.center_freq = center_freq
hackrf.rxvga_gain = 20

# Start HackRF RX stream
hackrf.receive()

# Capture samples
samples = hackrf.read_samples(num_samples)

# Close HackRF device
hackrf.close()

# Convert samples to numpy array
samples = np.array(samples)

# Plot FFT of captured signal
plt.figure()
plt.psd(samples, NFFT=1024, Fs=sample_rate/1e6, Fc=center_freq/1e6)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power/Frequency (dB/Hz)')
plt.title('FFT of Captured Signal')
plt.show()
