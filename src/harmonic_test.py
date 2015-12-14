import numpy
import unittest
import scipy

from harmonic import analyze
from stft import stft, istft
class TestHarmonic(unittest.TestCase):
  def test_shape(self):
    x = scipy.sin(scipy.linspace(0,1,44100)*scipy.pi*2*440)
    X = stft(x, 1024)
    tracks = analyze(X)
    assertTrue(tracks.shape == X.shape)

  def test_number_of_tracks(self):
    x = scipy.sin(scipy.linspace(0,1,44100)*scipy.pi*2*440)
    X = stft(x,1024)
    tracks = analyze(X)
    assertTrue(1 == reduce(lambda x,y: if y then x + 1 else x, map(lambda x: x != 0, tracks)))

if __name__ == '__main__':
  unittest.main()

