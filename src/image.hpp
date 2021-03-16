#ifndef IMAGE_HPP
#define IMAGE_HPP

class Image {
    private:
        int width;
        int height;
        int grayLevel;

        int** distributions;
        int*** pixels;

        double** normalizedDistributions;

        void _distributions();
        void _distributions(int** distributions, double** normalizedDistributions);
        void _pixels();
        void _pixels(int*** pixels);

        void __distributions(int** distributions, double** normalizedDistributions);
        void __pixels(int*** pixels);

        Image transpose();

    public:
        Image();
        Image(int width, int height, int grayLevel);
        // Image(int width, int height, int grayLevel, int** pixels);
        Image(int width, int height, int grayLevel, int*** pixels);
        Image(const Image& image);

        ~Image();

        int getWidth();
        int getHeight();
        int getGrayLevel();

        int** getDistributions();
        int*** getPixels();

        double getMean(int channel);
        double getVariance(int channel);
        double getStandardDeviation(int channel);

        double* getNormalizedDistribution(int channel);
        double** getNormalizedDistributions();

        Image& operator=(const Image& image);

        Image operator+(const Image& image);
        Image operator-(const Image& image);

        Image operator+(int scalar);
        Image operator*(int scalar);

        Image operator&(const Image& image);
        Image operator|(const Image& image);
        Image operator^(const Image& image);
        // Image operator!(void);

        Image negative();
        Image grayscale();
        Image translate(int x, int y);
        Image rotate(bool isClockwise);
        Image flip(bool isHorizontal);
        Image zoom();

        Image contrastStrech(int min, int max);
        Image logTransform(double c);
        Image inverseLogTransform(double c);
        Image powerTransform(double c);
        Image grayLevelSlice(int min, int max);
        Image bitPlaneSlice(int n);

        Image equalize();
        Image specifize(const Image& image);
};

#endif