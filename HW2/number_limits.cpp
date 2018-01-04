#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>

int main(){
  double Rs,Ri,Rm;

  // calculate Rs, Ri, and Rm for half/binary16 vs int16_t
  Rs=1/(pow(2,-14));
  Rm=(2-pow(2,-10))*pow(2,15)/(pow(2,15)-1);
  Ri=(pow(2,15)-1)/pow(2,11);
  std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
  Rs=1/(pow(2,-126));
  Rm=(2-pow(2,-23))*pow(2,127)/(pow(2,31)-1);
  Ri=(pow(2,31)-1)/pow(2,24);
  std::cout<< "32 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for double/binary64 vs int64_t
  Rs=1/(pow(2,-1022));
  Rm=(2-pow(2,-52))*pow(2,1023)/(pow(2,63)-1);
  Ri=(pow(2,63)-1)/pow(2,53);
  std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;
  
  return 0;
}


// Copyright year Shuang Zhao zs1995@bu.edu