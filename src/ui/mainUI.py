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
        self.geometryMenu = Menu(self.editMenu, tearoff=False)
        self.histogramMenu = Menu(self.editMenu, tearoff=False)
        self.rotationMenu = Menu(self.editMenu, tearoff=False)
        self.flipMenu = Menu(self.editMenu, tearoff=False)
        self.zoomMenu = Menu(self.editMenu, tearoff=False)
        self.filename = ''
        self.status = 'Initializing'
        self.statusbar = Label(self.parent, text = self.status)
        self.statusbar.pack(side=BOTTOM, fill=X)
        self.imageArrMain = np.zeros((1,1), dtype=np.uint8) #array image utama
        self.imageArrOperation = np.zeros((1,1), dtype=np.uint8) #array image yang akan dioperasikan
        self.scalarValue = DoubleVar()
        self.id = IntVar() #id command yang diberikan
        self.firstEntry = StringVar()
        self.secondEntry = StringVar()
        self.value = Label(self.parent, textvariable= self.firstEntry)
        self.initUI()

    def initUI(self):
        self.parent.title("Mini Photoshop")
        self.parent.config(menu = self.menubar)
        self.fileMenu.add_command(label="Open", command=lambda: self.open_image("Open"))
        self.fileMenu.add_command(label="Save File", command = lambda: self.save_image("Save File"), state='disabled')
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu.add_command(label="Negative", command= lambda: self.negative("Negative"), state='disabled')
        self.editMenu.add_command(label="Grayscale", command=lambda: self.grayscale("Grayscale"), state='disabled')
        self.editMenu.add_command(label="Contrast Stretching", command= lambda: self.negative("Contrast Stretching"), state='disabled')
        self.editMenu.add_command(label="Log Transformation", command=lambda: self.grayscale("Log Transformation"), state='disabled')
        self.editMenu.add_command(label="Inverse Log Transformation", command= lambda: self.negative("Inverse Log Transformation"), state='disabled')
        self.editMenu.add_command(label="Power Transformation", command=lambda: self.grayscale("Power Transformation"), state='disabled')
        self.editMenu.add_command(label="Gray Level Slicing", command= lambda: self.negative("Gray Level Slicing"), state='disabled')
        self.editMenu.add_command(label="Bit Plane Slicing", command=lambda: self.grayscale("Bit Plane Slicing"), state='disabled')

        self.imageBrighteningMenu.add_command(label="Addition with Scalar", command = lambda: self.scalar_input_window("Addition with Scalar"), state='disabled')
        self.imageBrighteningMenu.add_command(label="Multiplication with Scalar", command = lambda: self.scalar_input_window("Multiplication with Scalar"), state='disabled')
        self.editMenu.add_cascade(label="Image Brightening", menu=self.imageBrighteningMenu)

        self.arithmeticsMenu.add_command(label="Addition with Image", command = lambda: self.open_image("Addition with Image"), state='disabled')
        self.arithmeticsMenu.add_command(label="Subtraction with Image", command =lambda: self.open_image("Subtraction with Image"), state='disabled')
        self.editMenu.add_cascade(label="Arithmetics", menu=self.arithmeticsMenu)

        self.booleanMenu.add_command(label="And with Image", command = lambda: self.open_image("And with Image"), state='disabled')
        self.booleanMenu.add_command(label="Not with Image", command =lambda: self.open_image("Not with Image"), state='disabled')
        self.booleanMenu.add_command(label="Or with Image", command = lambda: self.open_image("Or with Image"), state='disabled')
        self.booleanMenu.add_command(label="Xor with Image", command =lambda: self.open_image("Xor with Image"), state='disabled')
        self.editMenu.add_cascade(label="Boolean", menu=self.booleanMenu)

        # self.geometryMenu.add_command(label="Translation", command = lambda: self.open_image("Translation"), state='disabled')
        self.geometryMenu.add_command(label="Translation", command = lambda: self.two_entry_input("Translation"))

        self.rotationMenu.add_command(label="Rotation 90 Clockwise", command = lambda: self.rotation("Rotation 90 Clockwise"), state='disabled')
        self.rotationMenu.add_command(label="Rotation 90 Counter Clockwise", command =lambda: self.rotation("Rotation 90 Counter Clockwise"), state='disabled')
        self.geometryMenu.add_cascade(label="Rotation", menu=self.rotationMenu)

        self.flipMenu.add_command(label="Flip Vertical", command = lambda: self.flip("Flip Vertical"), state='disabled')
        self.flipMenu.add_command(label="Flip Horizontal", command =lambda: self.flip("Flip Horizontal"), state='disabled')
        self.geometryMenu.add_cascade(label="Flip", menu=self.flipMenu)

        self.zoomMenu.add_command(label="Zoom In", command = lambda: self.open_image("Zoom In"), state='disabled')
        self.zoomMenu.add_command(label="Zoom Out", command =lambda: self.open_image("Zoom Out"), state='disabled')
        self.geometryMenu.add_cascade(label="Zoom", menu=self.zoomMenu)

        self.editMenu.add_cascade(label="Geometry", menu=self.geometryMenu)

        self.menubar.add_cascade(label="Edit", menu=self.editMenu)

        self.histogramMenu.add_command(label="Show Histogram", command =lambda: self.open_image("Show Histogram"), state='disabled')
        self.histogramMenu.add_command(label="Show Normalized Histogram", command =lambda: self.open_image("Show Normalized Histogram"), state='disabled')

        self.menubar.add_cascade(label="Histogram", menu=self.histogramMenu)
        self.value.pack()

    def idHandler(self, command):
        switcher = { 
            "Open" : 0,
            "Save File": 1,
            "Negative" : 2, 
            "Grayscale" : 3, 
            "Addition with Scalar" : 4, 
            "Multiplication with Scalar" : 5,
            "Addition with Image" : 6,
            "Subtraction with Image" : 7,
            "And with Image": 8,
            "Not with Image" : 9,
            "Or with Image" : 10,
            "Xor with Image" : 11,
            "Translation" : 12,
            "Rotation 90 Clockwise": 13,
            "Rotation 90 Counter Clockwise": 14,
            "Flip Vertical" : 14,
            "Flip Horizontal" : 15,
            "Zoom In" : 16,
            "Zoom Out" : 17,
            "Show Histogram" : 18,
            "Show Normalized Histogram" : 19,
            "Contrast Stretching": 20,
            "Log Transformation": 21,
            "Inverse Log Transformation": 22,
            "Power Transformation": 23,
            "Gray Level Slicing": 24,
            "Bit Plane Slicing": 25
        } 

        idTemp = switcher.get(command, lambda: -1)
        if (not idTemp == -1):
            self.id.set(int(idTemp))

    def open_filename(self): 
        # open file dialog box to select image 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def open_image(self, command):
        self.idHandler(command)
        # # Select the Imagename from a folder
        x = self.open_filename()
        self.rawImg = Image.open(x)

        if (self.id.get() == 0):
            #Open Image at the beginning
            # # Select the Imagename from a folder 
            # self.npArrImg = np.array(self.rawImg)
            # self.listImg = self.npArrImg.tolist()
            # self.imgType = ''
            # if (self.rawImg.mode == '1'):
            #     self.imgType = 'BINARY'
            # elif (self.rawImg.mode == 'L'):
            #     self.imgType = 'GRAYSCALE'
            # elif (self.rawImg.mode == 'RGB'):
            #     self.imgType = "RGB"
            #IMPORTANT
            #lempar array ke backend
            #self.imgObject = ip.makeImage(self.listImg, self.imgType)
            #simpen array dari backend
            # self.listImg = ip.getArray()

            # w, h = 512, 512
            # imageType = 'RGB'
            # grayLevel = 255
            # if (imageType == 'RGB'):
            #     self.imageArrMain = np.zeros((h, w, 3), dtype=np.uint8)
            #     self.imageArrMain[0:256, 0:256] = [255, 0, 0] # red patch in upper left
            #     self.rawImg = Image.fromarray(self.imageArrMain, 'RGB')
            # elif (imageType == 'GRAYSCALE'):
            #     if (grayLevel < 255):
            #         #yang ini belom, kyknya pake matplotlib ajadeh wkkw
            #         print('aaa')
            #     else:
            #         self.imageArrMain = np.zeros((h, w), dtype=np.uint8)
            #         self.imageArrMain[0:256, 0:256] = [125] # red patch in upper left
            #         self.rawImg = Image.fromarray(self.imageArrMain, 'P')
            # elif (imageType == 'BINARY'):
            #     self.imageArrMain = np.zeros((h, w), dtype=np.uint8)
            #     self.imageArrMain[0:256, 0:256] = [1] # red patch in upper left
            #     self.rawImg = Image.fromarray(self.imageArrMain, '1')

            # PhotoImage class is used to add image to widgets, icons etc 
            self.img = ImageTk.PhotoImage(self.rawImg) 

            # create a label 
            self.panel = Label(self.parent, image = self.img)

            # set the image as img 
            self.panel.pack()
            width, height = self.rawImg.size
            self.statusbar.config(text=self.filename + ' height = ' + str(height) + ' width = ' + str(width) + ' format = ' + str(self.rawImg.format) + ' size = ' + str(os.path.getsize(self.filename)) + ' bytes')
            self.disable_sub_menu('Open')
            
        else:
            self.imageArrOperation = np.array(self.rawImg)
            #panggil fungsi yang ngelakuin operasi2nya di backend
        self.enable_sub_menu('Save File')
        self.enable_all_sub_menu()

    def save_image(self, command):
        self.idHandler(command) 
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
        # if (menu == 'Open'):
        #     self.fileMenu.entryconfig('Open', state='normal')
        # elif (menu == 'Save File'):
        #     self.fileMenu.entryconfig('Save File', state='normal')
        self.fileMenu.entryconfig(menu, state='normal')

    def disable_sub_menu(self, menu):
        # if (menu == 'Open'):
        #     self.fileMenu.entryconfig('Open', state='disabled')
        # elif (menu == 'Save File'):
        #     self.fileMenu.entryconfig('Save File', state='disabled')
        self.fileMenu.entryconfig(menu, state='disabled')

    def enable_all_sub_menu(self):
        self.editMenu.entryconfig("Negative", state='normal')
        self.editMenu.entryconfig("Grayscale", state='normal')
        self.imageBrighteningMenu.entryconfig("Addition with Scalar", state='normal')
        self.imageBrighteningMenu.entryconfig("Multiplication with Scalar", state='normal')
        self.arithmeticsMenu.entryconfig("Addition with Image", state='normal')
        self.arithmeticsMenu.entryconfig("Subtraction with Image", state='normal')
        self.booleanMenu.entryconfig("And with Image", state='normal')
        self.booleanMenu.entryconfig("Not with Image", state='normal')
        self.booleanMenu.entryconfig("Or with Image", state='normal')
        self.booleanMenu.entryconfig("Xor with Image", state='normal')
        self.geometryMenu.entryconfig("Translation", state='normal')
        self.rotationMenu.entryconfig("Rotation 90 Clockwise", state='normal')
        self.rotationMenu.entryconfig("Rotation 90 Counter Clockwise", state='normal')
        self.flipMenu.entryconfig("Flip Vertical", state='normal')
        self.flipMenu.entryconfig("Flip Horizontal", state='normal')
        self.zoomMenu.entryconfig("Zoom In", state='normal')
        self.zoomMenu.entryconfig("Zoom Out", state='normal')
        self.histogramMenu.entryconfig("Show Histogram", state='normal')

    def negative(self, command):
        # ubah image object jadi negative
        # self.imageObject.negative()
        self.idHandler(command)
        print('negative')

    def grayscale(self, command):
        # ubah image object jadi grayscale
        #self.imageObject.grayscale()
        self.idHandler(command)
        print('grayscale')

    def scalar_input_window(self, command):
        self.idHandler(command)
        self.scalarInputWindow = Toplevel(self.parent)
        # sets the title of the Toplevel widget 
        self.scalarInputWindow.title("Scalar Value") 
    
        # sets the geometry of toplevel 
        self.scalarInputWindow.geometry("200x200")
        self.scaleLabel = Label(self.scalarInputWindow)
        scale = Scale(self.scalarInputWindow, variable=self.scalarValue, from_=-255, to=255, orient=HORIZONTAL)
        showScaleButton = Button(self.scalarInputWindow, text ="Show Scale", command = self.show)
        okButton = Button(self.scalarInputWindow, text ="OK", command = self.ok)

        scale.pack()
        showScaleButton.pack()
        okButton.pack()
        self.scaleLabel.pack()

    def show(self):
        selection = "Value = " + str(int(self.scalarValue.get()))
        self.scaleLabel.config(text = selection)
    
    def ok(self):
        #panggil fungsi image brightening backend
        id = self.id.get()
        if (id == 4 or id == 5):
            self.scalarInputWindow.destroy()
        elif (id == 12):
            try:
                int(self.firstEntry.get())
                int(self.secondEntry.get())
                self.twoEntryInputWindow.destroy()
            except ValueError:
                self.feedback.config(text='Masukan hanya bisa integer, silakan coba lagi')
            

    def two_entry_input(self, command):
        self.idHandler(command)
        self.twoEntryInputWindow = Toplevel(self.parent)
        # sets the title of the Toplevel widget 
        self.twoEntryInputWindow.title("X and Y Value") 
    
        # sets the geometry of toplevel 
        self.twoEntryInputWindow.geometry("330x170")

        label1 = Label(self.twoEntryInputWindow, text='X').place(x = 30, y = 30)
        entry1 = Entry(self.twoEntryInputWindow, textvariable=self.firstEntry).place(x = 80, y = 30)
        label2 = Label(self.twoEntryInputWindow, text='Y').place(x = 30, y = 60)
        entry2 = Entry(self.twoEntryInputWindow, textvariable=self.secondEntry).place(x = 80, y = 60)
        okButton = Button(self.twoEntryInputWindow, text ="OK", command = self.ok)
        self.feedback = Label(self.twoEntryInputWindow, text='')

        okButton.pack(side=BOTTOM, pady = 7)
        self.feedback.pack(side=BOTTOM, pady=12)

    def rotation(self, command):
        # rotate image object sesuai command
        #self.imageObject.grayscale()
        self.idHandler(command)
        #conditional kalo 90 cw dan ccw
        print('rotation')

    def flip(self, command):
        # flip image object sesuai command
        #self.imageObject.grayscale()
        self.idHandler(command)
        #conditional kalo flip vertical atau horizontal
        print('flip') 
    

def main():
    root = Tk()
    root.geometry('500x400')
    app = App(root)
    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()