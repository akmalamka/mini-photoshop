from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import os

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
        self.initUI()

    def initUI(self):

        self.parent.title("Mini Photoshop")
        self.parent.config(menu = self.menubar)
        self.fileMenu.add_command(label="Open", command=self.open_image)
        self.fileMenu.add_command(label="Save File", command = self.save_image, state='disabled')
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu.add_command(label="Negative", command=self.negative)
        self.editMenu.add_command(label="Grayscale", command=self.grayscale)
        self.editMenu.add_command(label="Image Brightening", command=self.image_brightening)
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)

    def open_filename(self): 

        # open file dialog box to select image 
        # The dialogue box has a title "Open" 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def open_image(self): 
        # # Select the Imagename from a folder 
        x = self.open_filename()
        # opens the image 
        self.rawImg = Image.open(x) 

        # PhotoImage class is used to add image to widgets, icons etc 
        self.img = ImageTk.PhotoImage(self.rawImg) 

        # create a label 
        self.panel = Label(self.parent, image = self.img)

        # set the image as img 
        self.panel.image = self.img 
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

    # def print_val(self, val):


    def image_brightening(self):
        # Toplevel object which will  
        # be treated as a new window 
        scalarInputWindow = Toplevel(self.parent) 
    
        # sets the title of the 
        # Toplevel widget 
        scalarInputWindow.title("Scalar Value") 
    
        # sets the geometry of toplevel 
        scalarInputWindow.geometry("200x200")
        # var = DoubleVar() 

        scale = Scale(scalarInputWindow, from_=0, to=255, orient=HORIZONTAL)
        scale.pack()

        scaleLabel = Label(scalarInputWindow)
        selection = "Value = " + str(scale.get())
        scaleLabel.config(text = selection)
        scaleLabel.pack()

def main():
    root = Tk()
    root.geometry('500x400')
    app = App(root)
    
    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()