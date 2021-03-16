from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import os
import numpy as np
import image

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.mainPanel = Label(self.parent) # panel yang nampilin gambar
        #Menu
        self.menubar = Menu(self.parent, tearoff=False)
        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.editMenu = Menu(self.menubar, tearoff=False)
        self.histogramMenu = Menu(self.menubar, tearoff=False)
        self.imageBrighteningMenu = Menu(self.editMenu, tearoff=False)
        self.arithmeticsMenu = Menu(self.editMenu, tearoff=False)
        self.booleanMenu = Menu(self.editMenu, tearoff=False)
        self.geometryMenu = Menu(self.editMenu, tearoff=False)
        self.rotationMenu = Menu(self.editMenu, tearoff=False)
        self.flipMenu = Menu(self.editMenu, tearoff=False)
        self.zoomMenu = Menu(self.editMenu, tearoff=False)
        self.showHistogramMenu = Menu(self.histogramMenu, tearoff=False)
        self.showNormalizedHistogramMenu = Menu(self.histogramMenu, tearoff=False)

        self.filename = ''
        self.status = 'Initializing'
        self.statusbar = Label(self.parent, text = self.status)
        self.statusbar.pack(side=BOTTOM, fill=X)
        # Image
        self.mainImageObject = image.Image() # object image utama
        self.operatorImageObject = image.Image() #object image yang dioperasikan
        self.imageArrMain = np.zeros((1,1), dtype=np.uint8) #array image utama hasil dari backend yang diubah 3D
        self.imageArrOperator = np.zeros((1,1), dtype=np.uint8) #array image yang akan dioperasikan 
        self.imageMainType = StringVar()
        self.imageOperatorType = StringVar()
        self.grayLevelMain = IntVar()
        self.grayLevelOperator = IntVar()
        self.mode = StringVar()
        self.format = StringVar()
        self.zoomStack = []
        
        self.scalarValue = DoubleVar()
        self.id = IntVar() #id command yang diberikan
        self.firstEntry = StringVar()
        self.secondEntry = StringVar()
        self.initUI()

    def initUI(self):
        self.parent.title("Mini Photoshop")
        self.parent.config(menu = self.menubar)
        self.fileMenu.add_command(label="Open", command=lambda: self.open_image("Open"))
        self.fileMenu.add_command(label="Save File", command = lambda: self.save_image("Save File"), state='disabled')
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu.add_command(label="Negative", command= lambda: self.negative("Negative"), state='disabled')
        self.editMenu.add_command(label="Grayscale", command=lambda: self.grayscale("Grayscale"), state='disabled')
        self.editMenu.add_command(label="Contrast Stretching", command= lambda: self.two_entry_input("Contrast Stretching"), state='disabled')
        self.editMenu.add_command(label="Log Transformation", command=lambda: self.scalar_input_window("Log Transformation"), state='disabled')
        self.editMenu.add_command(label="Inverse Log Transformation", command= lambda: self.scalar_input_window("Inverse Log Transformation"), state='disabled')
        self.editMenu.add_command(label="Power Transformation", command=lambda: self.scalar_input_window("Power Transformation"), state='disabled')
        self.editMenu.add_command(label="Gray Level Slicing", command= lambda: self.two_entry_input("Gray Level Slicing"), state='disabled')
        self.editMenu.add_command(label="Bit Plane Slicing", command=lambda: self.scalar_input_window("Bit Plane Slicing"), state='disabled')

        self.imageBrighteningMenu.add_command(label="Addition with Scalar", command = lambda: self.scalar_input_window("Addition with Scalar"), state='disabled')
        self.imageBrighteningMenu.add_command(label="Multiplication with Scalar", command = lambda: self.scalar_input_window("Multiplication with Scalar"), state='disabled')
        self.editMenu.add_cascade(label="Image Brightening", menu=self.imageBrighteningMenu)

        self.arithmeticsMenu.add_command(label="Addition with Image", command = lambda: self.open_image("Addition with Image"), state='disabled')
        self.arithmeticsMenu.add_command(label="Subtraction with Image", command =lambda: self.open_image("Subtraction with Image"), state='disabled')
        self.editMenu.add_cascade(label="Arithmetics", menu=self.arithmeticsMenu)

        self.booleanMenu.add_command(label="And with Image", command = lambda: self.open_image("And with Image"), state='disabled')
        self.booleanMenu.add_command(label="Not", command =lambda: self.negative("Not"), state='disabled')
        self.booleanMenu.add_command(label="Or with Image", command = lambda: self.open_image("Or with Image"), state='disabled')
        self.booleanMenu.add_command(label="Xor with Image", command =lambda: self.open_image("Xor with Image"), state='disabled')
        self.editMenu.add_cascade(label="Boolean", menu=self.booleanMenu)

        self.geometryMenu.add_command(label="Translation", command = lambda: self.two_entry_input("Translation"), state='normal')

        self.rotationMenu.add_command(label="Rotation 90 Clockwise", command = lambda: self.rotation("Rotation 90 Clockwise"), state='disabled')
        self.rotationMenu.add_command(label="Rotation 90 Counter Clockwise", command =lambda: self.rotation("Rotation 90 Counter Clockwise"), state='disabled')
        self.geometryMenu.add_cascade(label="Rotation", menu=self.rotationMenu)

        self.flipMenu.add_command(label="Flip Vertical", command = lambda: self.flip("Flip Vertical"), state='disabled')
        self.flipMenu.add_command(label="Flip Horizontal", command =lambda: self.flip("Flip Horizontal"), state='disabled')
        self.geometryMenu.add_cascade(label="Flip", menu=self.flipMenu)

        self.zoomMenu.add_command(label="Zoom In", command = lambda: self.zoom("Zoom In"), state='disabled')
        self.zoomMenu.add_command(label="Zoom Out", command =lambda: self.zoom("Zoom Out"), state='disabled')
        self.geometryMenu.add_cascade(label="Zoom", menu=self.zoomMenu)

        self.editMenu.add_cascade(label="Geometry", menu=self.geometryMenu)

        self.menubar.add_cascade(label="Edit", menu=self.editMenu)

        self.showHistogramMenu.add_command(label="Red", command = lambda: self.show_histogram("Show Histogram Red", 'red'), state='disabled')
        self.showHistogramMenu.add_command(label="Green", command =lambda: self.show_histogram("Show Histogram Green", 'green'), state='disabled')
        self.showHistogramMenu.add_command(label="Blue", command =lambda: self.show_histogram("Show Histogram Blue", 'blue'), state='disabled')
        self.histogramMenu.add_cascade(label="Show Histogram", menu=self.showHistogramMenu)

        self.showNormalizedHistogramMenu.add_command(label="Red", command = lambda: self.show_histogram("Show Normalized Histogram Red", 'red'), state='disabled')
        self.showNormalizedHistogramMenu.add_command(label="Green", command =lambda: self.show_histogram("Show Normalized Histogram Green", 'green'), state='disabled')
        self.showNormalizedHistogramMenu.add_command(label="Blue", command =lambda: self.show_histogram("Show Normalized Histogram Blue", 'blue'), state='disabled')
        self.histogramMenu.add_cascade(label="Show Normalized Histogram", menu=self.showNormalizedHistogramMenu)

        self.histogramMenu.add_command(label="Histogram Equalization", command =lambda: self.histogram_equalization("Histogram Equalization"), state='disabled')
        self.histogramMenu.add_command(label="Histogram Specification", command =lambda: self.show_histogram("Show Histogram Blue", 'blue'), state='disabled')

        self.menubar.add_cascade(label="Histogram", menu=self.histogramMenu)

    def save_array_to_backend(self, npArray, width, height, graylevel):
        imgObject = image.Image(height, width, graylevel)
        
        for i in range(width):
            for j in range(height):
                for k in range(3):
                    image.set(imgObject.getPixels(), i, j, k, int(npArray[i][j][k]))
        return imgObject

    def save_array_to_frontend(self, imgObject):
        arrTemp = np.zeros((imgObject.getHeight(), imgObject.getWidth(), 3), dtype='uint8')
        for i in range(imgObject.getHeight()):
            for j in range(imgObject.getWidth()):
                for k in range(3):
                    arrTemp[i][j][k] = image.get(imgObject.getPixels(), i, j, k)

        return arrTemp

    def npArrayHandler(self, command, imgType, npArray):
        if (command == 'convertTo3D'):
            if (imgType == 'RGB'):
                return npArray
            else:
                arrTemp = np.zeros((npArray.shape[0], npArray.shape[1], 3), dtype='uint8')
                if (imgType == 'GRAYSCALE'):
                    for i in range(npArray.shape[0]):
                        for j in range(npArray.shape[1]):
                            arrTemp[i][j][0] = npArray[i][j]
                            arrTemp[i][j][1] = npArray[i][j]
                            arrTemp[i][j][2] = npArray[i][j]

                elif (imgType == 'BINARY'):
                    for i in range(npArray.shape[0]):
                        for j in range(npArray.shape[1]):
                            if (npArray[i][j] or npArray[i][j] == 1):
                                arrTemp[i][j][0] = 1
                                arrTemp[i][j][1] = 1
                                arrTemp[i][j][2] = 1
                            else:
                                arrTemp[i][j][0] = 0
                                arrTemp[i][j][1] = 0
                                arrTemp[i][j][2] = 0
                return arrTemp

        elif (command == 'convert3DTo2D'):
            arrTemp = np.zeros((npArray.shape[0], npArray.shape[1]), dtype='uint8')
            for i in range(npArray.shape[0]):
                for j in range(npArray.shape[1]):
                    arrTemp[i][j] = npArray[i][j][0]
            return arrTemp

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
            "Not" : 9,
            "Or with Image" : 10,
            "Xor with Image" : 11,
            "Translation" : 12,
            "Rotation 90 Clockwise": 13,
            "Rotation 90 Counter Clockwise": 14,
            "Flip Vertical" : 15,
            "Flip Horizontal" : 16,
            "Zoom In" : 17,
            "Zoom Out" : 18,
            "Show Histogram Red" : 19,
            "Show Histogram Green" : 20,
            "Show Histogram Blue" : 21,
            "Show Normalized Histogram Red" : 22,
            "Show Normalized Histogram Green" : 23,
            "Show Normalized Histogram Blue" : 24,
            "Contrast Stretching": 25,
            "Log Transformation": 26,
            "Inverse Log Transformation": 27,
            "Power Transformation": 28,
            "Gray Level Slicing": 29,
            "Bit Plane Slicing": 30,
            "Histogram Equalization": 31,
            "Histogram Specification": 32
        } 

        idTemp = switcher.get(command, lambda: -1)
        if (not idTemp == -1):
            self.id.set(int(idTemp))

    def open_filename(self): 
        # open file dialog box to select image 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def show_image(self):
        switcher = {
            'RGB' : 'RGB',
            'GRAYSCALE' : 'L',
            'BINARY' : '1'
        }
        self.mode.set(switcher.get(self.imageMainType.get(), lambda: 'RGB'))
        if (self.mode.get() == 'RGB'):
            self.img = ImageTk.PhotoImage(Image.fromarray(self.imageArrMain, self.mode.get())) # photo image class tkinter
        else:
            arrTemp = self.npArrayHandler('convert3DTo2D', self.imageMainType.get(), self.imageArrMain)
            self.img = ImageTk.PhotoImage(Image.fromarray(arrTemp, self.mode.get())) # photo image class tkinter
        self.mainPanel = Label(image = self.img)
        self.mainPanel.pack()
        width = self.mainImageObject.getWidth()
        height = self.mainImageObject.getHeight()
        self.statusbar.config(text=self.filename + ' height = ' + str(height) + ' width = ' + str(width) + ' format = ' + self.format.get() + ' size = ' + str(os.path.getsize(self.filename)) + ' bytes')


    def open_image(self, command):
        self.idHandler(command)
        # # Select the Imagename from a folder
        x = self.open_filename()
        self.rawImg = Image.open(x) # Image Object PIL
        self.format.set(self.rawImg.format)
        if (self.id.get() == 0):
            self.imageArrMain = np.array(self.rawImg)
            if (self.rawImg.mode == 'RGB'):
                self.imageMainType.set('RGB')
                self.imageArrMain = self.npArrayHandler('convertTo3D', self.imageMainType.get(), self.imageArrMain)
            else:
                if (self.rawImg.mode == 'L'):
                    self.imageMainType.set('GRAYSCALE')
                elif (self.rawImg.mode == '1'):
                    self.imageMainType.set('BINARY')
                self.imageArrMain = self.npArrayHandler('convertTo3D',self.imageMainType.get(), self.imageArrMain)
            if (self.imageMainType.get() == 'GRAYSCALE' or self.imageMainType.get() == 'RGB'):
                self.grayLevelMain.set(256)
            elif (self.imageMainType.get() == 'BINARY'):
                self.grayLevelMain.set(2)

            self.mainImageObject = self.save_array_to_backend(self.imageArrMain, self.imageArrMain.shape[0], self.imageArrMain.shape[1], self.grayLevelMain.get())
            self.show_image()
            self.disable_sub_menu('Open')
            
        else:
            self.imageArrOperator = np.array(self.rawImg)
            if (self.rawImg.mode == 'RGB'):
                self.imageOperatorType.set('RGB')
                self.imageArrOperator = self.npArrayHandler('convertTo3D', self.imageOperatorType.get(), self.imageArrOperator)
            else:
                if (self.rawImg.mode == 'L'):
                    self.imageOperatorType.set('GRAYSCALE')
                elif (self.rawImg.mode == '1'):
                    self.imageOperatorType.set('BINARY')
                self.imageArrOperator = self.npArrayHandler('convertTo3D',self.imageOperatorType.get(), self.imageArrOperator)
            if (self.imageOperatorType.get() == 'GRAYSCALE' or self.imageOperatorType.get() == 'RGB'):
                self.grayLevelOperator.set(256)
            elif (self.imageOperatorType.get() == 'BINARY'):
                self.grayLevelOperator.set(2)

            self.operatorImageObject = self.save_array_to_backend(self.imageArrOperator, self.imageArrOperator.shape[0], self.imageArrOperator.shape[1], self.grayLevelOperator.get())

            id = self.id.get()
            if (id == 6): # Addition with Image
                self.mainImageObject = self.mainImageObject + self.operatorImageObject
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 7): # Subtraction with Image
                self.mainImageObject = self.mainImageObject - self.operatorImageObject
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 8): # And with Image
                self.mainImageObject = self.mainImageObject & self.operatorImageObject
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 10): # Or with Image
                self.mainImageObject = self.mainImageObject | self.operatorImageObject
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 11): # Xor with Image
                self.mainImageObject = self.mainImageObject ^ self.operatorImageObject
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()

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
        self.rawImg = Image.fromarray(self.imageArrMain, self.mode.get())

        self.rawImg.save(file)

    def enable_sub_menu(self, menu):
        self.fileMenu.entryconfig(menu, state='normal')

    def disable_sub_menu(self, menu):
        self.fileMenu.entryconfig(menu, state='disabled')

    def enable_all_sub_menu(self):
        self.editMenu.entryconfig("Negative", state='normal')
        self.editMenu.entryconfig("Grayscale", state='normal')
        self.imageBrighteningMenu.entryconfig("Addition with Scalar", state='normal')
        self.imageBrighteningMenu.entryconfig("Multiplication with Scalar", state='normal')
        self.arithmeticsMenu.entryconfig("Addition with Image", state='normal')
        self.arithmeticsMenu.entryconfig("Subtraction with Image", state='normal')
        self.booleanMenu.entryconfig("And with Image", state='normal')
        self.booleanMenu.entryconfig("Not", state='normal')
        self.booleanMenu.entryconfig("Or with Image", state='normal')
        self.booleanMenu.entryconfig("Xor with Image", state='normal')
        self.geometryMenu.entryconfig("Translation", state='normal')
        self.rotationMenu.entryconfig("Rotation 90 Clockwise", state='normal')
        self.rotationMenu.entryconfig("Rotation 90 Counter Clockwise", state='normal')
        self.flipMenu.entryconfig("Flip Vertical", state='normal')
        self.flipMenu.entryconfig("Flip Horizontal", state='normal')
        self.zoomMenu.entryconfig("Zoom In", state='normal')
        self.zoomMenu.entryconfig("Zoom Out", state='normal')
        self.showHistogramMenu.entryconfig("Red", state='normal')
        self.showHistogramMenu.entryconfig("Green", state='normal')
        self.showHistogramMenu.entryconfig("Blue", state='normal')
        self.showNormalizedHistogramMenu.entryconfig("Red", state='normal')
        self.showNormalizedHistogramMenu.entryconfig("Green", state='normal')
        self.showNormalizedHistogramMenu.entryconfig("Blue", state='normal')
        self.editMenu.entryconfig("Contrast Stretching", state='normal')
        self.editMenu.entryconfig("Log Transformation", state='normal')
        self.editMenu.entryconfig("Inverse Log Transformation", state='normal')
        self.editMenu.entryconfig("Power Transformation", state='normal')
        self.editMenu.entryconfig("Gray Level Slicing", state='normal')
        self.editMenu.entryconfig("Bit Plane Slicing", state='normal')
        self.histogramMenu.entryconfig("Histogram Equalization", state='normal')
        self.histogramMenu.entryconfig("Histogram Specification", state='normal')

    def negative(self, command):
        # ubah image object jadi negative
        self.idHandler(command)
        self.mainImageObject = self.mainImageObject.negative()

        arrTemp = self.save_array_to_frontend(self.mainImageObject)

        self.imageArrMain = arrTemp
        self.show_image()
        
    def grayscale(self, command):
        # ubah image object jadi grayscale
        self.idHandler(command)

        self.mainImageObject = self.mainImageObject.grayscale()

        arrTemp = self.save_array_to_frontend(self.mainImageObject)

        self.imageArrMain = arrTemp
        self.show_image()

    def scalar_input_window(self, command):
        self.idHandler(command)
        self.scalarInputWindow = Toplevel(self.parent)
        # sets the title of the Toplevel widget 
        title = ''
        if (self.id.get() == 30):
            title = 'Bit Plane Scalar Value'
        else:
            title = 'Scalar Value'
        self.scalarInputWindow.title(title) 
    
        # sets the geometry of toplevel 
        self.scalarInputWindow.geometry("600x100")
        self.scaleLabel = Label(self.scalarInputWindow)
        scale = Scale(self.scalarInputWindow, variable=self.scalarValue, from_=-255, to=255, orient=HORIZONTAL, length = 500)
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
        withoutCheck = [4, 5, 26, 27, 28, 30]
        if (id in withoutCheck):
            self.scalarInputWindow.destroy()
            if (id == 4): #Addition with Scalar
                self.mainImageObject = self.mainImageObject + int(self.scalarValue.get())
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 5): # Multiplication with Scalar
                self.mainImageObject = self.mainImageObject * int(self.scalarValue.get())
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 26): # Log Transformation
                self.mainImageObject = self.mainImageObject.logTransform(self.scalarValue.get())
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 27): # Inverse Log Transformation
                self.mainImageObject = self.mainImageObject.inverseLogTransform(self.scalarValue.get())
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 28): # Power Transformation
                self.mainImageObject = self.mainImageObject.powerTransform(self.scalarValue.get())
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()
            elif (id == 30):
                self.mainImageObject = self.mainImageObject.bitPlaneSlice(int(self.scalarValue.get()))
                arrTemp = self.save_array_to_frontend(self.mainImageObject)
                self.imageArrMain = arrTemp
                self.show_image()

        elif (id == 12 or id == 25 or id == 29):
            try:
                int(self.firstEntry.get())
                int(self.secondEntry.get())
                self.twoEntryInputWindow.destroy()
                if (id == 12): # Translation
                    self.mainImageObject = self.mainImageObject.translate(int(self.firstEntry.get()), int(self.secondEntry.get()))
                    arrTemp = self.save_array_to_frontend(self.mainImageObject)
                    self.imageArrMain = arrTemp
                    self.show_image()
                elif (id == 25): # Contrast Stretching
                    self.mainImageObject = self.mainImageObject.contrastStrech(int(self.firstEntry.get()), int(self.secondEntry.get()))
                    arrTemp = self.save_array_to_frontend(self.mainImageObject)
                    self.imageArrMain = arrTemp
                    self.show_image()
                elif (id == 29): # Gray Level Slicing
                    self.mainImageObject = self.mainImageObject.grayLevelSlice(int(self.firstEntry.get()), int(self.secondEntry.get()))
                    arrTemp = self.save_array_to_frontend(self.mainImageObject)
                    self.imageArrMain = arrTemp
                    self.show_image()
            except ValueError:
                self.feedback.config(text='Masukan hanya bisa integer, silakan coba lagi')
            
    def two_entry_input(self, command):
        self.idHandler(command)
        self.twoEntryInputWindow = Toplevel(self.parent)
        # sets the title of the Toplevel widget 
        title = ''
        textLabel1 = ''
        textLabel2 = ''
        
        if (self.id.get() == 12):
            title = "X and Y Value"
            textLabel1 = 'X'
            textLabel2 = 'Y'
        elif (self.id.get() == 25 or self.id.get() == 29):
            textLabel1 = 'rMin'
            textLabel2 = 'rMax'
            title = 'rMin and rMax Value'
        self.twoEntryInputWindow.title(title) 

        # sets the geometry of toplevel 
        self.twoEntryInputWindow.geometry("330x170")

        label1 = Label(self.twoEntryInputWindow, text=textLabel1).place(x = 30, y = 30)
        entry1 = Entry(self.twoEntryInputWindow, textvariable=self.firstEntry).place(x = 80, y = 30)
        label2 = Label(self.twoEntryInputWindow, text=textLabel2).place(x = 30, y = 60)
        entry2 = Entry(self.twoEntryInputWindow, textvariable=self.secondEntry).place(x = 80, y = 60)
        okButton = Button(self.twoEntryInputWindow, text ="OK", command = self.ok)
        self.feedback = Label(self.twoEntryInputWindow, text='')

        okButton.pack(side=BOTTOM, pady = 7)
        self.feedback.pack(side=BOTTOM, pady=12)

    def rotation(self, command):
        # rotate image object sesuai command
        self.idHandler(command)
        id = self.id.get()
        if (id == 13):
            self.mainImageObject = self.mainImageObject.rotate(True)
            arrTemp = self.save_array_to_frontend(self.mainImageObject)
            self.imageArrMain = arrTemp
            self.show_image()
        elif (id == 14):
            self.mainImageObject = self.mainImageObject.rotate(False)
            arrTemp = self.save_array_to_frontend(self.mainImageObject)
            self.imageArrMain = arrTemp
            self.show_image()

    def flip(self, command):
        # flip image object sesuai command
        self.idHandler(command)
        id = self.id.get()
        if (id == 15):
            self.mainImageObject = self.mainImageObject.flip(True)
            arrTemp = self.save_array_to_frontend(self.mainImageObject)
            self.imageArrMain = arrTemp
            self.show_image()
        elif (id == 16):
            self.mainImageObject = self.mainImageObject.flip(False)
            arrTemp = self.save_array_to_frontend(self.mainImageObject)
            self.imageArrMain = arrTemp
            self.show_image()

    def zoom(self, command):
        self.idHandler(command)
        id = self.id.get()
        if (id == 17): # Zoom In
            self.zoomStack.append(self.mainImageObject)
            self.mainImageObject = self.mainImageObject.zoom()
            arrTemp = self.save_array_to_frontend(self.mainImageObject)
            self.imageArrMain = arrTemp
            self.show_image()
        elif (id == 18): # Zoom Out
            self.mainImageObject = self.zoomStack.pop()
            arrTemp = self.save_array_to_frontend(self.mainImageObject)
            self.imageArrMain = arrTemp
            self.show_image()

    def show_histogram(self, command, color):
        self.idHandler(command)
        a=np.array([1,2,3,4,4,4,2,1,1,1,1, 256, 135])
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Pixel Frequency')
        plt.hist(a, bins = 256, range=[0, 256], color=color)
        plt.show()
    
    def histogram_equalization(self, command):
        self.idHandler(command)
        self.mainImageObject = self.mainImageObject.equalize()
        arrTemp = self.save_array_to_frontend(self.mainImageObject)
        self.imageArrMain = arrTemp
        self.show_image()

def main():
    root = Tk()
    root.geometry('500x400')
    app = App(root)
    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()