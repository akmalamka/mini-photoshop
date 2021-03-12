/* file : gfg.i */

/* name of module to use*/
%module structure
%{ 
	/* Every thing in this file is being copied in 
	wrapper file. We include the C header file necessary 
	to compile the interface */
	#include "../images/structure.hpp" 

	/* variable declaration*/
	// double myvar; 
%} 

/* explicitly list functions and variables to be interfaced */
// double myvar; 
// long long int fact(long long int n1); 
// int my_mod(int m, int n); 

/* or if we want to interface all functions then we can simply 
include header file like this - 
%include "gfg.h" 
*/
%include "../images/structure.hpp" 
