import numpy as np
import matplotlib.pyplot as plt


def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)


time = np.arange(0, 10, 0.001)
sin1 = sin_wave(1, 10, time)
sin2 = sin_wave(2, 5, time)
sin3 = sin_wave(4, 1, time)

time.shape

'''
plt.figure(figsize=(12,5))
plt.plot(time, sin1, label=r"$S/sin {20\pi} t$", color='red')
plt.plot(time, sin2, label=r"$S2/sin {10\pi} t$", color='blue')
plt.plot(time, sin3, label=r"$S4/sin {2\pi} t$", color='green')
plt.legend();
plt.grid();
plt.show()

sin_sum = sin1 + sin2 + sin3

plt.figure(figsize=(12,5))
plt.plot(time, sin_sum)
plt.grid();
plt.show()
'''

sin_sum = sin1 + sin2 + sin3

n = len(sin_sum)
k = np.arange(n)
Fs = 1/0.001
T = n/Fs
freq = k/T
freq = freq[range(int(n/2))]

Y = np.fft.fft(sin_sum)/n
Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2,1,figsize=(12,8))
ax[0].plot(time,sin_sum)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude'); ax[0].grid(True)
ax[1].plot(freq,abs(Y),'r',linestyle='',marker='^')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('Y(freq)')
ax[1].vlines(freq,[0],abs(Y))
ax[1].set_xlim([0,20]); ax[1].grid(True)
plt.show()
