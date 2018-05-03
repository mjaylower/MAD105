import pickle
import tkinter
import tkinter.messagebox


# GUI INTERFACE FOR MAIN MENU
class CustomerDirectoryMainMenu:

    def __init__(self, master, name_and_contact):  # PASSING THE ROOT WINDOW AND DICTIONARY

        # CREATING LOCAL VARIABLES FROM PASSED ARGUMENTS
        self.master = master
        self.name_and_contact = name_and_contact

        # CREATE GUI MAIN WINDOW
        self.master.title('Customer Directory')
        self.master.geometry('350x300')
        self.master.protocol('WM_DELETE_WINDOW', self.quit_and_save)  # CLICKING 'X' WILL RUN QUIT AND SAVE FUNCTION

        # WINDOW FRAMES TO BE USED
        self.header_frame = tkinter.Frame(self.master)  # HEADER FRAME TO EXPLAIN PROGRAM
        self.first_frame = tkinter.Frame(self.master)  # FRAME TO DISPLAY BUTTON OPTIONS

        # HEADER FRAME
        self.header_label = tkinter.Label(self.header_frame, text='CONTACT INFORMATION DIRECTORY', font='underline', width=50)
        self.header_label.pack()

        # CREATE BUTTONS IN FIRST FRAME
        self.add_button = tkinter.Button(self.first_frame, text='ADD', cursor='hand2', relief='ridge', width=15, bd=3, command=self.open_add_window)
        self.lookup_button = tkinter.Button(self.first_frame, text='LOOKUP', cursor='hand2', relief='ridge', width=15, bd=3, command=self.open_lookup_window)
        self.change_button = tkinter.Button(self.first_frame, text='CHANGE', cursor='hand2', relief='ridge', width=15, bd=3,  command=self.open_change_window)
        self.delete_button = tkinter.Button(self.first_frame, text='DELETE', cursor='hand2', relief='ridge', width=15, bd=3,  command=self.open_delete_window)
        self.save_exit_button = tkinter.Button(self.first_frame, text='SAVE & EXIT', cursor='hand2', bd=4, bg='red', font='bold', command=self.quit_and_save)

        # PACK BUTTONS
        self.add_button.pack(pady=5)
        self.lookup_button.pack(pady=5)
        self.change_button.pack(pady=5)
        self.delete_button.pack(pady=5)
        self.save_exit_button.pack(pady=35)

        # PACK FRAMES IN MAIN WINDOW
        self.header_frame.pack()
        self.first_frame.pack()

    # WHEN LOOK UP BUTTON CLICKED, FUNCTION EXECUTES AND CALLS THE LOOKUP_WINDOW CLASS
    def open_lookup_window(self):
        LookupWindow(self.master, self.name_and_contact)

    # WHEN ADD BUTTON CLICKED, FUNCTION EXECUTES AND CALLS THE ADD_WINDOW CLASS
    def open_add_window(self):
        AddWindow(self.master, self.name_and_contact)

    # WHEN CHANGE BUTTON CLICKED, FUNCTION EXECUTES AND CALLS THE CHANGE_WINDOW CLASS
    def open_change_window(self):
        FirstChangeWindow(self.master, self.name_and_contact)

    # WHEN DELETE BUTTON CLICKED, FUNCTION EXECUTES AND CALLS THE DELETE_WINDOW CLASS
    def open_delete_window(self):
        DeleteWindow(self.master, self.name_and_contact)

    # WHEN SAVE & EXIT IS CLICKED OR MAIN WINDOW IS 'X' OUT, FUNCTION EXECUTES
    # SAVE DATA TO FILE AND EXIT PROGRAM
    # ALL KEY:VALUE PAIRS WILL BE SAVED
    # NAME_AND_EMAIL DICTIONARY WILL BE WRITTEN TO NAME_AND_EMAIL.DAT FILE
    # MAIN WINDOW WILL CLOSE AND PROGRAM WILL END
    def quit_and_save(self):
        save_file = open('name_and_contact.dat', 'wb')  # OPEN FILE AND ENABLE BINARY WRITING 'WB'
        pickle.dump(self.name_and_contact, save_file)  # DUMP NEW DATA FROM DICTIONARY INTO FILE
        save_file.close()  # CLOSE FILE
        self.master.destroy()


