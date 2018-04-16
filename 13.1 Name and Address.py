import tkinter


class NameAddressGUI:

    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()

        # create 2 frames within the window
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # label info for top frame
        # initially no text will display
        self.prompt_label = tkinter.Label(self.top_frame)
        self.value = tkinter.StringVar()
        self.name_label = tkinter.Label(self.top_frame, textvariable=self.value)

        # pack top frame
        self.prompt_label.pack(side='left')
        self.name_label.pack(side='left')

        # create buttons for bottom frame
        self.show_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy)

        # pack buttons on bottom frame
        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames to window
        self.top_frame.pack()
        self.bottom_frame.pack()

        # create infinite loop
        tkinter.mainloop()

    # create function to set and return info value and display above in top frame
    def show(self):
        info = 'Michael Lower ' \
               '\n 8900 US Hwy 14 ' \
               '\n Crystal Lake, IL 60012'

        self.value.set(info)


# create an instance within the class
name_address = NameAddressGUI()
