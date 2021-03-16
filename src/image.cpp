#include "image.hpp"

#include <cmath>

int clip(int value, int grayLevel) {
  if (value < 0) return 0;
  if (value > (grayLevel - 1)) return grayLevel - 1;

  return value;
}

void Image::_distributions() {
    this->distributions = (int**) malloc(3 * sizeof(int*));
    for (int i = 0; i < 3; i++) {
        this->distributions[i] = (int*) malloc(this->grayLevel * sizeof(int));
        for (int j = 0; j < this->grayLevel; j++) {
            this->distributions[i][j] = 0;
        }
    }
}

void Image::_distributions(int** distributions) {
    this->_distributions();
    this->__distributions(distributions);
}

void Image::_pixels() {
    this->pixels = (int***) malloc(this->height * sizeof(int**));
    for (int i = 0; i < height; i++) {
        this->pixels[i] = (int**) malloc(this->width * sizeof(int*));
        for (int j = 0; j < width; j++) {
            this->pixels[i][j] = (int*) malloc(3 * sizeof(int));
            for (int k = 0; k < 3; k++) {
                this->pixels[i][j][k] = 0;
            }
        }
    }
}

void Image::_pixels(int*** pixels) {
    this->_pixels();
    this->__pixels(pixels);
}

void Image::__distributions(int** distributions) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < this->grayLevel; j++) {
            this->distributions[i][j] = distributions[i][j];
        }
    }
}

void Image::__pixels(int*** pixels) {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            for (int k = 0; k < 3; k++) {
                this->pixels[i][j][k] = pixels[i][j][k];
            }
        }
    }
}

Image::Image() {
    this->width = 8;
    this->height = 8;
    this->grayLevel = 8;

    this->_distributions();
    this->_pixels();
}

Image::Image(int width, int height, int grayLevel) {
    this->width = width;
    this->height = height;
    this->grayLevel = grayLevel;

    this->_distributions();
    this->_pixels();
}

Image::Image(int width, int height, int grayLevel, int*** pixels) {
    this->width = width;
    this->height = height;
    this->grayLevel = grayLevel;

    this->_distributions();
    this->_pixels(pixels);
}

Image::Image(const Image& image) {
    this->width = image.width;
    this->height = image.height;
    this->grayLevel = image.grayLevel;

    this->_distributions(image.distributions);
    this->_pixels(image.pixels);
}

Image::~Image() {
    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            free(this->pixels[i][j]);
        }
        free(this->pixels[i]);
    }
    free(this->pixels);

    for (int i = 0; i < 3; i++) {
        free(this->distributions[i]);
    }
    free(this->distributions);
}

int Image::getWidth() {
    return this->width;
}

int Image::getHeight() {
    return this->height;
}

int Image::getGrayLevel() {
    return this->grayLevel;
}

int** Image::getDistributions() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < this->grayLevel; j++) this->distributions[i][j] = 0;
        for (int j = 0; j < this->height; j++) {
            for (int k = 0; k < this->width; k++) {
                this->distributions[i][this->pixels[j][k][i]]++;
            }
        }
    }

    return this->distributions;
}

int*** Image::getPixels() {
    return this->pixels;
}

Image& Image::operator=(const Image& image) {
    this->width = image.width;
    this->height = image.height;
    this->grayLevel = image.grayLevel;

    this->_distributions(image.distributions);
    this->_pixels(image.pixels);

    return (*this);
}

