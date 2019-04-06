# -*- coding: utf-8 -*-
"""Music genre classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m3bTmeO1Ro2cJN2OolRcj2sh88m3Waqw
"""

import scipy
from matplotlib.pyplot import specgram
from scipy.io import wavfile
import os
import matplotlib.pyplot as plt

!git clone https://github.com/Ahanmr/music-genre-classification.git

directory=os.getcwd()+"/music-genre-classification/wav_files"
wave_filename=[]
for filename in os.listdir(directory):
  print(filename)
  wave_file=os.getcwd()+"/music-genre-classification/wav_files/"+str(filename)
  wave_filename.append(wave_file)


wave_filename

# coordinates=[]
# sample_rate=[]
# x=[]
# for file in range(len(wave_filename)):
#   sample_rate,x=scipy.io.wavfile.read(wave_filename[file])
#   coordinates=specgram(x,Fs=sample_rate,xextent=(0,45),cmap='Spectral')

#sampling a rock music wav file
sample_rate,x=scipy.io.wavfile.read(wave_filename[8])
specgram(x,Fs=sample_rate,xextent=(0,45),cmap='Spectral')
plt.show()
print(wave_filename[8])

#sampling a rock music wav file
sample_rate,x=scipy.io.wavfile.read(wave_filename[1])
specgram(x,Fs=sample_rate,xextent=(0,45),cmap='Spectral')
plt.show()
print(wave_filename[1])

#sampling a pop music wav file
sample_rate,x=scipy.io.wavfile.read(wave_filename[6])
specgram(x,Fs=sample_rate,xextent=(0,45),cmap='Spectral')
plt.show()
print(wave_filename[6])

