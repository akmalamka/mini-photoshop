from PIL import ImageTk, Image
from IPython.display import display
#open and read the file after the appending:
f = Image.open("../../img/lena.bmp")
# (f)
display(f)
f.save("../../img/abcd.bmp")
print('aaa')
# with open("../../img/baboon24.bmp", 'rb') as f:
#     data = f.read()
# # print(data)

# with open("../../img/lena.bmp", 'wb') as f:
#     f.write(data)