import numpy
import unittest
import scipy

from scipy.signal import sawtooth
from stft import stft, istft

class TestSTFT(unittest.TestCase):
  def test_invertable(self):
    x = sawtooth(numpy.linspace(0, 1, 44100) * 2 * numpy.pi * 10)
    X = stft(x, 44100, 1024, 512)
    xi = istft(X, 44100, 1, 512)
    self.assertTrue(numpy.allclose(xi, x))

if __name__ == '__main__':
  unittest.main()
