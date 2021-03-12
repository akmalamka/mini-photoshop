from tkinter import *
from PIL import ImageTk, Image

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Mini Photoshop")
        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Open')
        fileMenu.add_command(label='Save')
        menubar.add_cascade(label='File', menu=fileMenu)

        editMenu = Menu(menubar)
        editMenu.add_command(label="Negative")
        editMenu.add_command(label='Grayscale')
        menubar.add_cascade(label='Edit', menu=editMenu)

    def onExit(self):
        self.quit()

def main():
    root = Tk()
    root.geometry('2560x1600')
    app = App(root)
    image = ImageTk.PhotoImage(Image.open("../../img/car-1.ppm"))
    label = Label(image=image)
    label.pack()
    root.mainloop()


if __name__ == '__main__':
    main()