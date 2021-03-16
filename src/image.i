/* name of module to use*/
%module image
%{ 
	#include "image.hpp"
%} 

%typemap(out) int {
    $result = PyInt_FromLong((long) $1);
}

%inline %{

    int*** new_mat(int width, int height) {
        return (int ***) malloc(height * sizeof(int**));
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

    void freeAll(int*** arr, int width, int height) {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                free(arr[i][j]);
            }
            free(arr[i]);
        }
        free(arr);
    }

    void free(int*** arr, int width, int height) {
        for (int i = 0; i < height; i++) {
            // for (int j = 0; j < width; j++) {
            //     free(arr[i][j]);
            // }
            free(arr[i]);
        }
        // free(arr);
    }

    int get(int*** arr, int i, int j, int k) {
        return arr[i][j][k];
    }

    void set(int*** arr, int i, int j, int k, int value) {
        arr[i][j][k] = value;
    }

%}

%include "image.hpp" 
