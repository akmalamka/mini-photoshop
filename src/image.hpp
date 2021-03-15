#ifndef IMAGE_HPP
#define IMAGE_HPP

class Image {
    private:
        Image transpose();

    public:
        int width;
        int height;
        int grayLevel;
        int*** pixels;

        Image();
        Image(int width, int height, int grayLevel);
        Image(int width, int height, int grayLevel, int** pixels);
        Image(int width, int height, int grayLevel, int*** pixels);
        Image(const Image& image);

        ~Image();

        Image& operator=(const Image& image);

        Image operator+(const Image& image);
        Image operator-(const Image& image);

        Image operator+(int scalar);
        Image operator*(int scalar);

        Image operator&(const Image& image);
        Image operator|(const Image& image);
        Image operator^(const Image& image);
        Image operator!(void);

        Image negative();
        Image grayscale();
        Image translate(int x, int y);
        Image rotate(bool isClockwise);
        Image flip(bool isVertical);
        Image zoom();

        Image contrastStrech(int min, int max);
        Image logTransform(double c);
        Image inverseLogTransform(double c);
        Image powerTransform(double c);
        Image grayLevelSlice(int min, int max);
        Image bitPlaneSlice(int n);

        // int* distribution();
        // int* distribution(int channel);
        // int** distributions();

        // int** channel();
        // int** channel(int channel);
        // int*** channels();


};

#endif
