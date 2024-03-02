#pragma once
#include <stdbool.h>
#ifndef COMPLEX_NUMBER_H
#define COMPLEX_NUMBER_H

struct Complex{
	float real;
	float imag;
};

Complex complex_create(float real, float imag);
float get_real(Complex c);
float get_imag(Complex c);
void set_real(Complex* c, float real);
void set_imag(Complex* c, float imag);
void complex_display(Complex c);
Complex complex_add(Complex c1, Complex c2);
Complex complex_subtract(Complex c1, Complex c2);
Complex complex_multiply(Complex c1, Complex c2);
bool complex_equals(Complex c1, Complex c2);
Complex complex_conjugate(Complex c);
void complex_scalar_mult(Complex* c, float s);
float complex_mag(Complex c);
float complex_phase(Complex c);
void complex_to_polar(Complex c, float* r, float* theta);
Complex complex_divide(Complex c1, Complex c2);

#endif /* COMPLEX_NUMBER_H */