# CREATE GUI FOR POP UP WINDOW WHEN 'ADD' IS SELECTED IN THE MAIN WINDOW
class AddWindow:

    def __init__(self, master, name_and_contact):
        self.master = master
        self.name_and_contact = name_and_contact
        self.add_window = tkinter.Toplevel(self.master)
        self.add_window.title('CREATE NEW CONTACT')
        self.add_window.geometry('350x300')

        # DEFINE FRAMES
        self.header_frame = tkinter.Frame(self.add_window)
        self.first_frame = tkinter.Frame(self.add_window)
        self.second_frame = tkinter.Frame(self.add_window)
        self.third_frame = tkinter.Frame(self.add_window)
        self.forth_frame = tkinter.Frame(self.add_window)
        self.fifth_frame = tkinter.Frame(self.add_window)
        self.sixth_frame = tkinter.Frame(self.add_window)

        # HEADER FRAME
        self.header_label = tkinter.Label(self.header_frame, text='Please Enter Contact Information Below', font='bold')
        self.header_label.pack(side='top', pady=15)

        # FIRST FRAME
        self.first_name_entry_label = tkinter.Label(self.first_frame, text='First Name', width=10)
        self.first_name_entry = tkinter.Entry(self.first_frame, width=40, bd=3)
        self.first_name_entry_label.pack(side='left', padx=2, pady=2)
        self.first_name_entry.pack(side='left', pady=2)

        # SECOND FRAME
        self.last_name_entry_label = tkinter.Label(self.second_frame, text='Last Name', width=10)
        self.last_name_entry = tkinter.Entry(self.second_frame, width=40, bd=3)
        self.last_name_entry_label.pack(side='left', padx=2, pady=2)
        self.last_name_entry.pack(side='left', pady=2)

        # THIRD FRAME
        self.email_entry_label = tkinter.Label(self.third_frame, text='Email', width=10)
        self.email_entry = tkinter.Entry(self.third_frame, width=40, bd=3)
        self.email_entry_label.pack(side='left', padx=2, pady=2)
        self.email_entry.pack(side='left', pady=2)

        # FORTH FRAME
        self.phone_entry_label = tkinter.Label(self.forth_frame, text='Phone', width=10)
        self.phone_entry = tkinter.Entry(self.forth_frame, width=40, bd=3)
        self.phone_entry_label.pack(side='left', padx=2, pady=2)
        self.phone_entry.pack(side='left', pady=2)

        # FIFTH FRAME
        self.address_entry_label = tkinter.Label(self.fifth_frame, text='Address', width=10)
        self.address_entry = tkinter.Entry(self.fifth_frame, width=40, bd=3)
        self.address_entry_label.pack(side='left', padx=2, pady=2)
        self.address_entry.pack(side='left', pady=2)

        # SIXTH FRAME
        self.submit_button = tkinter.Button(self.sixth_frame, text='Submit', cursor='hand2', bg='green', font='bold', command=self.add)  # WHEN SUBMIT BUTTON CLICKED, ADD METHOD RAN
        self.cancel_button = tkinter.Button(self.sixth_frame, text='Cancel', cursor='hand2', bg='red', font='bold', command=self.add_window.destroy)  # WHEN CANCEL BUTTON CLICKED, RETURN TO MAIN MENU AND CLOSE POP UP WINDOW
        self.submit_button.pack(side='top', pady=20)
        self.cancel_button.pack(side='bottom')

        self.header_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.forth_frame.pack()
        self.fifth_frame.pack()
        self.sixth_frame.pack()

    def add(self):

        name = str(self.first_name_entry.get() + ' ' + self.last_name_entry.get())  # CREATES A STRING OF COMBINED NAMES
        email = self.email_entry.get()  # CREATE VARIABLE FROM ENTRY
        phone = self.phone_entry.get()  # CREATE VARIABLE FROM ENTRY
        address = str(self.address_entry.get())  # CREATE VARIABLE FROM ENTRY

        if name not in self.name_and_contact:  # IF NAME DOESN'T EXIST, ADD NEW KEY-VALUE PAIR TO NAME_AND_EMAIL DICTIONARY
            self.name_and_contact[name] = email, phone, address
            tkinter.messagebox.showinfo('Information', name + ' has been added to your database')

        else:
            tkinter.messagebox.showinfo('Information', name + ' already exists.\nPlease select the "CHANGE" option to make an update to ' + name + "'s information.")

        self.add_window.destroy()  # CLOSES OUT THE ADD POPUP WINDOW AFTER MESSAGE BOX IS CLOSED

    # CREATE GUI FOR POP UP WINDOW WHEN 'LOOKUP' IS SELECTED IN THE MAIN WINDOW
    # IN THE POP UP WINDOW - USAGE OF THE PREVIOUSLY DEFINED OBJECTS WILL BE USED
    # SUBMIT BUTTON WILL CALL UPON THE 'LOOKUP' METHOD


