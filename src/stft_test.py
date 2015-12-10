import numpy
import unittest
import scipy
from scipy import sin
from scipy.signal import sawtooth
from stft import stft, istft

class TestSTFT(unittest.TestCase):
  def test_invertable(self):
    x = sawtooth(numpy.linspace(0, 1, 44100) * 2 * numpy.pi * 10)
    X = stft(x, 1024)
    xi = istft(X, len(x))
    self.assertTrue(len(xi) == len(x))
    self.assertTrue(numpy.allclose(xi, x, 1e-01))

  def test_consistency(self):
    x = sin(scipy.linspace(0,1,44100) * 2 *  scipy.pi * 440)
    framesz = 1024
    X = stft(x, framesz)
    indices = [numpy.argmax(X[i][:framesz/2]) for i in range(len(X))]
    previous = indices[0]
    for val in indices[1:]:
      self.assertTrue(abs(abs(val)-abs(previous)) <= 1)
      previous = val

if __name__ == '__main__':
  unittest.main()
