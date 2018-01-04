import sys
if len(sys.argv)>4:
    for i in range(1,5):	
        sys.stdout.write (sys.argv[i]+'\n') 
    for i in range(5,len(sys.argv)):
        sys.stderr.write (sys.argv[i]+'\n') 
else:
    for i in range(1,len(sys.argv)):
        sys.stdout.write(sys.argv[i]+'\n')
# Copyright year ShuangZhao zs1995@bu.edu