class LookupWindow:

    def __init__(self, master, name_and_contact):

        self.master = master
        self.name_and_contact = name_and_contact

        self.lookup_window = tkinter.Toplevel(master)
        self.lookup_window.title('LOOKUP EXISTING CONTACT')
        self.lookup_window.geometry('350x300')

        self.first_frame = tkinter.Frame(self.lookup_window)
        self.second_frame = tkinter.Frame(self.lookup_window)
        self.third_frame = tkinter.Frame(self.lookup_window)

        self.description_label = tkinter.Label(self.first_frame, text='ENTER NAME TO LOOK UP CONTACT INFORMATION.')
        self.description_label.pack(pady=5)

        self.name_entry_label = tkinter.Label(self.second_frame, text='Full Name', font='bold')
        self.name_entry = tkinter.Entry(self.second_frame, width=40, bd=3)

        self.name_entry_label.pack(pady=5)
        self.name_entry.pack()

        self.submit_button = tkinter.Button(self.third_frame, text='Submit', cursor='hand2', bg='green', font='bold', command=self.lookup)
        self.cancel_button = tkinter.Button(self.third_frame, text='Cancel', cursor='hand2', bg='red', font='bold', command=self.lookup_window.destroy)

        self.submit_button.pack(side='top', pady=20)
        self.cancel_button.pack(side='bottom')

        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()

    def lookup(self):
        name = self.name_entry.get()

        if name in self.name_and_contact:
            values = self.name_and_contact[name]
            email = values[0]
            phone = values[1]
            address = str(values[2])

            tkinter.messagebox.showinfo('Information for ' + name, 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + 'Address: ' + address)

        else:
            tkinter.messagebox.showinfo('Information', name + "'s Name Was Not Found.\nPlease Select the ADD Button to Append Your Database.")

        self.lookup_window.destroy()  # CLOSES OUT THE ADD POPUP WINDOW AFTER MESSAGE BOX IS CLOSED

    # CREATE GUI FOR POP UP WINDOW WHEN 'CHANGE' IS SELECTED IN THE MAIN WINDOW
    # IN THE POP UP WINDOW - USAGE OF THE PREVIOUSLY DEFINED OBJECTS WILL BE USED
    # SUBMIT BUTTON WILL CALL UPON THE 'CHANGE' METHOD


class FirstChangeWindow:

    def __init__(self, master, name_and_contact):
        self.master = master
        self.name_and_contact = name_and_contact

        # CREATE WINDOW
        self.change_window = tkinter.Toplevel(master)
        self.change_window.title('SEARCH EXISTING CONTACT')
        self.change_window.geometry('350x300')

        # ESTABLISH FRAMES
        self.header_frame = tkinter.Frame(self.change_window)
        self.first_frame = tkinter.Frame(self.change_window)
        self.second_frame = tkinter.Frame(self.change_window)

        # HEADER FRAME
        self.header_label = tkinter.Label(self.header_frame, text='ENTER NAME TO BE UPDATED')
        self.header_label.pack(pady=15)

        # FIRST FRAME
        self.name_entry_label = tkinter.Label(self.first_frame, text='Full Name', font='bold')
        self.name_entry = tkinter.Entry(self.first_frame, width=40, bd=3)
        self.name_entry_label.pack()
        self.name_entry.pack()

        # SECOND FRAME
        self.submit_button = tkinter.Button(self.second_frame, text='Submit', cursor='hand2', bg='green', font='bold', command=self.open_first_change_window)
        self.cancel_button = tkinter.Button(self.second_frame, text='Cancel', cursor='hand2', bg='red', font='bold', command=self.change_window.destroy)
        self.submit_button.pack(side='top', pady=20)
        self.cancel_button.pack(side='bottom')

        # PACK FRAMES
        self.header_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()

    def open_first_change_window(self):
        name = self.name_entry.get()

        if name in self.name_and_contact:  # IF NAME EXIST IN DICTIONARY, ASK USER FOR NEW EMAIL
            SecondChangeWindow(self.change_window, self.name_and_contact, self.name_entry.get(), self.change_window)

        else:
            tkinter.messagebox.showinfo('Information', name + "'s Name Was Not Found\nPlease Select the ADD Button to Append Your Database.")

            self.change_window.destroy()  # close out window and return to main menu


