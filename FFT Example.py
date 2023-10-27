import numpy as np
from scipy.fft import fft,fftfreq
import matplotlib.pyplot as plt
import pandas as pd
#excel data read
dr= pd.read_excel("fft_data.xlsx")
plt.figure(figsize = (12, 6))
plt.subplot(121)
acceleration=dr['acc']
accelerations=np.array(acceleration)
time=dr["sn"]
plt.plot( dr["sn"],dr["acc"], "r")
plt.xlabel("Time(s)")
plt.ylabel("Acceleration")
plt.grid()
plt.xlim(left=0)
plt.text(-2,-50,"Test1 -Channel 01", )
#fft process
ts=0.0001
acc_fft=fft(accelerations)
N=len(acceleration)
normalize=N/2
normalize_fft=np.abs(acc_fft)/normalize
n=np.arange(N)
delta_f=(1/(N*ts))
freq=n*delta_f
plt.subplot(122)
plt.plot(freq,normalize_fft,"b",color="b",linewidth="0.6" )
plt.xlabel("Frequency(Hz)")
plt.ylabel('FFT Amplitude')
plt.grid()
plt.ylim(bottom=0)

plt.show()

