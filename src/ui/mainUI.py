# #!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# # -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

# from tkinter import *
 
# class App(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.grid()
#         self.widgets()
    
#     def widgets(self):
#         menubar = Menu(root)
#         menubar.add_command(label="File")
#         menubar.add_command(label="Quit", command=root.quit())

#         root.config(menu=menubar)

# root=Tk()
# root.title('Mini Photoshop')
# root.geometry('2560x1600')
# app=App(root)
# root.mainloop()

from tkinter import *

class Example(Frame):

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
        # fileMenu.add_command(label='New Project', command=doNothing)
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
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()