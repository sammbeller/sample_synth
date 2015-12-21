import numpy as np
import scipy

def analyze(X, ampCut, lengthCut):
  tracks = np.zeros(X.shape)
  

def peakDetection(mX, threshold):
  """ Largely copied form sms-tools UF.peakDetection
  This method ignores the first and last bins
  mX : array_like, int
    The magnitude spectrum of a DFT
  threshold: float
    A value between 0. and 1. representing the minimum amplitude of a peak
  """
  thresh = np.where(mX[1:-1]>threshold, mX[1:-1], 0);     # locations above threshold
  next_minor = np.where(mX[1:-1]>mX[2:], mX[1:-1], 0)     # locations higher than the next one
  prev_minor = np.where(mX[1:-1]>mX[:-2], mX[1:-1], 0)    # locations higher than the previous one
  ploc = [thresh[i] if (thresh[i] > 0 and next_minor[i] > 0 and prev_minor[i] > 0) else 0 for i in range(len(thresh))]
  return ploc

def parabolicInterpolation(mX, pX, ploc):
  """ Largely copied form sms-tools UF.peakInterp
  Interpolate peak values using parabolic interpolation
  mX, pX: magnitude and phase spectrum, ploc: locations of peaks
  returns iploc, ipmag, ipphase: interpolated peak location, magnitude and phase values
  """
  val = mX[ploc]                                          # magnitude of peak bin
  lval = mX[ploc-1]                                       # magnitude of bin at left
  rval = mX[ploc+1]                                       # magnitude of bin at right
  iploc = ploc + 0.5*(lval-rval)/(lval-2*val+rval)        # center of parabola
  ipmag = val - 0.25*(lval-rval)*(iploc-ploc)             # magnitude of peaks
  ipphase = np.interp(iploc, np.arange(0, pX.size), pX)   # phase of peaks by linear interpolation
  return iploc, ipmag, ipphase

 