# SECOND POP UP WINDOW AFTER IT IS DETERMINED THAT NAME SEARCHED EXISTS IN DATABASE
# PRE-FILLS FIELDS READ FROM LIST BASED ON NAME ENTERED IN FIRST POP UP WINDOW(CHANGE)
class SecondChangeWindow:

    def __init__(self, master, name_and_contact, name_entry, change_window):

        self.master = master
        self.name_and_contact = name_and_contact
        self.name = name_entry
        self.first_change_window = change_window

        # READS VALUES FROM DICTIONARY BASED ON NAME ENTERED AND PASSED DOWN FROM CHANGE WINDOW CLASS
        # LOCAL VARIABLES CREATED FOR EACH INDEX/VALUE IN THE PAIRS
        # LOCAL VARIABLES ARE USED TO PRE-FILL ENTRY FIELDS TO MAKE CHANGES
        self.values = name_and_contact[name_entry]
        self.email = self.values[0]
        self.phone = self.values[1]
        self.address = str(self.values[2])

        self.second_change_window = tkinter.Toplevel(master)
        self.second_change_window.title('Update Information for ' + name_entry)
        self.second_change_window.geometry('350x300')

        self.header_frame = tkinter.Frame(self.second_change_window)
        self.first_frame = tkinter.Frame(self.second_change_window)
        self.second_frame = tkinter.Frame(self.second_change_window)
        self.third_frame = tkinter.Frame(self.second_change_window)
        self.forth_frame = tkinter.Frame(self.second_change_window)
        self.fifth_frame = tkinter.Frame(self.second_change_window)

        # HEADER FRAME
        self.header_label = tkinter.Label(self.header_frame, text='Update information for ' + name_entry)
        self.header_label.pack(pady=15)

        # FIRST FRAME
        self.name_entry_label = tkinter.Label(self.first_frame, text='Name', width=10)
        self.name_entry = tkinter.Entry(self.first_frame, width=40, bd=3)
        self.name_entry.insert(0, self.name)
        self.name_entry_label.pack(side='left', padx=2, pady=2)
        self.name_entry.pack(side='left', pady=2)

        # SECOND FRAME
        self.email_entry_label = tkinter.Label(self.second_frame, text='Email', width=10)
        self.email_entry = tkinter.Entry(self.second_frame, width=40, bd=3)
        self.email_entry.insert(0, self.email)
        self.email_entry_label.pack(side='left', padx=2, pady=2)
        self.email_entry.pack(side='left', pady=2)

        # THIRD FRAME
        self.phone_entry_label = tkinter.Label(self.third_frame, text='Phone', width=10)
        self.phone_entry = tkinter.Entry(self.third_frame, width=40, bd=3)
        self.phone_entry.insert(0, self.phone)
        self.phone_entry_label.pack(side='left', padx=2, pady=2)
        self.phone_entry.pack(side='left', pady=2)

        # FORTH FRAME
        self.address_entry_label = tkinter.Label(self.forth_frame, text='Address', width=10)
        self.address_entry = tkinter.Entry(self.forth_frame, width=40, bd=3)
        self.address_entry.insert(0, self.address)
        self.address_entry_label.pack(side='left', padx=2, pady=2)
        self.address_entry.pack(side='left', pady=2)

        # FIFTH FRAME
        self.submit_button = tkinter.Button(self.fifth_frame, text='Submit', cursor='hand2', font='bold', bg='green', command=self.change)
        self.cancel_button = tkinter.Button(self.fifth_frame, text='Cancel', cursor='hand2', font='bold', bg='red', command=self.second_change_window.destroy)
        self.submit_button.pack(side='top', pady=20)
        self.cancel_button.pack(side='bottom')

        # PACK FRAMES
        self.header_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.forth_frame.pack()
        self.fifth_frame.pack()

    # METHOD WILL CHANGE EMAIL WHEN A NAME IS FOUND
    def change(self):
        # CREATES LOCAL VARIABLES FROM INSTANCES CREATED IN __INIT__
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = str(self.address_entry.get())

        if self.name == name:  # if name is not changed
            del self.name_and_contact[name]  # deletes original(pre-filled) key:value pairs

            self.name_and_contact[name] = email, phone, address  # creates new key:value pairs with same name

            tkinter.messagebox.showinfo('Information', 'Thank you, ' + name + "'s information has been updated.")

        elif self.name != name:  # if name is changed
            if name not in self.name_and_contact:  # and new new is not already in the dictionary
                del self.name_and_contact[self.name]  # delete original(pre-filled) key:value pairs
                self.name_and_contact[name] = email, phone, address  # creates new key:value pairs with updated info
                tkinter.messagebox.showinfo('Information', 'Thank you, ' + name + "'s information has been updated.")

            elif name in self.name_and_contact:  # new name enter already exist in dictionary
                del self.name_and_contact[self.name]  # delete original(pre-filled) key:value pairs
                del self.name_and_contact[name]  # delete existing key:value pair to be updated so duplicates don't exist

                self.name_and_contact[name] = email, phone, address  # creates new key:value pair with updated info
                tkinter.messagebox.showinfo('Information', 'Thank you, ' + name + "'s information has been updated.")

        self.second_change_window.destroy()  # CLOSES OUT THE CHANGE POPUP WINDOW AFTER MESSAGE BOX IS CLOSED
        self.first_change_window.destroy()  # CLOSES OUT THE 2ND CHANGE POPUP WINDOW AFTER MESSAGE BOX IS CLOSED


