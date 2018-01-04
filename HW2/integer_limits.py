Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for i in range(1,9):
    print(Table.format(i,2**(8*i)-1,-(2**(8*i-1)),2**(8*i-1)-1))
 
# Copyright year ShuangZhao zs1995@bu.edu