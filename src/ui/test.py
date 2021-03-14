from tkinter import *

def third_window(data):
    top = Toplevel()
    lbl = Label(top, text=data)
    lbl.place(x=20,y=20)
    top.wait_window()

def second_window(root, v):
    def event_btn():
        if len(v.get()) != 0:
            top.destroy()
    top = Toplevel()
    top.geometry("400x400+200+200")

    entry = Entry(top, textvariable = v, width=15)
    entry.place(x=30,y=30)
    btn = Button(top, text="Send", command = event_btn)
    btn.place(x=80, y=80)
    root.wait_window(top)

def main():
    def event_btn():
        second_window(root, v)
        print(v.get())
        root.withdraw()
        third_window(v.get())
    root = Tk()
    root.geometry("200x200+100+100")

    btn = Button(root, text="Test button", command = event_btn) 
    btn.place(x=50, y=50)

    v = StringVar()
    root.mainloop()

if __name__ == "__main__":
    main()