// Copyright 2017 Shuang Zhao zs1995@bu.edu

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
struct shuru{
	string id;
	double x;
	double y;
	double vx;
	double vy;
};
string id_0;
string x_0,y_0,vx_0,vy_0;
vector<shuru>a;
vector<double>t;
int len_a;
double d[10000][10000];
double T,kk,ttt;
int id1,id2,count_;
shuru b[10000];
int id_do[2];


void collision(int i1,int i2){
	double v1[2]={a[i1].vx , a[i1].vy};
	double v2[2]={a[i2].vx , a[i2].vy};
	double x1[2]={a[i1].x , a[i1].y};
	double x2[2]={a[i2].x , a[i2].y};
	double vv1[2]={(v1[0]-((v1[0]-v2[0])*(x1[0]-x2[0])+(v1[1]-v2[1])*(x1[1]-x2[1]))*(x1[0]-x2[0])/100),(v1[1]-((v1[0]-v2[0])*(x1[0]-x2[0])+(v1[1]-v2[1])*(x1[1]-x2[1]))*(x1[1]-x2[1])/100)};
	double vv2[2]={(v2[0]-((v2[0]-v1[0])*(x2[0]-x1[0])+(v2[1]-v1[1])*(x2[1]-x1[1]))*(x2[0]-x1[0])/100),(v2[1]-((v2[0]-v1[0])*(x2[0]-x1[0])+(v2[1]-v1[1])*(x2[1]-x1[1]))*(x2[1]-x1[1])/100)};
	a[i1].vx=vv1[0];
	a[i1].vy=vv1[1];
	a[i2].vx=vv2[0];
	a[i2].vy=vv2[1];
}
void calculate_time(int i1,int i2){
	double A = pow((a[i1].vx-a[i2].vx),2)+pow((a[i1].vy-a[i2].vy),2);
	double B = 2*(a[i1].x-a[i2].x)*(a[i1].vx-a[i2].vx)+ 2*(a[i1].y-a[i2].y)*(a[i1].vy-a[i2].vy);
	double C = pow((a[i1].x-a[i2].x),2)+pow((a[i1].y-a[i2].y),2)-100.0;
	double tt=0xffffffff;
	if(A!=0){
		if((pow(B,2)-4*A*C) >= 0){
			double delta = sqrt(pow(B,2)-4*A*C);
			if(((-B-delta)/(2*A))>=0){
				tt=((-B-delta)/(2*A));
			}
			else if(((-B+delta)/(2*A))>=0){
				tt=((-B+delta)/(2*A));
			}
		}
	}
	if(tt==0 && (0.0000000000000000000001*A+0.00000000001*B+C)>0){
		tt=0xffffffff;
	}
	if(tt!=0xffffffff){
		d[i1][i2] = tt;
	}
	if(tt==0xffffffff){
		d[i1][i2] = -1;
	}
	if(tt<ttt){
		ttt=tt;
		id_do[0]=i1;
		id_do[1]=i2;
	}
}
void traverse0(){
	ttt=0xffffffff;
	id_do[0]=-1;
	id_do[1]=-1;
	for(int i=0;i<len_a-1;i++){
		for(int j=i+1;j<len_a;j++){
			calculate_time(i,j);
		}
	}
	if(ttt==0xffffffff){
		ttt=-1;
	}
}
void traverse(){
	ttt=0xffffffff;
	id_do[0]=-1;
	id_do[1]=-1;
	for(int i=0;i<len_a-1;i++){
		for(int j=i+1;j<len_a;j++){
			if(i==id1 || j==id2 || i==id2 || j==id1){
				calculate_time(i,j);
			}
			else{
				if(d[i][j] != -1){
					d[i][j] -= kk;
				}
				if(d[i][j]<ttt && d[i][j]!=-1){
					ttt=d[i][j];
					id_do[0]=i;
					id_do[1]=j;
				}
			}
		}
	}
	if(ttt==0xffffffff){
		ttt=-1;
	}
}
int main(int argc, char *argv[]){
	for(int i=1;i<argc;i++){
		char * e;
		errno = 0;
		double ti=strtod(argv[i], &e);
		if(*e != '\0' || errno != 0){
			exit(2);
		}
		if(ti>=0){
			t.push_back(ti);
		}
	}
	if(t.size()==0){
		exit(2);
	}
	sort(t.begin(),t.end());
	//time ends here
	shuru aa;
	vector<string> row;
	vector<vector<string>> table;
	string line;
	while(getline(cin,line)){
		stringstream ss(line);
		string entry;
		while(ss>>entry){
			row.push_back(entry);
		}
		table.push_back(row);
		row.clear();
	}
	for(int i=0;i<table.size();i++){
		if(table[i].size()!=5){
			exit(1);
		}
		aa.id=table[i][0];
		try{
			aa.x=stod(table[i][1]);
			aa.y=stod(table[i][2]);
			aa.vx=stod(table[i][3]);
			aa.vy=stod(table[i][4]);
		}
		catch(exception &e){
			exit(1);
		}
		a.push_back(aa);
	}
	// a ends here
	len_a=a.size();
	for(int i=0;i<len_a;i++){
		for(int j=0;j<len_a;j++){
			d[i][j]=-1;
		}
	}
	kk=0;id1=-1;id2=-1;
	while(true){
		int fl=0;
		if(count_==0){
			traverse0();
		}
		else{
			traverse();
		}
		kk=ttt;
		id1=id_do[0];
		id2=id_do[1];
		while((t[0]<=(T+ttt))||ttt==-1){
			for(int i=0;i<len_a;i++){
				b[i].id=a[i].id;
				b[i].x=a[i].x+a[i].vx*(t[0]-T);
				b[i].y=a[i].y+a[i].vy*(t[0]-T);
				b[i].vx=a[i].vx;
				b[i].vy=a[i].vy;
			}
			cout<<t[0]<<endl;
			for(int i=0;i<len_a;i++){
				cout<<b[i].id<<" "<<b[i].x<<" "<<b[i].y<<" "<<b[i].vx<<" "<<b[i].vy<<endl;				
			}
			if(t.size()==1){
				fl=1;
				break;
			}
			for(int i=0;i<t.size()-1;i++){
				t[i]=t[i+1];
			}
			t.pop_back();
		}
		if(t.size()==1&&fl==1){
			break;
		}
		if(t.size()!=0){
			for(int i=0;i<len_a;i++){
				a[i].x=a[i].x+a[i].vx*ttt;
				a[i].y=a[i].y+a[i].vy*ttt;
			}
			T +=ttt;
			collision(id_do[0],id_do[1]);
		}
		count_ +=1;
	}



	return 0;
}