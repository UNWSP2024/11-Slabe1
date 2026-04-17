import tkinter


class myGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("saying")

        self.label = tkinter.Label(self.main_window, text= "It's sad that a family can be torn apart by something as simple as a pack of wolves")

        self.label.pack()
        
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = myGUI()