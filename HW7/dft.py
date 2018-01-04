# Copyright 2017 Shuang Zhao zs1995@bu.edu
# Copyright 2017 Xintong Hao hxtong@bu.edu

from numpy import zeros, exp, array, pi


def DFT(x):
	try:
		array(x,dtype = complex)
	except:
		raise ValueError
	try:
		N=len(x)
	except:
		raise ValueError
	X = zeros(N,dtype =complex)
	for k in range(0,N):
		a=0
		for n in range(0,N):
			a += x[n]*exp(-2j*pi*n*k/N)
		X[k] = a
	return(X)

def main():
	a = [1,2j,3j]
	print(DFT(a))


if __name__ == '__main__':
    main()