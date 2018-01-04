# Copyright 2017 Shuang Zhao zs1995@bu.edu
import sys
import numpy as np

shuru = sys.stdin.read()

def collision(i1,i2):
	v1= np.array([a[i1][3], a[i1][4]])
	v2= np.array([a[i2][3], a[i2][4]])
	x1= np.array([a[i1][1], a[i1][2]])
	x2= np.array([a[i2][1], a[i2][2]])
	vv1= v1-np.dot((v1-v2), (x1-x2))*(x1-x2)/100
	vv2= v2-np.dot((v2-v1), (x2-x1))*(x2-x1)/100
	a[i1][3] = vv1[0]
	a[i1][4] = vv1[1]
	a[i2][3] = vv2[0]
	a[i2][4] = vv2[1]


def calculate_time(i1,i2):
	A = (a[i1][3]-a[i2][3])**2 + (a[i1][4]-a[i2][4])**2
	B = 2*(a[i1][1]-a[i2][1])*(a[i1][3]-a[i2][3])+ 2*(a[i1][2]-a[i2][2])*(a[i1][4]-a[i2][4])
	C = (a[i1][1]-a[i2][1])**2 +(a[i1][2]-a[i2][2])**2 -100
	global ttt
	tt=0xffffffff
	if(A!=0):
		if ((B**2 - 4*A*C) >= 0):
			if (-B - (B**2 - 4*A*C)**0.5) / (2*A)>=0:
				tt=(-B - (B**2 - 4*A*C)**0.5) / (2*A)
			elif (-B + (B**2 - 4*A*C)**0.5) / (2*A)>=0:
				tt=(-B + (B**2 - 4*A*C)**0.5) / (2*A)
	else:
		if(B!=0):
			if((-C)/B)>=0:
				tt= (-C)/B
	if(tt==0 and ((0.00000000001**2)*A+0.00000000001*B+C)>0):
		tt=0xffffffff
	if(tt<ttt):
		ttt = tt
		id_do[0] = i1
		id_do[1] = i2
		
def traverse():
	global ttt
	ttt = 0xffffffff
	global id_do
	id_do = [-1,-1]
	for i in range(0,len_a-1):
		for j in range(i+1,len_a):
			calculate_time(i,j)
	if(ttt==0xffffffff):
		ttt = -1

def main():
	global a
	global t
	# shuru_checker   start:
	a = shuru.splitlines(True)
	t = sys.argv
	del t[0]
	if(len(t)==0):
		exit (2)
	for i in range (0, len(t)):
		try:
			t[i] = float(sys.argv[i])
		except:
			exit (2)
	if max(t)<0:
		exit (2)
	for i in range(0, len(a)):
		a[i] = a[i].split(' ')
		if (len(a[i]) != 5):
			exit (1)
		for j in range (1,5):
			try:
				a[i][j] = float(a[i][j])
			except:
				exit (1)
	# end
	global len_a
	len_a = len(a)
	global T
	T = 0
	time = sorted(t)
	for i in range(len(time)):
		if(time[0]<0):
			del(time[0])

	while (len(time)!= 0):
		traverse()
		while ((time[0] <= (T + ttt)) or (ttt==-1)):
			b = [[0 for i in range(5)] for j in range(len_a)]
			for i in range(len_a):
				b[i][0] = a[i][0]
				b[i][1] = a[i][1] + a[i][3]*(time[0]-T)
				b[i][2] = a[i][2] + a[i][4]*(time[0]-T)
				b[i][3] = a[i][3]
				b[i][4] = a[i][4]

			print(time[0])
			for i in range(len_a):
				for j in range(5):
					print(str(b[i][j]), end=' ')
				print()

			del(time[0])
			if(len(time) == 0):
				break
		if(len(time) != 0):
			for i in range(0,len_a):
				a[i][1] = a[i][1] + a[i][3]*ttt
				a[i][2] = a[i][2] + a[i][4]*ttt
			T += ttt
			
			collision(id_do[0], id_do[1])
    
if __name__ == '__main__':
    main()
