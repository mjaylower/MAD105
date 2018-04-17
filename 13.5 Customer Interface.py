import tkinter
import tkinter.messagebox


# INITIATE CLASS TO CREATE WINDOWS AND FUNCTIONS
class MyGUI:
    def __init__(self):

        # CREATE WINDOW
        self.main_window = tkinter.Tk()

        # DEFINE FRAMES TO BE USED
        # Header Frame to include background color, to blend with background color of brewery_name_header
        self.header_frame = tkinter.Frame(self.main_window, bg='#e0990b')
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # HEADER FRAME
        # First Label to be formatted with BG color and font size, bold/larger
        # Second Label to be formatted with font and size
        self.brewery_name_header = tkinter.Label(self.header_frame, text='Crabby Mike\'s Brewery', bg='#e0990b', font='Helvetica 15 underline bold')
        self.explanation_label = tkinter.Label(self.header_frame, text='Make your selections below to calculate total', font='Helvetica 12')

        # PACK HEADER FRAME
        self.brewery_name_header.pack()
        self.explanation_label.pack()

        # TOP FRAME
        # Initiate check box variables
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()

        # set variable's values to 0 of previously defined check boxes
        # 0 indicates the check box is unchecked - when checked values change to 1
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)

        # INITIATE CHECK BOXES
        # indicate frame location, display text,
        # and associated with previously defined checkbox variable
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Azaccalypse (IIPA) - 8.8% - $6.89', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Sunrise Hefe (Hefeweizen) - 4.5% - $4.09', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Quiet Man (Irish Red) - 6.4% - $4.49', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Hot Spark (Blonde Ale) - 4.5% - $3.99', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Coal Dust (Black IPA) - 7.2% - $5.89', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Sunset Sour (Berliner Weisse) - 2.9% - $4.89', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Electricity (NEIPA) - 5.4% - $5.99', variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame, text='Overtime Porter (Porter) - 5.8% - $5.49', variable=self.cb_var8)

        # PACK CHECKBOXES TO ANCHOR/ALIGN TO THE WEST(LEFT)
        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')
        self.cb8.pack(anchor='w')

        # MIDDLE FRAME
        # Middle Frame will include the total and label explanation
        # Also, retrieves currency value from 'TOTAL' function through self.sub_total
        # Includes label font formatting of bold font and color
        # Including tax_label here for formatting issues
        self.description_label = tkinter.Label(self.mid_frame, text='Total*:', bg='yellow', font='bold')
        self.sub_total = tkinter.StringVar()
        self.sub_total_label = tkinter.Label(self.mid_frame, textvariable=self.sub_total, font='bold', bg='yellow')
        self.tax_label = tkinter.Label(self.bottom_frame, text='*All prices include local sales tax', font='Helvetica 8')

        # PACK MIDDLE FRAME
        self.description_label.pack(side='left')
        self.sub_total_label.pack(side='left')
        self.tax_label.pack(side='bottom')

        # BOTTOM FRAME
        # Buttons for calculation and exit program
        # Calculate formatted to be Green, ridged border and bold/larger
        # Exit formatted to be Red, ridged border and bold/larger
        self.ok_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.total, bg='green', relief='ridge', bd=4, font='bold')
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy, bg='red', relief='ridge', bd=4, font='bold')

        # PACK BOTTOM FRAME
        self.ok_button.pack(side='left')
        self.exit_button.pack(side='right')

        # PACK ALL FRAMES TO MAIN_WINDOW
        self.header_frame.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # INITIATE WINDOW LOOP TO RUN UNTIL EXITED
        tkinter.mainloop()

    # CREATE TOTAL FUNCTION TO CALCULATE VALUES BASED ON CHECKBOX SELECTIONS
    def total(self):
        # CREATE LOCAL VARIABLES FOR PRICES OF
        # ITEMS BEING USED IN ABOVE WINDOW
        # These are local variables, so able to use
        # same variable names as before without effecting others
        cb1 = 6.89
        cb2 = 4.09
        cb3 = 4.49
        cb4 = 3.99
        cb5 = 5.89
        cb6 = 4.89
        cb7 = 5.99
        cb8 = 5.49

        # create sub_total local variable and calculate based
        # format sub_total for currency
        # each self.cb_var will return either 1 or 0 from the .get method.
        # That will be multiplied by local variable(price) and
        # then add all items together for total.
        sub_total = '${:,.2f}'.format((self.cb_var1.get()*cb1) + (self.cb_var2.get()*cb2) + (self.cb_var3.get()*cb3) + (self.cb_var4.get()*cb4) + (self.cb_var5.get()*cb5) + (self.cb_var6.get()*cb6) + (self.cb_var7.get()*cb7) + (self.cb_var8.get()*cb8))

        # return local variable sub_total back to middle_frame command method for displaying
        self.sub_total.set(sub_total)


# create an instance
my_gui = MyGUI()
