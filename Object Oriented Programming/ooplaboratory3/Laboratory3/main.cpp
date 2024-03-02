#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#include "complex_test.h"


int main(int argc, char** argv)
{

	run_complex_tests(true);


	Complex c1;
	c1.real = 10;
	c1.imag = 1;
	float c1_phase = complex_phase(c1);
	float c1_mag = complex_mag(c1);
	float r, theta;
	printf("Complex number allocated on the stack:");
	printf("\n");
	complex_display(c1);
	printf("\n");



	complex_to_polar(c1, &r, &theta);
	printf("Polar coordinates\nMagnitude: %f\nPhase: %f radians.", r, theta);
	printf("\n");

	printf("Conjugate\n");
	complex_display(complex_conjugate(c1));
	printf("\n");

	float scalar = 3;
	complex_scalar_mult(&c1, scalar);
	printf("Multiplication with the scalar %f\n", scalar);
	complex_display(c1);
	printf("\n");


	Complex* c2 = (Complex*)malloc(sizeof(Complex));
	c2->real = 7;
	c2->imag = 2;
	float c2_mag = complex_mag(*c2);
	float r2, theta2;
	printf("Complex number allocated on the heap:");
	printf("\n");
	complex_display(*c2);
	printf("\n");


	complex_to_polar(*c2, &r2, &theta2);
	printf("Polar coordinates\nMagnitude: %f\nPhase: %f", r, theta);
	printf("\n");

	printf("Conjugate\n");
	complex_display(complex_conjugate(*c2));
	printf("\n");

	float scalar2 = 4;
	complex_scalar_mult(c2, scalar2);
	printf("Multiplication with the scalar %f\n", scalar2);
	complex_display(*c2);
	printf("\n");

	printf("Operations with the complex numbers");
	printf("\n");

	printf("Addition:\n");
	complex_display(complex_add(c1, *c2));
	printf("\n");

	printf("Subtraction:\n");
	complex_display(complex_subtract(c1, *c2));
	printf("\n");

	printf("Multiplication:\n");
	complex_display(complex_multiply(c1, *c2));
	printf("\n");

	Complex c2_inv;
	c2_inv.real = 1 / c2->real;
	c2_inv.imag = 1 / c2->imag;
	printf("Division:\n");
	complex_display(complex_multiply(c1, c2_inv));
	printf("\n");

	free(c2);


	getchar();
	return 0;
}