Image Image::operator+(const Image& image) {
    int minWidth = (this->width < image.width) ? this->width : image.width;
    int minHeight = (this->height < image.height) ? this->height : image.height;

    Image new_image(minWidth, minHeight, this->grayLevel);

    for (int i = 0; i < minHeight; i++) {
        for (int j = 0; j < minWidth; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] + image.pixels[i][j][k], new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator-(const Image& image) {
    int minWidth = (this->width < image.width) ? this->width : image.width;
    int minHeight = (this->height < image.height) ? this->height : image.height;

    Image new_image(minWidth, minHeight, this->grayLevel);

    for (int i = 0; i < minHeight; i++) {
        for (int j = 0; j < minWidth; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] - image.pixels[i][j][k], new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator+(int scalar) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] + scalar, new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator*(int scalar) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] * scalar, new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator&(const Image& image) {
    int minWidth = (this->width < image.width) ? this->width : image.width;
    int minHeight = (this->height < image.height) ? this->height : image.height;

    Image new_image(minWidth, minHeight, this->grayLevel);

    for (int i = 0; i < minHeight; i++) {
        for (int j = 0; j < minWidth; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] & image.pixels[i][j][k], new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator|(const Image& image) {
    int minWidth = (this->width < image.width) ? this->width : image.width;
    int minHeight = (this->height < image.height) ? this->height : image.height;

    Image new_image(minWidth, minHeight, this->grayLevel);

    for (int i = 0; i < minHeight; i++) {
        for (int j = 0; j < minWidth; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] | image.pixels[i][j][k], new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator^(const Image& image) {
    int minWidth = (this->width < image.width) ? this->width : image.width;
    int minHeight = (this->height < image.height) ? this->height : image.height;

    Image new_image(minWidth, minHeight, this->grayLevel);

    for (int i = 0; i < minHeight; i++) {
        for (int j = 0; j < minWidth; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(this->pixels[i][j][k] ^ image.pixels[i][j][k], new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::operator!(void) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(!this->pixels[i][j][k], new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::transpose() {
    Image new_image(this->height, this->width, this->grayLevel);

    for (int i = 0; i < this->width; i++) {
        for (int j = 0; j < this->height; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = this->pixels[j][i][k];
            }
        }
    }

    return new_image;
}

Image Image::negative() {
    Image new_image(this->width, this->height, this->grayLevel);
    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip((new_image.grayLevel - 1) - this->pixels[i][j][k], new_image.grayLevel);
            }
        }
    }
    return new_image;
}

Image Image::grayscale() {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            int new_pixel = (int) round(0.2126 * this->pixels[i][j][0] + 0.7152 * this->pixels[i][j][1] + 0.0724 * this->pixels[i][j][3]);
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip(new_pixel, new_image.grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::translate(int x, int y) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = y; i < this->height; i++) {
        for (int j = x; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = this->pixels[i - y][j - x][k];
            }
        }
    }

    return new_image;
}

Image Image::rotate(bool isClockwise) {
    return (*this).transpose().flip(isClockwise);
}

Image Image::flip(bool isHorizontal) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = (isHorizontal) ? this->pixels[i][(this->width - 1) - j][k] : this->pixels[(this->height - 1) - i][j][k];
            }
        }
    }

    return new_image;
}

Image Image::zoom() {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = this->pixels[i / 2][j / 2][k];
            }
        }
    }

    return new_image;
}

Image Image::contrastStrech(int min, int max) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                if (this->pixels[i][j][k] < min) new_image.pixels[i][j][k] = 0;
                if (this->pixels[i][j][k] > max) new_image.pixels[i][j][k] = this->grayLevel - 1;
                else new_image.pixels[i][j][k] = clip((this->pixels[i][j][k] - min) * (this->grayLevel - 1) / (max - min), this->grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::logTransform(double c) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip((int) (c * log(1 + this->pixels[i][j][k])), this->grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::inverseLogTransform(double c) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip((int) (c * (exp(this->pixels[i][j][k]) - 1)), this->grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::powerTransform(double c) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip((int) pow(this->pixels[i][j][k], c), this->grayLevel);
            }
        }
    }

    return new_image;
}

Image Image::grayLevelSlice(int min, int max) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                if (this->pixels[i][j][k] > min && this->pixels[i][j][k] < max) new_image.pixels[i][j][k] = this->grayLevel - 1;
                else new_image.pixels[i][j][k] = 0;
            }
        }
    }

    return new_image;
}

Image Image::bitPlaneSlice(int n) {
    Image new_image(this->width, this->height, this->grayLevel);

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                if (this->pixels[i][j][k] & (1 << n)) new_image.pixels[i][j][k] = this->grayLevel - 1;
                else new_image.pixels[i][j][k] = 0;
            }
        }
    }

    return new_image;
}

Image Image::equalize() {
    Image new_image(this->width, this->height, this->grayLevel);

    int dimension = this->width * this->height;
    int** distributions = this->getDistributions();
    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            for (int k = 0; k < 3; k++) {
                new_image.pixels[i][j][k] = clip((int) distributions[k][this->pixels[i][j][k]] * (this->grayLevel - 1) / dimension, this->grayLevel);
            }
        }
    }

    return new_image;
}