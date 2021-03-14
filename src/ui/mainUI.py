from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import os
import numpy as np
#import image_processing as ip

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.panel = Label(self.parent)
        self.menubar = Menu(self.parent, tearoff=False)
        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.editMenu = Menu(self.menubar, tearoff=False)
        self.imageBrighteningMenu = Menu(self.editMenu, tearoff=False)
        self.arithmeticsMenu = Menu(self.editMenu, tearoff=False)
        self.booleanMenu = Menu(self.editMenu, tearoff=False)
        self.filename = ''
        self.status = 'Initializing'
        self.statusbar = Label(self.parent, text = self.status)
        self.statusbar.pack(side=BOTTOM, fill=X)
        self.imageArr = np.zeros((1,1), dtype=np.uint8)
        self.brighteningScalarValue = DoubleVar()
        self.initUI()

    def initUI(self):
        self.parent.title("Mini Photoshop")
        self.parent.config(menu = self.menubar)
        self.fileMenu.add_command(label="Open", command=self.open_image)
        self.fileMenu.add_command(label="Save File", command = self.save_image, state='disabled')
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu.add_command(label="Negative", command=self.negative)
        self.editMenu.add_command(label="Grayscale", command=self.grayscale)

        self.imageBrighteningMenu.add_command(label="Addition with Scalar", command = lambda: self.image_brightening_handler(0))
        self.imageBrighteningMenu.add_command(label="Multiplication with Scalar", command =lambda: self.image_brightening_handler(1))
        self.editMenu.add_cascade(label="Image Brightening", menu=self.imageBrighteningMenu)

        self.arithmeticsMenu.add_command(label="Addition with Image", command = lambda: self.open_image(0))
        self.arithmeticsMenu.add_command(label="Subtraction with Image", command =lambda: self.open_image(1))
        self.editMenu.add_cascade(label="Arithmetics", menu=self.arithmeticsMenu)

        self.booleanMenu.add_command(label="And with Image", command = lambda: self.open_image(2))
        self.booleanMenu.add_command(label="Not with Image", command =lambda: self.open_image(3))
        self.booleanMenu.add_command(label="Or with Image", command = lambda: self.open_image(4))
        self.booleanMenu.add_command(label="Xor with Image", command =lambda: self.open_image(5))
        self.editMenu.add_cascade(label="Boolean", menu=self.booleanMenu)

        self.menubar.add_cascade(label="Edit", menu=self.editMenu)


    def open_filename(self): 
        # open file dialog box to select image 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def open_image(self, option = -1):
        if (option == 0):
            #Addition with Image
            print('0')
        elif (option == 1):
            #Subtraction with Image
            print('1')
        elif (option == 2):
            #And with Image
            print('2')
        elif (option == 3):
            #Not with Image
            print('3')
        elif (option == 4):
            #Or with Image
            print('4')
        elif (option == 5):
            #Xor with Image
            print('5')
        else:
            #Open Image at the beginning
            # # Select the Imagename from a folder 
            x = self.open_filename()

            self.rawImg = Image.open(x)
            self.npArrImg = np.array(self.rawImg)
            self.listImg = self.npArrImg.tolist()
            self.imgType = ''
            if (self.rawImg.mode == '1'):
                self.imgType = 'BINARY'
            elif (self.rawImg.mode == 'L'):
                self.imgType = 'GRAYSCALE'
            elif (self.rawImg.mode == 'RGB'):
                self.imgType = "RGB"
            #IMPORTANT
            #lempar array ke backend
            #self.imgObject = ip.makeImage(self.listImg, self.imgType)
            #simpen array dari backend
            # self.listImg = ip.getArray()

            # w, h = 512, 512
            # imageType = 'RGB'
            # grayLevel = 255
            # if (imageType == 'RGB'):
            #     self.imageArr = np.zeros((h, w, 3), dtype=np.uint8)
            #     self.imageArr[0:256, 0:256] = [255, 0, 0] # red patch in upper left
            #     self.rawImg = Image.fromarray(self.imageArr, 'RGB')
            # elif (imageType == 'GRAYSCALE'):
            #     if (grayLevel < 255):
            #         #yang ini belom, kyknya pake matplotlib ajadeh wkkw
            #         print('aaa')
            #     else:
            #         self.imageArr = np.zeros((h, w), dtype=np.uint8)
            #         self.imageArr[0:256, 0:256] = [125] # red patch in upper left
            #         self.rawImg = Image.fromarray(self.imageArr, 'P')
            # elif (imageType == 'BINARY'):
            #     self.imageArr = np.zeros((h, w), dtype=np.uint8)
            #     self.imageArr[0:256, 0:256] = [1] # red patch in upper left
            #     self.rawImg = Image.fromarray(self.imageArr, '1')

            # PhotoImage class is used to add image to widgets, icons etc 
            self.img = ImageTk.PhotoImage(self.rawImg) 

            # create a label 
            self.panel = Label(self.parent, image = self.img)

            # set the image as img 
            self.panel.pack()
            width, height = self.rawImg.size
            self.statusbar.config(text=self.filename + ' height = ' + str(height) + ' width = ' + str(width) + ' format = ' + str(self.rawImg.format) + ' size = ' + str(os.path.getsize(self.filename)) + ' bytes')
            self.disable_sub_menu('Open')
            self.enable_sub_menu('Save File')
    

    def save_image(self): 
        files = [('All Files', '*.*'),  
                ('PGM Files', '*.pgm'), 
                ('PPM Files', '*.ppm'),
                ('PBM Files', '*.pbm'),
                ('BMP Files', '*.bmp')] 
        file = asksaveasfilename( filetypes = files, defaultextension = files)
        if file is None:
            return None
        #IMPORTANT
        # ubah array dari backend ke numpy
        # self.npArrImg = np.array(self.listImg)
        # ubah numpy array ke image sesuai sama modenya rawImg
        # self.rawImg = Image.fromarray(self.npArrImg, self.rawImg.mode), kalo gabisa pake mode, pake imgType

        self.rawImg.save(file)

    def enable_sub_menu(self, menu):
        if (menu == 'Open'):
            self.fileMenu.entryconfig('Open', state='normal')
        elif (menu == 'Save File'):
            self.fileMenu.entryconfig('Save File', state='normal')

    def disable_sub_menu(self, menu):
        if (menu == 'Open'):
            self.fileMenu.entryconfig('Open', state='disabled')
        elif (menu == 'Save File'):
            self.fileMenu.entryconfig('Save File', state='disabled')

    def negative(self):
        # ubah image object jadi negative
        # self.imageObject.negative()
        print('negative')

    def grayscale(self):
        # ubah image object jadi grayscale
        #self.imageObject.grayscale()
        print('grayscale')

    def image_brightening_handler(self, id):
        imageBrightenerWindow = ImageBrightenerWindow(self.parent)
        imageBrightenerWindow.id = id



class ImageBrightenerWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.scalarInputWindow = Toplevel(self.parent) 
        self.scaleLabel = Label(self.scalarInputWindow)
        self.brighteningScaleAdd = DoubleVar()
        self.id = 0 #id 0 untuk additional, id 2 untuk multiplication
        self.initUI()

    def initUI(self):
        # sets the title of the Toplevel widget 
        self.scalarInputWindow.title("Scalar Value") 
    
        # sets the geometry of toplevel 
        self.scalarInputWindow.geometry("200x200")
        scale = Scale(self.scalarInputWindow, variable=self.brighteningScaleAdd, from_=-255, to=255, orient=HORIZONTAL)
        showScaleButton = Button(self.scalarInputWindow, text ="Show Scale", command = self.show)
        okButton = Button(self.scalarInputWindow, text ="OK", command = self.ok)
        
        scale.pack()
        showScaleButton.pack()
        okButton.pack()
        self.scaleLabel.pack()

    def show(self):
        selection = "Value = " + str(self.brighteningScaleAdd.get())
        self.scaleLabel.config(text = selection)
        # print(self.id)
    
    def ok(self):
        #panggil fungsi image brightening backend
        if (self.id == 0):
            print('abc')
        elif (self.id == 1):
            print('def')
        self.scalarInputWindow.withdraw()
        self.parent.update()
        self.parent.deiconify()


def main():
    root = Tk()
    root.geometry('500x400')
    app = App(root)

    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()