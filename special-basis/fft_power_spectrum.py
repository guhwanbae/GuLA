# Author  : Gu-hwan Bae
# Summary : Visualize frequency elements by using descrete fourier transform.

import gula.fourier as gfourier
import numpy as np
import matplotlib.pyplot as plt

# The number of samples
N = 4096
# Frequency of sinusoidal signal
freq = 60
# Sample time
timestep = .001
func = lambda x: np.sin(2*np.pi*freq*timestep*x)
xt = np.arange(N)
yt = func(xt)

#yf = gfourier.dft(yt)
yf = gfourier.fft(yt)

#Calculate power spectrum to visualize frequency elements.
psd = np.abs(yf) ** 2
xf = np.fft.fftfreq(N, d=timestep)

#Rescale xt array which represent a unit second.
xt = xt * timestep

fig, ax = plt.subplots(nrows=2, ncols=1)
fig.tight_layout()

ax[0].set_title('Sinusoidal')
ax[0].set_xlabel('s, seconds')
ax[0].set_ylabel('mA')
ax[0].set_xlim([0, 3/freq])
ax[0].plot(xt, yt, color='b')
ax[0].grid()

ax[1].set_title('Frequency power spectrum')
ax[1].set_xlim([-2*freq, 2*freq])
ax[1].set_xlabel('Hz, hertz')
ax[1].set_ylabel('mW')
ax[1].plot(xf, psd, color='r')
ax[1].grid()

plt.show()
