# # import image_processing as ip
# import image
import numpy as np
# from PIL import Image

# def save_array_to_backend( npArray, width, height, graylevel, depth = 0):
#     imgObject = image.Image(height, width, graylevel)
    
#     for i in range(width):
#         for j in range(height):
#             for k in range(3):
#                 image.set(imgObject.pixels, i, j, k, int(npArray[i][j][k]))
#     return imgObject

# def save_array_to_frontend(imgObject):
#     arrTemp = np.zeros((imgObject.height, imgObject.width, 3), dtype='uint8')
#     for i in range(imgObject.height):
#         for j in range(imgObject.width):
#             for k in range(3):
#                 arrTemp[i][j][k] = image.get(imgObject.pixels, i, j, k)

#     return arrTemp

# def npArrayHandler(imgType, npArray):
#     if (imgType == 'RGB'):
#         return npArray
#     else:
#         arrTemp = np.zeros((npArray.shape[0], npArray.shape[1], 3), dtype='uint8')
#         for i in range(npArray.shape[0]):
#             for j in range(npArray.shape[1]):
#                 if (npArray[i][j]):
#                     arrTemp[i][j][0] = 1
#                     arrTemp[i][j][1] = 1
#                     arrTemp[i][j][2] = 1
#                 else:
#                     arrTemp[i][j][0] = 0
#                     arrTemp[i][j][1] = 0
#                     arrTemp[i][j][2] = 0

#         return arrTemp

# # file PBM dan BMP Biner
# print('abc pbm')
# rawImg = Image.open('../img//test/abc.pbm')
# nparr = np.array(rawImg)
# nparr = npArrayHandler('BINARY', nparr)
# # print(nparr) 
# # print('ccc')
# # print(nparr)
# imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

# print(image.get(imgObject.pixels, 1, 2, 0))

# now = imgObject.negative()
# # now = imgObject + 10 gabisaa

# print(image.get(now.pixels, 1, 2, 0))

# arrNow = save_array_to_frontend(now)

# print(arrNow[1][2][0])

# # file PGM dan BMP Grayscale dan RAW
# print('abc')
# rawImg = Image.open('../img/test/abc.pgm')
# nparr = np.array(rawImg)
# # print(nparr)
# nparr = npArrayHandler('GRAYSCALE', nparr)
# print('ccc')
# # print(nparr)
# imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)
# print(image.get(imgObject.pixels, 1, 2, 0))

# # now = imgObject.negative()
# now = imgObject + 10

# print(image.get(now.pixels, 1, 2, 0))

# arrNow = save_array_to_frontend(now)

# print(arrNow[1][2][0])

# print('zelda')
# rawImg = Image.open('../img//test/zelda.bmp')
# nparr = np.array(rawImg)
# nparr = npArrayHandler('GRAYSCALE', nparr)
# imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

# print(image.get(imgObject.pixels, 1, 2, 0))

# now = imgObject.negative()
# # now = imgObject + 10 gabisaa

# print(image.get(now.pixels, 1, 2, 0))

# arrNow = save_array_to_frontend(now)

# print(arrNow[1][2][0])

# print('raw gabisaaa wkwk')
# # rawImg = Image.open('../img/sample.raw')
# # nparr = np.array(rawImg)
# # nparr = npArrayHandler('GRAYSCALE', nparr)
# # imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

# # print(image.get(imgObject.pixels, 1, 2, 0))

# # now = imgObject.negative()
# # # now = imgObject + 10 gabisaa

# # print(image.get(now.pixels, 1, 2, 0))

# # arrNow = save_array_to_frontend(now)

# # print(arrNow[1][2][0])

# # # file PPM dan BMP RGB
# print('lena')
# rawImg = Image.open('../img//test/lena.bmp')
# print(rawImg.mode == 'RGB')
# nparr = np.array(rawImg)
# print(len(nparr.shape))
# # print(nparr.shape)
# imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

# print(image.get(imgObject.pixels, 1, 1, 0))

# now = imgObject + 10

# print(image.get(now.pixels, 1, 1, 0))

# arrNow = save_array_to_frontend(now)

# print(arrNow[1][1][0])

# print('baboon')
# rawImg = Image.open('../img/test/baboon24.ppm')
# nparr = np.array(rawImg)
# imgObject = save_array_to_backend(nparr, nparr.shape[0], nparr.shape[1], 256, 3)

# print(image.get(imgObject.pixels, 1, 2, 2))

# now = imgObject + 10

# print(image.get(now.pixels, 1, 2, 2))

# arrNow = save_array_to_frontend(now)

# print(arrNow[1][2][2])

# from tkinter import *  
# from PIL import ImageTk,Image  
# root = Tk()  


# def npArrayHandler(command, imgType, npArray):
#         if (command == 'convertTo3D'):
#             if (imgType == 'RGB'):
#                 return npArray
#             else:
#                 arrTemp = np.zeros((npArray.shape[0], npArray.shape[1], 3), dtype='uint8')
#                 if (imgType == 'GRAYSCALE'):
#                     for i in range(npArray.shape[0]):
#                         for j in range(npArray.shape[1]):
#                             arrTemp[i][j][0] = npArray[i][j]
#                             arrTemp[i][j][1] = npArray[i][j]
#                             arrTemp[i][j][2] = npArray[i][j]

#                 elif (imgType == 'BINARY'):
#                     print('bbb')
#                     print(npArray[0][0:10])
#                     for i in range(npArray.shape[0]):
#                         for j in range(npArray.shape[1]):
#                             if (npArray[i][j] or npArray[i][j] == 1):
#                                 arrTemp[i][j][0] = 1
#                                 arrTemp[i][j][1] = 1
#                                 arrTemp[i][j][2] = 1
#                             else:
#                                 arrTemp[i][j][0] = 0
#                                 arrTemp[i][j][1] = 0
#                                 arrTemp[i][j][2] = 0
#                     print(arrTemp[0][0:10])
#                 return arrTemp

#         elif (command == 'convert3DTo2D'):
#             print('ddd')
#             arrTemp = np.zeros((npArray.shape[0], npArray.shape[1]), dtype='uint8')
#             for i in range(npArray.shape[0]):
#                 for j in range(npArray.shape[1]):
#                     arrTemp[i][j] = npArray[i][j][1]
#             # print(arrTemp.shape)
#             # print(arrTemp[0][0:10])
#             return arrTemp
        
# raw = Image.open('../img/test/abc.pbm')
# nparr = np.array(raw)
# imageArrMain = npArrayHandler('convertTo3D', 'BINARY', nparr)
# arrTemp = npArrayHandler('convert3DTo2D', 'BINARY', imageArrMain)
# # print(nparr == arrTemp)
# comparison = nparr == arrTemp
# equal_arrays = comparison.all()
# print('arrtemp shape = ' + str(arrTemp.shape))
# print('nparr shape = ' + str(nparr.shape))
# print('comparison')
# print(equal_arrays)
# print(nparr[0] == arrTemp[0])
# img = ImageTk.PhotoImage(Image.fromarray((arrTemp * 255).astype('uint8'), 'L')) # photo image class tkinter
# # img = ImageTk.PhotoImage(Image.fromarray(nparr, 'L'))  
# canvas = Label(image = img) 
# canvas.pack()  
# # canvas.create_image(20, 20, anchor=NW, image=img) 
# root.mainloop() 

import matplotlib.pyplot as plt
from numpy import array
gn=array([1,2,3,728,625,0,736,5243,9.0])
# plt.hist(gn.astype('float'))
# plt.show()
img = plt.imread('../img/test/lena.bmp')
arr = np.array(img)
print(arr)