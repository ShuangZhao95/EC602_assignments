x=[]
x=input().split(' ')
len_x=len(x)
h=[]
h=input().split(' ')
len_h=len(h)
k=len_x+len_h-1
import numpy as np
y=np.zeros(k)
for i in range(0,len_x):
	for j in range(0,len_h):
		y[i+j]+=float(x[i])*float(h[j])
for i in range(0,k):
	print(y[i],end =' ')
print(' ')
        
        


# Copyright year Shuang Zhao zs1995@bu.edu