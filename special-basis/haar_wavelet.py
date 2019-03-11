# Author  : Gu-hwan Bae
# Summary : Wavelet transform and applications by using gula.wavelet module.

import gula.wavelet as gwavelet
import numpy as np

# Case I : Haar wavelet transform for 1D signals.
data = np.array([4, 5, 3, 7, 4, 5, 9, 7, 2, 3, 3, 5, 0, 0, 0, 0])

w = gwavelet.haar(data)
data_inv = gwavelet.haarinv(w)

print('data =', data)
print('wavelet coefficients =', w)
print('data_inv =', data_inv)

# Suppress wavelet coefficient entries which less than threshold,
# and calculate its sparsity.
suppressed = gwavelet.suppress(w, 1.0)
print('suppressed =', suppressed)
print('sparsity =', gwavelet.sparsity(suppressed))

normalized = gwavelet.normalizeHaar(w)
print('normalized =', normalized)
print('unnormalized =', gwavelet.unnormalizedHaar(normalized))
