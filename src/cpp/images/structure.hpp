#ifndef STRUCTURE_HPP
#define STRUCTURE_HPP

#include <iostream>
#include "pixel.hpp"

enum ImageType {
    BLACKANDWHITE,
    GRAYSCALE,
    RGB
};

class Image {
    protected:
    pixel** pixels;

    public:
    ImageType imageType;
    int height;
    int width;

    Image(ImageType imageType, int height, int width);

    Image(const Image& otherImage);

    Image();

    virtual ~Image();

    static Image* loadImage(std::string filename);

    void set_pixel(int row, int col, pixel px);

    pixel get_pixel(int row, int col);
};

#endif