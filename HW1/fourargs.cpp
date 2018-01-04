#include<iostream>
int main(int argumentscount, char **arguments){
	for(int i=1;i<=4;i++){
	    std::cout<<arguments[i]<<'\n';
    }
    for(int j=5;j<=argumentscount;j++){
    	std::cerr<<arguments[j]<<'\n';
    }
	return 0;
}
// Copyright year ShuangZhao zs1995@bu.edu