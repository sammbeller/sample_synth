import imp
import numpy as np
import scipy
import matplotlib.pyplot as plt

stft = imp.load_source('stft', 'src/stft.py')
harmonic = imp.load_source('harmonic', 'src/harmonic.py')
sinwave = scipy.sin(scipy.linspace(0,1,44100)*2*scipy.pi*440)
