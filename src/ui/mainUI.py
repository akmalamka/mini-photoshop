from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import os
import numpy as np

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.panel = Label(self.parent)
        self.menubar = Menu(self.parent, tearoff=False)
        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.editMenu = Menu(self.menubar, tearoff=False)
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
        self.editMenu.add_command(label="Image Brightening", command =self.imageBrighteningHandler)
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)

    def open_filename(self): 

        # open file dialog box to select image 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def open_image(self): 
        # # Select the Imagename from a folder 
        # x = self.open_filename()

        #panggil fungsi backend yang nyimpen strukturnya

        #simpen strukturnya

        w, h = 512, 512
        imageType = 'BINARY'
        grayLevel = 255
        if (imageType == 'RGB'):
            self.imageArr = np.zeros((h, w, 3), dtype=np.uint8)
            self.imageArr[0:256, 0:256] = [255, 0, 0] # red patch in upper left
            self.rawImg = Image.fromarray(self.imageArr, 'RGB')
        elif (imageType == 'GRAYSCALE'):
            if (grayLevel < 255):
                #yang ini belom, kyknya pake matplotlib ajadeh wkkw
                print('aaa')
            else:
                self.imageArr = np.zeros((h, w), dtype=np.uint8)
                self.imageArr[0:256, 0:256] = [125] # red patch in upper left
                self.rawImg = Image.fromarray(self.imageArr, 'P')
        elif (imageType == 'BINARY'):
            self.imageArr = np.zeros((h, w), dtype=np.uint8)
            self.imageArr[0:256, 0:256] = [1] # red patch in upper left
            self.rawImg = Image.fromarray(self.imageArr, '1')

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
        print(file)
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
        #return ip.negative(self.img)
        print('negative')

    def grayscale(self):
        #return ip.grayscale(self.img)
        print('grayscale')

    def imageBrighteningHandler(self):
        imageBrightenerWindow = ImageBrightenerWindow(self.parent)



class ImageBrightenerWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.scalarInputWindow = Toplevel(self.parent) 
        self.scaleLabel = Label(self.scalarInputWindow)
        self.brighteningScaleAdd = DoubleVar()
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
    
    def ok(self):
        #panggil fungsi image brightening backend
        self.scalarInputWindow.withdraw()


def main():
    root = Tk()
    root.geometry('500x400')
    app = App(root)

    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()