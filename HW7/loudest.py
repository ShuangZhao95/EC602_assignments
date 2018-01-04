# Copyright 2017 Shuang Zhao zs1995@bu.edu
# Copyright 2017 Xintong Hao hxtong@bu.edu
import scipy.io.wavfile as wavfile
import numpy as np 

def loudest_band(music,frame_rate,bandwidth):
	N = music.shape[0]
	BW=int(bandwidth * N / frame_rate)
	FFT = np.fft.fftshift(np.fft.fft(music))
	V = abs(FFT)**2
	index_0 = abs(np.arange(-frame_rate/2 , frame_rate/2, frame_rate/N)).argmin()
	sum_v = np.sum(V[index_0-1:index_0 +BW -1])
	maxsum=0
	max_index=0

	for i in range(index_0, N-BW):
		sum_v = sum_v-V[i-1]+V[i-1+BW]
		if (sum_v>=maxsum) :
			maxsum = sum_v
			max_index = i
	fl = (max_index- index_0)*frame_rate/N
	fh = fl + bandwidth
	
	loudest_f = np.zeros(N)
	for i in range(N):
		if (i in range(max_index, max_index+BW+1)) or (i in range(2*index_0- max_index- BW , 2* index_0 - max_index +1)) :
			loudest_f[i] = 1
		else:
			loudest_f[i] = 0
	filtered_signal = loudest_f*FFT
	loudest = np.real(np.fft.ifft(np.fft.ifftshift(filtered_signal)))
	low = fl
	high = fh

	return (low, high, loudest)

