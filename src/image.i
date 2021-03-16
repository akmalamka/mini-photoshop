/* name of module to use*/
%module image
%{ 
	#include "image.hpp"
%} 

%typemap(out) int {
    $result = PyInt_FromLong((long) $1);
}

%typemap(out) double {
    $result = PyFloat_FromDouble((double) $1);
}

%inline %{

    int get(int*** arr, int i, int j, int k) {
        return arr[i][j][k];
    }

    void set(int*** arr, int i, int j, int k, int value) {
        arr[i][j][k] = value;
    }

    int get(int** arr, int i, int j) {
        return arr[i][j];
    }

    double get(double** arr, int i, int j) {
        return arr[i][j];
    }

%}

%include "image.hpp" 
