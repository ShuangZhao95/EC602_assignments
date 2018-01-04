# Copyright year Shuang Zhao zs1995@bu.edu
class Polynomial():
    
    def __init__(self,a=[]):   
        if(a==None or len(a)==0):
            a=[0]
        self.a=a
        self.d={}      
        for i in range (0,len(a)):
            self.d[i]=a[len(a)-1-i]

    def __setitem__(self,key,value):
        if (value!=0):
            self.d[key]=value
        

    def __getitem__(self,key):
        if key in self.d:
            return self.d[key]
        else:
            return 0    
            
        
    def __str__(self):
        return "{}".format(self.d)
    def __repr__(self):
        return str(self)
    
    
    def __add__(self,v):
        y=Polynomial()
        for j in self.d:
            y.d[j]=self.d[j]
        for i in v.d:
            if(i in self.d):
                y.d[i]+=v.d[i]
            else:
                y.d[i]=v.d[i]
        return y
    
    def __sub__(self,v):
        y=Polynomial()
        for i in self.d:
            y.d[i]=self.d[i]
        for i in v.d:
            if(i in self.d):
                y.d[i]-=v.d[i]
            else:
                y.d[i]=-v.d[i]
        return y 
    
    def __mul__(self,v):
        y=Polynomial()
        for i in self.d:
            if(self.d[i]!=0):
                for j in v.d:
                    if(v.d[j]!=0):
                        if((i+j) in y.d):
                            y.d[i+j]+=(self.d[i]*v.d[j])
                        else:
                            y.d[i+j]=(self.d[i]*v.d[j])
        return y
    
    def __eq__(self,v):
        return(self.d==v.d)
    
    def eval(self,v):
        k=0
        for i in self.d:
            k+=(self.d[i]*(v**i))
        return k
    
    def deriv(self):
        y=Polynomial()
        for i in self.d:
            y[i-1]=self.d[i]*i
        return y

                
    
def main():

    print('hi')
    pass
    

if __name__=="__main__":
	main()