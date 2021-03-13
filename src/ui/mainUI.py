from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile 

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.panel = Label(self.parent)
        self.menubar = Menu(self.parent, tearoff=False)
        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.editMenu = Menu(self.menubar, tearoff=False)
        self.filename = ''
        self.initUI()

    def initUI(self):

        self.parent.title("Mini Photoshop")
        self.parent.config(menu = self.menubar)
        self.fileMenu.add_command(label="Open", command=self.openImage)
        self.fileMenu.add_command(label="Save File", command = self.saveImage)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu.add_command(label="Negative")
        self.editMenu.add_command(label="Grayscale")
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)

    def onExit(self):
        self.quit()

    def openfilename(self): 

        # open file dialog box to select image 
        # The dialogue box has a title "Open" 
        self.filename = filedialog.askopenfilename(title ='Open') 
        return self.filename 

    def openImage(self): 
        # # Select the Imagename from a folder 
        x = self.openfilename()

        # opens the image 
        self.img = Image.open(x) 

        # PhotoImage class is used to add image to widgets, icons etc 
        self.img = ImageTk.PhotoImage(self.img) 

        # create a label 
        self.panel = Label(self.parent, image = self.img)

        # set the image as img 
        self.panel.image = self.img 
        self.panel.grid(row = 2)
        labelimage = Label(self.parent, text=self.filename)
        labelimage.grid(row = 4)
        self.disableOpenSubMenu()
    

    def saveImage(self): 
        files = [('All Files', '*.*'),  
                ('PGM Files', '*.pgm'), 
                ('PPM Files', '*.ppm'),
                ('PBM Files', '*.pbm'),
                ('BMP Files', '*.bmp')] 
        file = asksaveasfile(filetypes = files, defaultextension = files)
        if file is None:
            return None
        img_to_save=open(self.filename,"rb").read()
        file.write(img_to_save)
        file.close() 

    def enableOpenSubMenu(self):
        self.fileMenu.entryconfig('Open', state='normal')

    def disableOpenSubMenu(self):
        self.fileMenu.entryconfig('Open', state='disabled')


def main():
    root = Tk()
    root.geometry('2560x1600')
    # w = Label(root)
    # w.pack()
    app = App(root)
    
    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()