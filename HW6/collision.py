#!/usr/bin/env python
# Copyright 2017 Shuang Zhao zs1995@bu.edu

import sys

shuru = sys.stdin.read()

def collision(i1,i2):
	v1= [a[i1][3], a[i1][4]]
	v2= [a[i2][3], a[i2][4]]
	x1= [a[i1][1], a[i1][2]]
	x2= [a[i2][1], a[i2][2]]
	vv1 = [(v1[0]-((v1[0]-v2[0])*(x1[0]-x2[0])+(v1[1]-v2[1])*(x1[1]-x2[1]))*(x1[0]-x2[0])/100),(v1[1]-((v1[0]-v2[0])*(x1[0]-x2[0])+(v1[1]-v2[1])*(x1[1]-x2[1]))*(x1[1]-x2[1])/100)]
	vv2 = [(v2[0]-((v2[0]-v1[0])*(x2[0]-x1[0])+(v2[1]-v1[1])*(x2[1]-x1[1]))*(x2[0]-x1[0])/100),(v2[1]-((v2[0]-v1[0])*(x2[0]-x1[0])+(v2[1]-v1[1])*(x2[1]-x1[1]))*(x2[1]-x1[1])/100)]
	a[i1][3] = vv1[0]
	a[i1][4] = vv1[1]
	a[i2][3] = vv2[0]
	a[i2][4] = vv2[1]

def calculate_time(i1,i2):
	A = (a[i1][3]-a[i2][3])**2 + (a[i1][4]-a[i2][4])**2
	if(A==0):
		return 0
	B = 2*(a[i1][1]-a[i2][1])*(a[i1][3]-a[i2][3])+ 2*(a[i1][2]-a[i2][2])*(a[i1][4]-a[i2][4])
	C = (a[i1][1]-a[i2][1])**2 +(a[i1][2]-a[i2][2])**2 -100
	global ttt
	tt=0xffffffff
	if(A!=0):
		if ((B**2 - 4*A*C) >= 0):
			delta=(B**2 - 4*A*C)**0.5
			if (-B - delta) / (2*A)>=0:
				tt=(-B - delta) / (2*A)
			elif (-B + delta) / (2*A)>=0:
				tt=(-B + delta) / (2*A)
	if(tt==0 and ((0.0000000000000000000001)*A+0.00000000001*B+C)>0):
		tt=0xffffffff
	if tt!=0xffffffff:
		d[i1][i2] = tt
	if tt==0xffffffff:
		d[i1][i2] = -1
	if(tt<ttt):
		ttt = tt
		id_do[0] = i1
		id_do[1] = i2

def traverse0():
	global ttt
	ttt = 0xffffffff
	global id_do
	id_do = [-1,-1]
	for i in range(0,len_a_1):
		for j in range(i+1,len_a):
			calculate_time(i,j)
	if(ttt==0xffffffff):
		ttt = -1
	
def traverse():
	global ttt
	ttt = 0xffffffff
	global id_do
	id_do = [-1,-1]
	for i in range(0,len_a_1):
		for j in range(i+1,len_a):
			if(i==id1 or j==id2 or i==id2 or j==id1):
				calculate_time(i,j)
			else:
				if(d[i][j] != -1):
					d[i][j] -= kk
				if(d[i][j] < ttt and d[i][j]!=-1):
					ttt = d[i][j]
					id_do[0] = i
					id_do[1] = j
	if(ttt==0xffffffff):
		ttt = -1

def main():
	global a
	global t
	# shuru_checker   start:
	a = shuru.splitlines(True)
	global len_a
	len_a = len(a)
	global len_a_1
	len_a_1 = len_a-1
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
	for i in range(0, len_a):
		a[i] = a[i].split()
		if (len(a[i]) != 5):
			exit (1)
		for j in range (1,5):
			try:
				a[i][j] = float(a[i][j])
			except:
				exit (1)
	# end

	global T
	T = 0
	time = sorted(t)
	for i in range(len(time)):
		if(time[0]<0):
			del(time[0])
	global d
	d = [[-1 for i in range(len_a)] for j in range(len_a)]

	global kk
	global id1
	global id2
	kk = 0
	id1 = -1
	id2 = -1
	count = 0
	while (len(time)!= 0):
		if(count==0):
			traverse0()
		else:
			traverse()
		kk = ttt
		id1 = id_do[0]
		id2 = id_do[1]
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
		count +=1
    
if __name__ == '__main__':
    main()
