import numpy
import scipy
from numpy import fft

def stft(x,framesz):
    """ Get the stft of a signal x
    x : array_like
        The signal
    framesz : int
        The window/fft length in samples
    """
    hop = int(float(framesz)/2)
    x = numpy.append(numpy.zeros(framesz), x) # Pad so we can reconstruct the whole signal
    x = numpy.append(x, numpy.zeros(framesz))
    w = scipy.hanning(framesz)
    X = scipy.array([scipy.fft(w*x[i:i+framesz]) 
                     for i in range(hop, len(x)-(framesz), hop)])
    return X

def istft(X, N):
    """ Transform an array of spectra to the original signal
    """
    framesz = X.shape[1]
    hop = int(float(framesz)/2)
    x = scipy.zeros(N + (2*framesz))
    for n,i in enumerate(range(hop, len(x)-(framesz+hop), hop)):
        x[i:i+framesz] += scipy.real(scipy.ifft(X[n]))
    return x[framesz:-framesz]
