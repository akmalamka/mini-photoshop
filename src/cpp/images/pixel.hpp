#ifndef PIXEL_HPP
#define PIXEL_HPP

#include <cstdlib>
#include <cstdarg>
#define uchar unsigned char

struct pixel {
    uchar len;
    uchar alpha;
    uchar* in;

    pixel();
    pixel(uchar p);
    pixel(uchar p1, uchar p2, uchar p3);
    pixel(uchar p1, uchar p2, uchar p3, uchar a);
    pixel(const pixel& otherPixel);

    ~pixel();
};

#endif