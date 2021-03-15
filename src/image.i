/* file : pixel.i */

/* name of module to use*/
%module image
%{ 
	/* Every thing in this file is being copied in 
	wrapper file. We include the C header file necessary 
	to compile the interface */
	#include "image.hpp"

	/* variable declaration*/
	// double myvar; 
	// int width;
	// int height;
	// int grayLevel;
	// int*** pixels;
%} 

%inline %{
/* Note: double[4][4] is equivalent to a pointer to an array double (*)[4] */
double (*new_mat44())[4] {
   return (double (*)[4]) malloc(16*sizeof(double));
}
void free_mat44(double (*x)[4]) {
   free(x);
}
void mat44_set(double x[4][4], int i, int j, double v) {
   x[i][j] = v;
}
double mat44_get(double x[4][4], int i, int j) {
   return x[i][j];
}

int*** new_mat(int width, int height) {
//    return (double (*)[4]) malloc(16*sizeof(double));
//    return (int (*)(*)(*)) malloc(height * sizeof(int**));
	return (int ***) malloc(height * sizeof(int**));
	// for (int i = 0; i < height; i++) {
    //     arr[i] = (int**) malloc(width * sizeof(int*));
    //     for (int j = 0; j < width; j++) {
    //         arr[i][j] = (int*) malloc(3 * sizeof(int));
    //         for (int k = 0; k < 3; k++) {
    //             arr[i][j][k] = 0;
    //         }
    //     }
    // }
	// return arr;
}

int*** mat(int*** arr, int width, int height) {
	for (int i = 0; i < height; i++) {
        arr[i] = (int**) malloc(width * sizeof(int*));
        for (int j = 0; j < width; j++) {
            arr[i][j] = (int*) malloc(3 * sizeof(int));
            for (int k = 0; k < 3; k++) {
                arr[i][j][k] = 0;
            }
        }
    }
	return arr;
}

void free(int*** arr, int width, int height) {
	for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            free(arr[i][j]);
        }
        free(arr[i]);
    }
    free(arr);
}

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
%include "image.hpp" 
