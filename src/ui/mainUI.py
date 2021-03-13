from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile 

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.imageOpened = False
        self.panel = Label(self.parent)
        self.menubar = Menu(self.parent, tearoff=False)
        self.fileMenu = Menu(self.menubar, tearoff=False)
        self.editMenu = Menu(self.menubar, tearoff=False)
        # self.controller = controller
        self.initUI()

    def initUI(self):

        self.parent.title("Mini Photoshop")
        # menubar = Menu(self.parent, tearoff=False)
        self.parent.config(menu = self.menubar)
        # fileMenu = Menu(self.menubar, tearoff=False)
        self.fileMenu.add_command(label="Open", command=self.openImage)
        self.fileMenu.add_command(label="Save File", command = lambda : self.saveImage)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        # editMenu = Menu(self.menubar, tearoff=False)
        # self.editMenu.add_command(label="Blank the Canvas", command=self.blankTheCanvas)
        self.editMenu.add_command(label="Negative")
        self.editMenu.add_command(label="Grayscale")
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)
        # print(self.menubar.entrycget(0, 'state'))

    def onExit(self):
        self.quit()

    def openfilename(self): 

        # open file dialog box to select image 
        # The dialogue box has a title "Open" 
        filename = filedialog.askopenfilename(title ='Open') 
        return filename 

    def openImage(self): 
        # Select the Imagename from a folder 
        x = self.openfilename() 

        # opens the image 
        img = Image.open(x) 

        # PhotoImage class is used to add image to widgets, icons etc 
        img = ImageTk.PhotoImage(img) 

        # create a label 
        self.panel = Label(self.parent, image = img) 
        
        # set the image as img 
        self.panel.image = img 
        self.panel.grid(row = 2)
        self.imageOpened = True 
        self.disableOpenSubMenu()
    

    def saveImage(self): 
        files = [('All Files', '*.*'),  
                ('PGM Files', '*.pgm'), 
                ('PPM Files', '*.ppm'),
                ('PBM Files', '*.pbm'),
                ('BMP Files', '*.BMP')] 
        file = asksaveasfile(filetypes = files, defaultextension = files)

    # def blankTheCanvas(self):
    #     self.panel = Label()
    #     self.disableMenu()

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