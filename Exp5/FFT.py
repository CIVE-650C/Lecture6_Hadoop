
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt
import pandas as pd


# # Intro Example

# In[2]:

# sampling rate
Fs = 150.0  
# sampling interval over 1 time unit
Ts = 1.0 / Fs
# create a grid of time over 1 time unit
t = np.arange(0, 1, Ts)

# frequency of the signal y
# T = 1/f = 0.2 (Period)
f = 5.0
#Amplitude
A = 50.0
# y = A*sin(wt), where w = 2*pi*f
y = A*np.sin(2 * np.pi * f * t)

# plot what the data
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()


# In[5]:

yFFT = np.fft.fft(y)
n = len(yFFT)/2
freq = range(0, n, 1)
yFFT = yFFT[:n]
plt.plot(freq, abs(yFFT))


# ## What if it has two component? (2 different frequencies)

# In[6]:

f2 = f*2 
A2 = A/2
y2 = A2*np.sin(2 * np.pi * f2 * t)
y3 = y + y2

yrange = [-80, 80]
ytick = range(-80, 100, 40)

fig, ax = plt.subplots(3, 1)
plt.tight_layout()

ax[0].plot(t, y)
ax[0].set_ylim(yrange)
ax[0].set_yticks(ytick)
ax[0].grid(True)

ax[1].plot(t, y2)
ax[1].set_ylim(yrange)
ax[1].set_yticks(ytick)
ax[1].grid(True)

ax[2].plot(t, y3)
ax[2].set_ylim(yrange)
ax[2].set_yticks(ytick)
ax[2].grid(True)


# ## Frequency Domain Plot

# In[9]:

y2FFT = np.fft.fft(y2)
n = len(y2FFT)/2
y2FFT = y2FFT[:n]

y3FFT = np.fft.fft(y3)
y3FFT = y3FFT[:n]

fig, ax = plt.subplots(3, 1)
ax[0].plot(freq, abs(yFFT))
ax[1].plot(freq, abs(y2FFT))
ax[2].plot(freq, abs(y3FFT))


# # Square Wave Example: http://mathworld.wolfram.com/FourierSeriesSquareWave.html

# In[7]:

## UDF
def sinSquare(n, x):
    y = 1.0/n * np.sin(n * np.pi * x / 0.5)
    return y


# In[8]:

fig, ax = plt.subplots(3, 1)
ySquare = 0
N = 200
for n in range(1, N, 2):
    y_n = sinSquare(n, t)
    ySquare = (ySquare + y_n)
    ax[0].plot(t, y_n)

#square wave plot
ySquare = ySquare * 4 / np.pi  
ax[1].plot(t, ySquare)

# frequency plot
ySquareFFT = np.fft.fft(ySquare)
ax[2].plot(abs(ySquareFFT[:len(ySquareFFT)/2]))


# # Inverse Fourier Transforms

# ## recall: the simple example yFFT is like

# In[9]:

y = A*np.sin(2 * np.pi * f * t)
yFFT = np.fft.fft(y)
plt.plot(abs(yFFT[:len(yFFT)/2]))


# In[10]:

# inverse conversion
inverseFFT = np.fft.ifft(yFFT)
plt.plot(t, inverseFFT)
plt.grid()


# ## Square Wave Example

# In[11]:

plt.plot(abs(ySquareFFT[:len(ySquareFFT)/2]))


# In[12]:

iFFTSquare = np.fft.ifft(ySquareFFT)
plt.plot(t, iFFTSquare)
plt.grid()


# # Smoothing/Denoise Application

# In[47]:

# adding noise to y
alpha = 1
y_noise = y + np.random.randint(-A/alpha, A/alpha, len(y))
plt.plot(t, y_noise)
plt.plot(t, y, color='r', alpha = 0.3)


# In[48]:

fig, ax = plt.subplots(2, 1)
ax[0].plot(abs(yFFT[:len(yFFT)/2]))

y_noise_FFT = np.fft.fft(y_noise)
ax[1].plot(abs(y_noise_FFT[:len(y_noise_FFT)/2]))


# In[74]:

threshold = 1000
mask = abs(y_noise_FFT) > threshold
y_DEnoise_FFT = y_noise_FFT * mask
y_DEnoise_iFFT = np.fft.ifft(y_DEnoise_FFT)
plt.plot(t, y_DEnoise_iFFT)


# ## Another Smoothing Example

# In[91]:

#Read the data
header = ['date', 'startT', 'endT', 'startSec', 'endSec', 'vol', 'occu','speed']
data = pd.read_csv('I-35 NB at 1st AVE ANKENY-SB-20151228.csv', names = header)
print data.head(10)


# In[92]:

# remove data without any detection
data = data.ix[data['speed']>0, :]
print data.head(10)


# In[105]:

# plot the raw speed data
speed = data['speed']
time = data['startSec']/3600
plt.plot(time, speed, '.')
plt.plot(time, speed, alpha = 0.5)
plt.grid()
plt.xlabel('Time of Day')
plt.ylabel('Speed(mph)')
plt.xlim([0,24])
plt.xticks(range(0, 26, 2))
plt.ylim([20,90])
plt.yticks(range(20, 100, 10))
plt.show()


# In[118]:

# plot its frequency domain
speedFFT= np.fft.fft(speed)
plt.plot(abs(speedFFT[1:len(speedFFT)/2]))
plt.grid()


# In[123]:

# denoise
threshold = 1500
mask = abs(speedFFT) > threshold
speed_DEnoise_FFT = speedFFT * mask
speed_DEnoise_iFFT = np.fft.ifft(speed_DEnoise_FFT)

#plotting
plt.plot(time, speed, alpha = 0.5)
plt.plot(time, speed_DEnoise_iFFT, linewidth=2.0)
plt.grid()
plt.xlabel('Time of Day')
plt.ylabel('Speed(mph)')
plt.xlim([0,24])
plt.xticks(range(0, 26, 2))
plt.ylim([20,90])
plt.yticks(range(20, 100, 10))
plt.show()


# In[ ]:



