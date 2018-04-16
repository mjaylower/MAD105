import tkinter


class MPGConverterGUI:
    def __init__(self):

        # create main window
        self.main_window = tkinter.Tk()

        # create 3 frames for entry, conversion and buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # label info and entry box for top frame
        self.prompt_label1 = tkinter.Label(self.top_frame, text='Number of gallons your car can hold:')
        self.prompt_label2 = tkinter.Label(self.top_frame, text='Number of miles you can drive on a full tank:')
        self.gas_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        # pack top frame
        self.prompt_label1.pack()
        self.gas_entry.pack()
        self.prompt_label2.pack()
        self.miles_entry.pack()

        # label info and get conversion data from convert function for middle frame
        self.description_label = tkinter.Label(self.mid_frame, text='Your MPG:')
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # pack middle frame
        self.description_label.pack(side='left')
        self.miles_label.pack(side='left')

        # create buttons for bottom frame to fun function based on entries or exit program
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy)

        # pack buttons frame
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames to window
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # create infinite loop
        tkinter.mainloop()

    # create the conversion function from entry boxes of top frame in window
    def convert(self):
        miles = int(self.miles_entry.get())  # get the gas entry
        gas = int(self.gas_entry.get())  # get the miles entry

        # create local variable based on equation of entry values
        mpg = format(miles / gas, '.2f')  # format equation 2 decimal places

        self.value.set(mpg)  # returns value back into middle frame


# create instance
mpg_convert = MPGConverterGUI()
