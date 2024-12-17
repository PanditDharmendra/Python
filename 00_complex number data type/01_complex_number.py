import numpy as np
import matplotlib.pyplot as plt

# Time domain signal
t = np.linspace(0, 1, 500)
signal = np.cos(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 20 * t) * 1j  # Signal with real and imaginary parts

# Plot the real and imaginary components
plt.plot(t, signal.real, label="Real part")
plt.plot(t, signal.imag, label="Imaginary part", linestyle='--')
plt.legend()
plt.show()
