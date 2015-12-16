import numpy as np
import scipy

def analyze(X, ampCut, lengthCut):
  tracks = np.zeros(X.shape)
  

def peakDetection(mX, threshold):
  """ Largely copied form sms-tools UF.peakDetection
  mX : array_like, int
    The magnitude spectrum of a DFT
  threshold: float
    A value between 0. and 1. representing the minimum amplitude of a peak
  """
  thresh = np.where(mX[1:-1]>threshold, mX[1:-1], 0);             # locations above threshold
  next_minor = np.where(mX[1:-1]>mX[2:], mX[1:-1], 0)     # locations higher than the next one
  prev_minor = np.where(mX[1:-1]>mX[:-2], mX[1:-1], 0)    # locations higher than the previous one
  ploc = [thresh[i] if (thresh[i] > 0 and next_minor[i] > 0 and prev_minor[i] > 0) else 0 for i in range(len(thresh))]
  return ploc

 
