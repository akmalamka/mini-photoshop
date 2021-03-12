#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include "pixel.hpp"

pixel::pixel() {
    len = 1;
    in = new uchar[len];
    in[0] = 0;
    alpha = 1;
}

pixel::pixel(uchar p) {
    len = 1;
    in = new uchar[len];
    in[0] = p;
    alpha = 1;
}

pixel::pixel(uchar p1, uchar p2, uchar p3) {
    len = 3;
    in = new uchar[len];
    in[0] = p1;
    in[1] = p2;
    in[2] = p3;
    alpha = 1;
}

pixel::pixel(uchar p1, uchar p2, uchar p3, uchar a) {
    len = 3;
    in = new uchar[len];
    in[0] = p1;
    in[1] = p2;
    in[2] = p3;
    alpha = 1;
    alpha = a;
}

pixel::pixel(const pixel& otherPixel) {
    len = otherPixel.len;
    in = new uchar[len];
    for (int i = 0; i < len; i++) {
        in[i] = otherPixel.in[i];
    }
    alpha = otherPixel.alpha;
}

pixel::~pixel() {
    delete[] in;
}