#include <math.h>

#include <stdio.h>



#include "complex_number.h"



Complex complex_create(float real, float imag) {
	Complex c;
	c.real = real;
	c.imag = imag;
	return c;
}
float get_real(Complex c) {
	return c.real;
}
float get_imag(Complex c) {
	return c.imag;

}
void set_real(Complex* c, float real) {
	c->real = real;

}
void set_imag(Complex* c, float imag) {
	c->imag = imag;
}
void complex_display(Complex c) {
	if (c.imag >= 0)
		printf("%.2f +%.2fi\n", c.real, c.imag);
	else
		printf("%.2f -%.2fi\n", c.real,(-1)* c.imag);

}
Complex complex_add(Complex c1, Complex c2) {
	Complex c;
	c.real = c1.real + c2.real;
	c.imag = c1.imag + c2.imag;
	return c;
}
Complex complex_subtract(Complex c1, Complex c2) {
	Complex c;
	c.real = c1.real - c2.real;
	c.imag = c1.imag - c2.imag;
	return c;
}
Complex complex_multiply(Complex c1, Complex c2) {
	Complex c;
	c.real = c1.real * c2.real - c1.imag * c2.imag;
	c.imag = c1.real * c2.imag + c1.imag * c2.real;
	return c;
}
bool complex_equals(Complex c1, Complex c2) {
	return(c1.real == c2.real) && (c1.imag == c2.imag);
}
Complex complex_conjugate(Complex c) {
	Complex conj;
	conj.real = c.real;
	conj.imag = -c.imag;
	return conj;
}
void complex_scalar_mult(Complex* c, float s) {
	c->real *= s;
	c->imag *= s;
}
float complex_mag(Complex c) {
	return sqrt(c.real * c.real + c.imag * c.imag);
}
float complex_phase(Complex c) {
	return atan2(c.imag, c.real);
}

void complex_to_polar(Complex c, float* r, float* theta) {
	*r = complex_mag(c);
	*theta = complex_phase(c);
}
Complex complex_divide(Complex c1, Complex c2) {
	float aux= c2.real * c2.real + c2.imag * c2.imag;
	Complex r;
	r.real = (c1.real * c2.real + c1.imag * c2.imag) / aux;
	r.imag = (c1.imag * c2.real - c1.real * c2.imag) / aux;
	return r;
}
