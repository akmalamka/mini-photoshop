from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import os
import numpy as np
#import image_processing as ip

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.mainPanel = Label(self.parent) # panel yang nampilin gambar
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
        self.imageArrMain = np.zeros((1,1), dtype=np.uint8) #array image utama hasil dari backend
        self.imageArrOperation = np.zeros((1,1), dtype=np.uint8) #array image yang akan dioperasikan 
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
        self.booleanMenu.add_command(label="Not with Image", command =lambda: self.open_image("Not with Image"), state='disabled')
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

        self.zoomMenu.add_command(label="Zoom In", command = lambda: self.open_image("Zoom In"), state='disabled')
        self.zoomMenu.add_command(label="Zoom Out", command =lambda: self.open_image("Zoom Out"), state='disabled')
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

        self.menubar.add_cascade(label="Histogram", menu=self.histogramMenu)
        
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
            "Bit Plane Slicing": 30
        } 

        idTemp = switcher.get(command, lambda: -1)
        if (not idTemp == -1):
            self.id.set(int(idTemp))

    def open_filename(self): 
        # open file dialog box to select image 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def show_image(self):
        self.img = ImageTk.PhotoImage(self.rawImg) # photo image class tkinter
        self.mainPanel = Label(image = self.img)
        self.mainPanel.pack()
        width, height = self.rawImg.size
        self.statusbar.config(text=self.filename + ' height = ' + str(height) + ' width = ' + str(width) + ' format = ' + str(self.rawImg.format) + ' size = ' + str(os.path.getsize(self.filename)) + ' bytes')


    def open_image(self, command):
        self.idHandler(command)
        # # Select the Imagename from a folder
        x = self.open_filename()
        self.rawImg = Image.open(x) # Image Object PIL

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
            # self.img = ImageTk.PhotoImage(self.rawImg) 

            # create a label 
            # self.panel = Label(self.parent, image = self.img)

            # set the image as img 
            # self.panel.pack()
            # width, height = self.rawImg.size
            # self.statusbar.config(text=self.filename + ' height = ' + str(height) + ' width = ' + str(width) + ' format = ' + str(self.rawImg.format) + ' size = ' + str(os.path.getsize(self.filename)) + ' bytes')
            # panggil fungsi backend, kasih parameter np.array(self.rawImg)
            self.show_image()
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
        title = ''
        if (self.id.get() == 30):
            title = 'Bit Plane Scalar Value'
        else:
            title = 'Scalar Value'
        self.scalarInputWindow.title(title) 
    
        # sets the geometry of toplevel 
        self.scalarInputWindow.geometry("200x100")
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
        withoutCheck = [4, 5, 26, 27, 28, 30]
        if (id in withoutCheck):
            self.scalarInputWindow.destroy()
        elif (id == 12 or id == 25 or id == 29):
            try:
                #case kalo contrast stretching ato translation
                int(self.firstEntry.get())
                int(self.secondEntry.get())
                self.twoEntryInputWindow.destroy()
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

    def show_histogram(self, command, color):
        self.idHandler(command)
        a=np.array([1,2,3,4,4,4,2,1,1,1,1, 256, 135])
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Pixel Frequency')
        plt.hist(a, bins = 256, range=[0, 256], color=color)
        plt.show()
    

def main():
    root = Tk()
    root.geometry('500x400')
    app = App(root)
    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()