class DeleteWindow:

    def __init__(self, master, name_and_contact):
        self.master = master
        self.name_and_contact = name_and_contact

        # CREATE INFO FOR DELETE POP UP WINDOW
        self.delete_window = tkinter.Toplevel(master)
        self.delete_window.title('DELETE CONTACT')
        self.delete_window.geometry('350x300')

        # FRAMES FOR DELETE WINDOW
        self.header_frame = tkinter.Frame(self.delete_window)
        self.first_frame = tkinter.Frame(self.delete_window)
        self.second_frame = tkinter.Frame(self.delete_window)

        # HEADER FRAME
        self.header_label = tkinter.Label(self.header_frame, text='ENTER NAME TO BE REMOVED')
        self.header_label.pack(side='top')

        # FIRST FRAME
        self.name_entry_label = tkinter.Label(self.first_frame, text='Full Name', font='bold')
        self.name_entry = tkinter.Entry(self.first_frame, width=40, bd=3)
        self.name_entry_label.pack(pady=15)
        self.name_entry.pack()

        # THIRD FRAME
        self.submit_button = tkinter.Button(self.second_frame, text='DELETE', cursor='hand2', font='bold', bg='green', command=self.delete)
        self.cancel_button = tkinter.Button(self.second_frame, text='Cancel', cursor='hand2', font='bold', bg='red', command=self.delete_window.destroy)
        self.submit_button.pack(side='top', pady=20)
        self.cancel_button.pack(side='bottom')

        # DELETE WINDOW PACK
        self.header_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()

    # METHOD WILL DELETE NAME AND EMAIL FROM DICTIONARY
    # METHOD IS RAN WHEN THE 'SUBMIT' BUTTON IS SELECTED IN DELETE POP UP WINDOW
    def delete(self):

        name = self.name_entry.get()

        if name in self.name_and_contact:  # IF NAME EXIST IN DICTIONARY, DELETE KEY-VALUE PAIR
            del self.name_and_contact[name]
            tkinter.messagebox.showinfo('CONTACT DELETED', name + ' has been deleted.')
        else:
            tkinter.messagebox.showinfo('DOH!', name + " Was Not Found\nLooks like you didn't need to delete " + name + ' after all!')

        self.delete_window.destroy()  # CLOSES OUT DELETE POP UP WINDOW WHEN MESSAGE BOX IS CLOSED


# FUNCTION TO START PROGRAM AND CALL INSTANCE TO INITIATE GUI INTERFACE
def main():
    try:
        input_file = open('name_and_contact.dat', 'rb')  # TRIES TO OPEN DATA FILE WITH 'RB' SO IT CAN PICKLE
        name_and_contact = pickle.load(input_file)  # DATA FOUND ON FILE WILL BE MAPPED TO VARIABLE
        # print(name_and_contact)  # USED TO TEST CONTENT OF FILE TO ENSURE READING DATA CORRECTLY
    except (FileNotFoundError, IOError):  # IF EITHER ERROR OCCURS, FOLLOWING WILL TAKE PLACE
        name_and_contact = {}  # CREATES AN EMPTY DICTIONARY SINCE ONE DOESN'T EXIST YET BASED ON ERROR OCCURRENCE
        # print('File Not Found, Please Add Data To Create New File')  # USED TO TEST EXCEPTION

    root = tkinter.Tk()  # CREATE ROOT WINDOW

    CustomerDirectoryMainMenu(root, name_and_contact)  # CALLS THE INSTANCE CLASS TO RUN GUI MAIN MENU

    tkinter.mainloop()  # INITIATES WINDOW LOOP


# STARTS THE PROGRAM
main()
