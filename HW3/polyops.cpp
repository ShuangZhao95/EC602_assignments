#include <vector>
typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a, const Poly &b) {

  int len_a = a.size(), len_b = b.size();
  Poly c(max(len_a, len_b));

  for(int i = 0; i < len_a; i++) {
    c[i] += a[i];
  }
  for(int i = 0; i < len_b; i++) {
    c[i] += b[i];
  }
  for(int i = max(len_a, len_b) - 1; i > 0; i--) {
    if(c[i] == 0) {
      c.pop_back();
    } else {
      break;
    }
  }
  return c;
};

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a, const Poly &b) {

  int len_a = a.size(), len_b = b.size();
  Poly c(len_a + len_b);
  for(int i = 0; i < len_a; i++) {
    for(int j = 0; j < len_b; j++) {
      c[i + j] += a[i] * b[j];
    }
  }
  for(int i = len_a + len_b - 1; i > 0; i--) {
    if(c[i] == 0) {
      c.pop_back();
    } else {
      break;
    }
  }
  return c;
};

// Copyright year Shuang Zhao zs1995@bu.edu