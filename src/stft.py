import numpy
import scipy
from numpy import fft

def stft(x, fs, framesz, hop):
    """ Get the stft of a signal x
    x : array_like
        The signal
    fs : int
        The sampling rate of x
    framesz : int
        The window/fft length in samples
    hop : int
        The hop distance in samples
    """
    framesamp = int(framesz*fs)
    x = numpy.append(numpy.zeros(framesz), x)
    x = numpy.append(x, numpy.zeros(framesz))
    w = scipy.hanning(framesz)
    X = scipy.array([scipy.fft(w*x[i:i+framesz]) 
                     for i in range(0, len(x)-framesz, hop)])
    return X

def istft(X, fs, T, hop):
    """ Transform an array of spectra to the original signal
    """
    x = scipy.zeros(T*fs)
    framesamp = X.shape[1]
    hopsamp = int(hop*fs)
    for n,i in enumerate(range(0, len(x)-framesamp, hopsamp)):
        x[i:i+framesamp] += scipy.real(scipy.ifft(X[n]))
    return x
