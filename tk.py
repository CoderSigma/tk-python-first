from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title('Robby')
        self.pack(fill=BOTH, expand=1)
        #quitButton = Button(self, text="quit", command=self.client_exit)
        #quitButton.place(x=544, y=312)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

        edit = Menu(menu)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='TEST', menu=edit)


    def showTxt(self):
        text = Label(self, text='BETA TEST')
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("800x500")
app = Window(root)

root.mainloop()
