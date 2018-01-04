# Copyright 2017 Shuang Zhao zs1995@bu.edu
# Copyright 2017 Xintong Hao hxtong@bu.edu
import scipy.io.wavfile as wavfile
from numpy import *;

def dialer(file_name,frame_rate,phone,tone_time):
	fl=array([941,697,697,697,770,770,770,852,852,852,941,941])
	fh=array([1336,1209,1336,1477,1209,1336,1477,1209,1336,1477,1209,1477])
	data=array([])
	l=len(phone)
	for i in range(l):
		if(phone[i]=='*'):
			n=10
		elif(phone[i]=='#'):
			n=11
		else:
			n=int(phone[i])
		t = linspace(0,tone_time,int(tone_time*frame_rate),endpoint=False)

		d = sin(2*pi*fl[n]*t)+sin(2*pi*fh[n]*t)
		data=append(data,d)
	print(len(t))
	print(len(data))
	wavfile.write(file_name, frame_rate, data.astype(float32))

def main():
	dialer('ok.wav',8000,'1234567890',0.2)

if __name__ == '__main__':
    main()