#!/usr/bin/python

################################################################################
# spectrogram.py wavfilename
# Generates a spectrogram with the given wav file
#
# Reference:
# http://dsp.stackexchange.com/questions/10743/generating-spectrograms-in-python-with-less-noise
################################################################################

from scipy.io import wavfile
import numpy as np
import pylab

def generateSpecgram(filename):
 fs,data = wavfile.read(filename)
 Pxx, f, t, plot = pylab.specgram(
  data,
  NFFT=4096,
  Fs=fs,
  detrend=pylab.detrend_none,
  window=pylab.window_hanning,
  noverlap=int(4096*0.5))
 pylab.ylabel('Frequency [Hz]')
 pylab.xlabel('Time [sec]')
 pylab.title('Spectrogram of CNC Noise')
 pylab.show()

while True:
 try:
  continue
 except KeyboardInterrupt:
  pylab.close('all')
  exit()
