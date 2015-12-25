import numpy as np
import matplotlib.pyplot as plt
from stft import stft, istft

def spectrogram(X, fs=44100):
  """ For plotting a numpy array representing a spectrogram
  """
  # plot magnitude spectrogram
  numFrames = len(X)
  frmTime = H*np.arange(numFrames)/float(fs)                             
  binFreq = fs*np.arange(N*maxplotfreq/fs)/N  
  plt.pcolormesh(frmTime, binFreq, np.transpose(mX[:,:N*maxplotfreq/fs+1]))
  plt.xlabel('time (sec)')
  plt.ylabel('frequency (Hz)')
  plt.title('magnitude spectrogram')
  plt.autoscale(tight=True)

def plotDifference(signal):
  X = stft(signal, 1024)
  xo = istft(X, len(signal))
  plt.plot(abs(abs(signal)-abs(xo)))
  plt.show()
