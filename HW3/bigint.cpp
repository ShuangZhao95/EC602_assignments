#include <string>
#include <vector>

typedef string BigInt;

BigInt multiply_int(const BigInt &a, const BigInt &b) {
  int k;
  BigInt s;
  int len_a = a.length(), len_b = b.length();
  vector<int> c(len_a + len_b);
  if(a == "0" || b == "0") {
    s = "0";
    return s;
  } else {
    for(int i = len_a - 1; i >= 0; i--) {
      for(int j = len_b - 1; j >= 0; j--) {
        c[i + j + 1] += (a[i] - 48) * (b[j] - 48);
        k = c[i + j + 1] / 10;
        c[i + j] += k;
        c[i + j + 1] = c[i + j + 1] % 10;
      }
    }
    if(c[0] == 0) {
      s.resize(len_a + len_b - 1);
      for(int i = 1; i < (len_a + len_b); i++) {
        s[i - 1] = c[i] + 48;
      }
    } else {
      s.resize(len_a + len_b);
      for(int i = 0; i < (len_a + len_b); i++) {
        s[i] = c[i] + 48;
      }
    }
    return s;
  }
};

// Copyright year Shuang Zhao zs1995@bu.edu