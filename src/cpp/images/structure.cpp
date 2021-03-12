#include <iostream>
#include <fstream>
#include <cstdlib>
#include "structure.hpp"
#include "pixel.hpp"
#include "../utils/string.hpp"
#include "../utils/reader.hpp"
#include "../utils/exception.hpp"

using namespace std;

Image::Image() {
  this->imageType = RGB;
  this->height = 32;
  this->width = 32;
  
  this->pixels = (pixel**) malloc(height * sizeof (pixel*));
  for (int i = 0; i < height; i++){
    this->pixels[i] = (pixel*) malloc(width * sizeof (pixel));
    for (int j = 0; j < width; j++) {
      this->pixels[i][j] = pixel(0,0,0,0);
    }
  }

}

Image::Image(ImageType imageType, int height, int width) {
  this->imageType = imageType;
  this->height = height;
  this->width = width;

  this->pixels = (pixel**) malloc(height * sizeof (pixel*));
  for (int i = 0; i < height; i++){
    this->pixels[i] = (pixel*) malloc(width * sizeof (pixel));
    for (int j = 0; j < width; j++) {
      this->pixels[i][j] = pixel(0,0,0,0);
    }
  }

}

Image::Image(const Image& otherImage) {
  this->imageType = otherImage.imageType;
  this->height = otherImage.height;
  this->width = otherImage.width;

  this->pixels = (pixel**) malloc(height * sizeof (pixel*));
  for (int i = 0; i < height; i++){
    this->pixels[i] = (pixel*) malloc(width * sizeof (pixel));
    for (int j = 0; j < width; j++) {
      this->pixels[i][j] = pixel(0,0,0,0);
    }
  }
  
  for (int i = 0; i < this->height; i++) {
    for (int j = 0; j < this->width; j++) {
      this->set_pixel(i, j, otherImage.pixels[i][j]);
    }
  }
}

Image::~Image() {
  for (int i = 0; i < this->height; i++) {
    free(this->pixels[i]);
  }
  free(this->pixels);
}

Image* Image::loadImage(std::string filename) {
  // if (hasEnding(filename, ".pbm")) {
  //   return BWImage::loadPBM(filename);
  // } else if (hasEnding(filename, ".pgm")) {
  //   return GrayscaleImage::loadPGM(filename);
  // } else if (hasEnding(filename, ".ppm")) {
  //   return RGBImage::loadPPM(filename);
  // } else if (hasEnding(filename, ".bmp")) {
  //   return RGBImage::loadBMP(filename);
  // } else 
  if (hasEnding(filename, ".raw")) {
    // return GrayscaleImage::loadRAW(filename);
    std::ifstream image_file;
    image_file.open(filename, std::ios::in | std::ios::binary);
    if (image_file.is_open()) {
      // retrieving file size
      image_file.seekg(0, std::ios::end);
      std::streampos size = image_file.tellg();
      image_file.seekg(0, std::ios::beg);

      char* bytes = new char[size];
      image_file.read(bytes, size);
      image_file.close();

      int pointer = 0;
      int width = nextInt(bytes, size, &pointer);
      int height = nextInt(bytes, size, &pointer);

      Image* image = new Image(GRAYSCALE, height, width);
      for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
          uchar gray = nextInt(bytes, size, &pointer);
          image->set_pixel(i, j, pixel(gray));
        }
      }

    delete[] bytes;
    return image;
    } else {
      throw "format not supported";
    }
  }
}

void Image::set_pixel(int row, int col, pixel px) {
  this->pixels[row][col] = px;
}

pixel Image::get_pixel(int row, int col) {
  return this->pixels[row][col];
}

// int main () {
//   string line;
//   ifstream myfile ("../../../img/sample.raw");
//   if (myfile.is_open())
//   {
//     int a, b;
//     myfile >> a >> b;
//     cout << a << endl;
//     cout << b << endl;
//      // while (myfile >> a >> b)
//     // {
//     //     // process pair (a,b)
//     // }
//     while ( getline (myfile,line) )
//     {

//       cout << line << '\n';
//     }

//     myfile.close();
//   }

//   else cout << "Unable to open file"; 

//   return 0;
// }