import image_processing as ip

# a = image_processing.Image(image_processing.GRAYSCALE, 12, 13)
# print(a.height)
a = ip.Image_loadImage(ip.convertSystemToStdString("../../../img/sample.raw"))
print(a.height)