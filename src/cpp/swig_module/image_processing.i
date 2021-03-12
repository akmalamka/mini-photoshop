/* file : gfg.i */

/* name of module to use*/
%module image_processing 
%{ 
	/* Every thing in this file is being copied in 
	wrapper file. We include the C header file necessary 
	to compile the interface */
	// #include "images/pixel.hpp"
	// #include "images/structure.hpp"
	// #include "images/pixel.hpp"
	// #include "utils/exception.hpp"
	// #include "utils/math.hpp"
	// #include "utils/reader.hpp"
	// #include "utils/string.hpp" 
    // #include <iostream>
    // #include <cstdlib>
    // #include <cstdarg>
    // #include <fstream>

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
%include "structure.i"
%include "pixel.i"
%include "reader.i"
%include "string.i" 
