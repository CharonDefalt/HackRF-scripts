import pyhackrf
import numpy as np

# Define parameters
sample_rate = 5e6  # 5 MHz sample rate
center_freq = 2.5e9  # 2.5 GHz center frequency (example)
num_samples = 1024  # Number of samples to transmit

# Open HackRF device
hackrf = pyhackrf.HackRF()

# Configure HackRF for transmission
hackrf.sample_rate = sample_rate
hackrf.center_freq = center_freq
hackrf.txvga_gain = 20

# Generate LTE signal samples (example: random noise)
lte_signal = np.random.normal(0, 1, num_samples)  # Example: random noise
lte_signal = lte_signal.astype(np.complex64)  # Convert to complex64 for transmission

# Start HackRF TX stream
hackrf.transmit()

# Transmit LTE signal samples
hackrf.send_samples(lte_signal)

# Close HackRF device
hackrf.close()
