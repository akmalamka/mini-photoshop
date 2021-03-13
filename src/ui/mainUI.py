from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import rawpy
import imageio

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Mini Photoshop")
        menubar = Menu(self.parent, tearoff=False)
        self.parent.config(menu = menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Open Image', command=self.open_img)
        fileMenu.add_command(label='Save')
        menubar.add_cascade(label='File', menu=fileMenu)

        editMenu = Menu(menubar, tearoff=False)
        editMenu.add_command(label="Negative")
        editMenu.add_command(label='Grayscale')
        menubar.add_cascade(label='Edit', menu=editMenu)

    def onExit(self):
        self.quit()

    def openfilename(self): 

        # open file dialog box to select image 
        # The dialogue box has a title "Open" 
        filename = filedialog.askopenfilename(title ='"Open') 
        return filename 

    def open_img(self): 
        # Select the Imagename from a folder 
        x = self.openfilename() 

        # opens the image 
        img = Image.open(x) 
        
        # resize the image and apply a high-quality down sampling filter 
        # img = img.resize((250, 250), Image.ANTIALIAS) 

        # PhotoImage class is used to add image to widgets, icons etc 
        img = ImageTk.PhotoImage(img) 

        # create a label 
        panel = Label(self.parent, image = img) 
        
        # set the image as img 
        panel.image = img 
        panel.grid(row = 2) 


def main():
    root = Tk()
    root.geometry('2560x1600')
    app = App(root)
    
    # path = "../../img/sample.raw"
    # with rawpy.imread(path) as raw:
    #     rgb = raw.postprocess()
    # imageio.imsave('default.tiff', rgb)
    # image = ImageTk.PhotoImage(Image.open("../../img/sample.raw"))
    # label = Label(image=image)
    # label.pack()
    # Allow Window to be resizable 
    root.resizable(width = True, height = True) 
    root.mainloop()


if __name__ == '__main__':
    main()