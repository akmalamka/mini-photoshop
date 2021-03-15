/* file : pixel.i */

/* name of module to use*/
%module image
%{ 
	/* Every thing in this file is being copied in 
	wrapper file. We include the C header file necessary 
	to compile the interface */
	#include "../images/image.hpp"

	/* variable declaration*/
	// double myvar; 
	// int width;
	// int height;
	// int grayLevel;
	// int*** pixels;
%} 

/* explicitly list functions and variables to be interfaced */
// Image transpose();
// double myvar; 
// long long int fact(long long int n1); 
// int my_mod(int m, int n); 

/* or if we want to interface all functions then we can simply 
include header file like this - 
%include "gfg.h" 
*/
%include "../images/image.hpp" 
