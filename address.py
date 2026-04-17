import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("name and address")

        self.info_button = tkinter.Button(self.main_window, text= "show info", command= self.get_value)
        self.quit_button = tkinter.Button(self.main_window, text= "quit", command = self.main_window.destroy)

        self.info_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def get_value(self):
        self.address_label = tkinter.Label(self.main_window, text="Abe Phillips \n 67 Somewhere St, New York, NY")
        self.address_label.pack(side='top')



if __name__ == '__main__':
    my_gui = myGUI()
