# import image_processing as ip
import image
import numpy as np
from PIL import Image

def save_array_to_backend( npArray, width, height, graylevel, depth = 0):
    imgObject = image.Image(height, width, graylevel)
    
    for i in range(width):
        for j in range(height):
            for k in range(3):
                image.set(imgObject.pixels, i, j, k, int(npArray[i][j][k]))
    return imgObject

def save_array_to_frontend(imgObject):
    arrTemp = np.zeros((imgObject.height, imgObject.width, 3), dtype='uint8')
    for i in range(imgObject.height):
        for j in range(imgObject.width):
            for k in range(3):
                arrTemp[i][j][k] = image.get(imgObject.pixels, i, j, k)

    return arrTemp

def npArrayHandler(imgType, npArray):
    if (imgType == 'RGB'):
        return npArray
    else:
        arrTemp = np.zeros((npArray.shape[0], npArray.shape[1], 3), dtype='uint8')
        for i in range(npArray.shape[0]):
            for j in range(npArray.shape[1]):
                arrTemp[i][j][0] = npArray[i][j]
        return arrTemp

# file PBM dan BMP Biner
print('abc pbm')
rawImg = Image.open('../img/abc.pbm')
nparr = np.array(rawImg)
nparr = npArrayHandler('BINARY', nparr)
imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

print(image.get(imgObject.pixels, 1, 2, 0))

now = imgObject.negative()
# now = imgObject + 10 gabisaa

print(image.get(now.pixels, 1, 2, 0))

arrNow = save_array_to_frontend(now)

print(arrNow[1][2][0])

# file PGM dan BMP Grayscale dan RAW
print('abc')
rawImg = Image.open('../img/abc.pgm')
nparr = np.array(rawImg)
nparr = npArrayHandler('GRAYSCALE', nparr)
imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

print(image.get(imgObject.pixels, 1, 2, 0))

now = imgObject.negative()
# now = imgObject + 10 gabisaa

print(image.get(now.pixels, 1, 2, 0))

arrNow = save_array_to_frontend(now)

print(arrNow[1][2][0])

print('zelda')
rawImg = Image.open('../img/zelda.bmp')
nparr = np.array(rawImg)
nparr = npArrayHandler('GRAYSCALE', nparr)
imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

print(image.get(imgObject.pixels, 1, 2, 0))

now = imgObject.negative()
# now = imgObject + 10 gabisaa

print(image.get(now.pixels, 1, 2, 0))

arrNow = save_array_to_frontend(now)

print(arrNow[1][2][0])

print('raw gabisaaa wkwk')
# rawImg = Image.open('../img/sample.raw')
# nparr = np.array(rawImg)
# nparr = npArrayHandler('GRAYSCALE', nparr)
# imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

# print(image.get(imgObject.pixels, 1, 2, 0))

# now = imgObject.negative()
# # now = imgObject + 10 gabisaa

# print(image.get(now.pixels, 1, 2, 0))

# arrNow = save_array_to_frontend(now)

# print(arrNow[1][2][0])

# # file PPM dan BMP RGB
print('lena')
rawImg = Image.open('../img/lena.bmp')
nparr = np.array(rawImg)
# print(nparr.shape)
imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

print(image.get(imgObject.pixels, 1, 2, 2))

now = imgObject + 10

print(image.get(now.pixels, 1, 2, 2))

arrNow = save_array_to_frontend(now)

print(arrNow[1][2][2])

print('baboon')
rawImg = Image.open('../img/baboon24.ppm')
nparr = np.array(rawImg)
imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

print(image.get(imgObject.pixels, 1, 2, 2))

now = imgObject + 10

print(image.get(now.pixels, 1, 2, 2))

arrNow = save_array_to_frontend(now)

print(arrNow[1][2][2])